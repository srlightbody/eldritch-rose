#!/usr/bin/env python3
"""Generate every app theme file from palette.toml.

  python build/build.py            # write all app files + palette.lua
  python build/build.py check      # verify working tree matches (CI/pre-commit)
  python build/build.py templatize # regenerate templates from current drowned files

Only the 9 per-variant roles (base/surface/overlay/_nc/hl_low/hl_med/hl_high +
inactive_tab/border) and the display name vary between variants; everything else
is shared. Templates carry @@role@@ placeholders so a round-trip is byte-exact.
"""
import sys, tomllib, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TPL = Path(__file__).resolve().parent / "templates"
ROLES = ["base", "surface", "overlay", "_nc", "hl_low", "hl_med", "hl_high",
         "inactive_tab", "border"]

# app -> (theme dir, file extension). The default (drowned) file has no suffix.
APPS = {
    "alacritty": ("alacritty", ".toml"),
    "kitty":     ("kitty", ".conf"),
    "ghostty":   ("ghostty", ""),
    "foot":      ("foot", ".ini"),
    "wezterm":   ("wezterm", ".toml"),
    "tmux":      ("tmux", ".conf"),
    "k9s":       ("k9s", ".yaml"),
    "bat":       ("bat", ".tmTheme"),
    "delta":     ("delta", ".gitconfig"),
    "lazygit":   ("lazygit", ".yml"),
    "noctalia":  ("noctalia", ".json"),  # special path handling below
}


def load_palette():
    return tomllib.loads((ROOT / "palette.toml").read_text())


def shared_colors(pal):
    """Flat name->hex for colors identical across variants (accents/bright/delta)."""
    out = {}
    for k, v in pal["accents"].items():
        out[k] = v
    for k, v in pal["bright"].items():
        out[f"b_{k}"] = v
    for k, v in pal["delta"].items():
        out[f"d_{k}"] = v
    return out


def out_path(app, suffix):
    """Where the rendered file for `app`+variant lands."""
    d, ext = APPS[app]
    if app == "noctalia":
        name = "Eldritch Rose" + (f" {suffix}" if suffix else "")
        return ROOT / d / "colorschemes" / name / f"{name}.json"
    stem = "eldritch-rose" + (f"-{suffix.lower()}" if suffix else "")
    return ROOT / d / f"{stem}{ext}"


def render(template_text, variant, pal):
    """Fill placeholders for one variant."""
    v = pal["variants"][variant]
    out = template_text
    # placeholders carry bare hex digits; any leading '#' stays literal in the
    # template, so apps that write '#rrggbb' and apps that write bare 'rrggbb'
    # (foot) both round-trip.
    for role in ROLES:
        out = out.replace(f"@@{role}@@", v[role].lstrip("#"))
    for name, hx in shared_colors(pal).items():
        out = out.replace(f"@@{name}@@", hx.lstrip("#"))
    suffix = f" {v['suffix']}" if v["suffix"] else ""
    slug = "eldritch-rose" + (f"-{v['suffix'].lower()}" if v["suffix"] else "")
    return out.replace("@@name_suffix@@", suffix).replace("@@slug@@", slug)


def build_lua(pal):
    """Regenerate lua/eldritch-rose/palette.lua from the same source."""
    a = pal["accents"]
    L = []
    add = L.append
    add("-- Eldritch Rose palette: shared eldritch accents over a selectable dark ramp.")
    add("-- Variants change ONLY the ramp (base/surface/overlay/_nc + highlight grays);")
    add("-- accents and neutrals are shared. Select with:")
    add('--   require("eldritch-rose").setup({ variant = "void" })  -- or abyssal / miasma')
    add('local config = require("eldritch-rose.config")')
    add("")
    add("-- accents + neutrals, identical across every variant")
    add("local shared = {")
    for k in ("ash", "shroud", "text"):
        add(f'\t{k} = "{a[k]}",')
    add("")
    for k in ("ichor", "witchfire", "siren", "rift", "aether", "umbra", "blight"):
        add(f'\t{k} = "{a[k]}",')
    add("")
    add('\tnone = "NONE",')
    add("}")
    add("")
    add("-- per-variant dark ramp")
    add("local ramps = {")
    for name in pal["order"]:
        v = pal["variants"][name]
        for c in v["comment"]:
            add(f"\t-- {c}")
        add(f"\t{name} = {{")
        add(f'\t\tbase = "{v["base"]}", surface = "{v["surface"]}", '
            f'overlay = "{v["overlay"]}", _nc = "{v["_nc"]}",')
        add(f'\t\thighlight_low = "{v["hl_low"]}", highlight_med = "{v["hl_med"]}", '
            f'highlight_high = "{v["hl_high"]}",')
        add("\t},")
    add("}")
    add("")
    add("local built = {}")
    add("")
    add("-- Returns the merged palette for the configured variant. Memoized per variant")
    add("-- so the frequent parse_color() lookups don't rebuild it.")
    add("return function()")
    add("\tlocal v = config.options.variant")
    add('\tif v == "auto" then v = config.options.dark_variant end')
    add('\tif not ramps[v] then v = "drowned" end')
    add("\tif not built[v] then")
    add("\t\tbuilt[v] = vim.tbl_extend(\"force\", {}, ramps[v], shared)")
    add("\tend")
    add("\treturn built[v]")
    add("end")
    return "\n".join(L) + "\n"


def all_outputs(pal):
    """Yield (path, rendered_text) for every app x variant, plus palette.lua."""
    for app in APPS:
        tpl = (TPL / f"{app}.tmpl").read_text()
        for name, v in pal["variants"].items():
            yield out_path(app, v["suffix"]), render(tpl, name, pal)
    yield ROOT / "lua" / "eldritch-rose" / "palette.lua", build_lua(pal)


def cmd_build(pal):
    n = 0
    for path, text in all_outputs(pal):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
        n += 1
    print(f"wrote {n} files")


def cmd_check(pal):
    drift = 0
    for path, text in all_outputs(pal):
        cur = path.read_text() if path.exists() else ""
        if cur != text:
            drift += 1
            rel = path.relative_to(ROOT)
            print(f"DRIFT: {rel}")
            for line in difflib.unified_diff(
                cur.splitlines(), text.splitlines(),
                fromfile=f"{rel} (working tree)", tofile=f"{rel} (generated)", lineterm=""):
                print("  " + line)
    if drift:
        print(f"\n{drift} file(s) out of sync — run: python build/build.py")
        sys.exit(1)
    print("all files match palette.toml")


def cmd_templatize(pal):
    """Rebuild templates from the current drowned files (dev-only)."""
    d = pal["variants"]["drowned"]
    # roles first, then shared; on a hex collision (cursor==blight) the first
    # wins, keeping a single deterministic placeholder per hex.
    hex_to_ph = {}
    for r in ROLES:
        hex_to_ph.setdefault(d[r].lstrip("#").lower(), f"@@{r}@@")
    for name, hx in shared_colors(pal).items():
        hex_to_ph.setdefault(hx.lstrip("#").lower(), f"@@{name}@@")
    TPL.mkdir(parents=True, exist_ok=True)
    for app in APPS:
        text = out_path(app, "").read_text()
        for hx, ph in hex_to_ph.items():
            text = text.replace("#" + hx, "#" + ph)  # '#rrggbb' -> '#@@role@@'
            text = text.replace(hx, ph)               # bare 'rrggbb' -> '@@role@@'
        # tmux's source-file comment names this variant's own file; other apps'
        # include hints point at the generic active file, so leave their slug.
        if app == "tmux":
            text = text.replace("eldritch-rose.conf", "@@slug@@.conf")
        text = text.replace("Eldritch Rose", "Eldritch Rose@@name_suffix@@")
        (TPL / f"{app}.tmpl").write_text(text)
    print(f"regenerated {len(APPS)} templates")


if __name__ == "__main__":
    pal = load_palette()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "build"
    {"build": cmd_build, "check": cmd_check, "templatize": cmd_templatize}[cmd](pal)

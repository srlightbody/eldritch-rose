# Eldritch Rose

A mashup theme: [Rose Pine](https://rosepinetheme.com/)'s muted backgrounds and
structure with [Eldritch](https://github.com/eldritch-theme)'s vivid cool accents
and neon-green cursor. Dark, low-contrast base; the blues, cyans, and purples pop.

## Palette

| Role            | Hex       | Source     |
|-----------------|-----------|------------|
| base (bg)       | `#0e0218` | violet     |
| surface         | `#17112b` | violet     |
| overlay         | `#241a38` | violet     |
| muted           | `#6e6a86` | rose pine  |
| subtle          | `#908caa` | rose pine  |
| text (fg)       | `#ebfafa` | eldritch   |
| love (red)      | `#eb6f92` | rose pine  |
| gold (yellow)   | `#f6c177` | rose pine  |
| rose            | `#f48fc9` | eldritch   |
| pine (blue)     | `#4d8bff` | azure      |
| foam (cyan)     | `#04d1f9` | eldritch   |
| iris (purple)   | `#a48cf2` | eldritch   |
| leaf (green)    | `#37f499` | eldritch   |
| cursor          | `#37f499` | eldritch   |
| selection       | `#403d52` | rose pine  |

### 16-color ANSI

```
normal   0 #26233a  1 #eb6f92  2 #37f499  3 #f6c177  4 #4d8bff  5 #a48cf2  6 #04d1f9  7 #e0def4
bright   8 #6e6a86  9 #f9515d 10 #69f8b3 11 #f1fc79 12 #7aa6ff 13 #fd92ce 14 #66e4fd 15 #ebfafa
```

## Install

Each app needs only its one file. The fastest path per app is below; no full
clone required. Replace the raw URL base if you fork it.

### Neovim

Nothing to download by hand, the plugin manager fetches it. It's self
contained (no dependencies). With lazy.nvim:

```lua
{
	"srlightbody/eldritch-rose",
	lazy = false,
	priority = 1000,
	config = function()
		vim.cmd.colorscheme("eldritch-rose")
	end,
}
```

packer:

```lua
use({ "srlightbody/eldritch-rose" })
-- then: vim.cmd.colorscheme("eldritch-rose")
```

### Ghostty

Drop the theme file into ghostty's themes dir and point at it:

```sh
mkdir -p ~/.config/ghostty/themes
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/ghostty/eldritch-rose \
	-o ~/.config/ghostty/themes/eldritch-rose
```

```
# ~/.config/ghostty/config
theme = eldritch-rose
```

Reload with `ctrl+shift+,` (or `cmd+shift+,` on macOS).

### Alacritty (0.13+)

```sh
mkdir -p ~/.config/alacritty/themes
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/alacritty/eldritch-rose.toml \
	-o ~/.config/alacritty/themes/eldritch-rose.toml
```

```toml
# ~/.config/alacritty/alacritty.toml
[general]
import = ["~/.config/alacritty/themes/eldritch-rose.toml"]
```

### tmux

```sh
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/tmux/eldritch-rose.conf \
	-o ~/.config/tmux/eldritch-rose.conf
```

```
# ~/.config/tmux/tmux.conf
source-file ~/.config/tmux/eldritch-rose.conf
```

Reload with `tmux source-file ~/.config/tmux/tmux.conf`.

### VS Code

Until it's on the marketplace, install it as a local extension by symlinking the
`vscode/` folder into your extensions dir:

```sh
git clone https://github.com/srlightbody/eldritch-rose ~/.eldritch-rose
ln -s ~/.eldritch-rose/vscode ~/.vscode/extensions/eldritch-rose
```

Reload the window, then `Ctrl+Shift+P` (`Cmd+Shift+P` on macOS) → "Preferences:
Color Theme" → Eldritch Rose.

### foot

```sh
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/foot/eldritch-rose.ini \
	-o ~/.config/foot/eldritch-rose.ini
```

```ini
# ~/.config/foot/foot.ini
include=~/.config/foot/eldritch-rose.ini
```

### kitty

```sh
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/kitty/eldritch-rose.conf \
	-o ~/.config/kitty/eldritch-rose.conf
```

```conf
# ~/.config/kitty/kitty.conf
include ./eldritch-rose.conf
```

### wezterm

```sh
mkdir -p ~/.config/wezterm/colors
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/wezterm/eldritch-rose.toml \
	-o ~/.config/wezterm/colors/eldritch-rose.toml
```

```lua
-- wezterm.lua
config.color_scheme = "Eldritch Rose"
```

### bat

```sh
mkdir -p "$(bat --config-dir)/themes"
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/bat/eldritch-rose.tmTheme \
	-o "$(bat --config-dir)/themes/eldritch-rose.tmTheme"
bat cache --build
```

```sh
# ~/.config/bat/config
--theme="Eldritch Rose"
```

### delta

Needs the bat theme above (delta uses bat's syntax themes).

```sh
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/delta/eldritch-rose.gitconfig \
	-o ~/.config/delta/eldritch-rose.gitconfig
```

```ini
# ~/.gitconfig
[include]
	path = ~/.config/delta/eldritch-rose.gitconfig
```

### lazygit

Merge `lazygit/eldritch-rose.yml` into `~/.config/lazygit/config.yml` (it's the
`gui.theme` block).

### k9s

```sh
mkdir -p ~/.config/k9s/skins
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/k9s/eldritch-rose.yaml \
	-o ~/.config/k9s/skins/eldritch-rose.yaml
```

```yaml
# ~/.config/k9s/config.yaml
k9s:
  ui:
    skin: eldritch-rose
```

### lsd

```sh
curl -fsSL https://raw.githubusercontent.com/srlightbody/eldritch-rose/main/lsd/eldritch-rose.yaml \
	-o ~/.config/lsd/colors.yaml
```

### Noctalia

Drop the colorscheme directory into noctalia's colorschemes folder, then pick it
in noctalia's settings (noctalia generates the per-terminal files itself):

```sh
mkdir -p ~/.config/noctalia/colorschemes
cp -r "noctalia/colorschemes/Eldritch Rose" ~/.config/noctalia/colorschemes/
```

## Notes

- The neovim theme is standalone: it vendors and adapts rose-pine/neovim's
  highlight engine (MIT, see LICENSE) and drives it from the palette above, so
  there's no runtime dependency and it's free to drift from rose pine over time.
- Blue is an azure (`#4d8bff`) kept distinct from the eldritch cyan ramp
  (`#04d1f9`/`#66e4fd`); eldritch's own purple-blue is deliberately dropped. In
  neovim, keywords take the azure (pine) and types take the cyan (foam).
- Warm accents (red/gold) stay stock rose pine; rose is pushed to an electric
  fuchsia, and the cool ones plus the cursor are eldritch.

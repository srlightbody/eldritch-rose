# Eldritch Rose

A mashup theme: [Rose Pine](https://rosepinetheme.com/)'s muted backgrounds and
structure with [Eldritch](https://github.com/eldritch-theme)'s vivid cool accents
and neon-green cursor. Dark, low-contrast base; the blues, cyans, and purples pop.

## Palette

| Role            | Hex       | Source     |
|-----------------|-----------|------------|
| base (bg)       | `#191724` | rose pine  |
| surface         | `#1f1d2e` | rose pine  |
| overlay         | `#26233a` | rose pine  |
| muted           | `#6e6a86` | rose pine  |
| subtle          | `#908caa` | rose pine  |
| text (fg)       | `#ebfafa` | eldritch   |
| love (red)      | `#eb6f92` | rose pine  |
| gold (yellow)   | `#f6c177` | rose pine  |
| rose            | `#ebbcba` | rose pine  |
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

## Notes

- The neovim theme is standalone: it vendors and adapts rose-pine/neovim's
  highlight engine (MIT, see LICENSE) and drives it from the palette above, so
  there's no runtime dependency and it's free to drift from rose pine over time.
- Blue is an azure (`#4d8bff`) kept distinct from the eldritch cyan ramp
  (`#04d1f9`/`#66e4fd`); eldritch's own purple-blue is deliberately dropped. In
  neovim, keywords take the azure (pine) and types take the cyan (foam).
- Warm accents (red/gold/rose) stay stock rose pine; only the cool ones plus the
  cursor are eldritch.

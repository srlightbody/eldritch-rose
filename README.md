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

### Ghostty

Copy or symlink the theme into ghostty's themes directory, then set it:

```sh
ln -s ~/Projects/eldritch-rose/ghostty/eldritch-rose ~/.config/ghostty/themes/eldritch-rose
```

```
# ~/.config/ghostty/config
theme = eldritch-rose
```

### Alacritty (0.13+)

```toml
# ~/.config/alacritty/alacritty.toml
[general]
import = ["~/Projects/eldritch-rose/alacritty/eldritch-rose.toml"]
```

### Neovim

Builds on `rose-pine/neovim` (required dependency). With lazy.nvim:

```lua
{
	dir = "~/Projects/eldritch-rose/nvim",
	name = "eldritch-rose",
	dependencies = { "rose-pine/neovim" },
	config = function()
		vim.cmd("colorscheme eldritch-rose")
	end,
}
```

### tmux

```
# ~/.config/tmux/tmux.conf
source-file ~/Projects/eldritch-rose/tmux/eldritch-rose.conf
```

## Notes

- Blue is an azure (`#4d8bff`) kept distinct from the eldritch cyan ramp
  (`#04d1f9`/`#66e4fd`); eldritch's own purple-blue is deliberately dropped. In
  neovim, keywords take the azure (pine) and types take the cyan (foam).
- The neovim theme intentionally keeps rose pine's warm accents (red/gold/rose)
  stock and only brightens the cool ones plus the cursor.

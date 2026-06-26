local M = {}

local palette = require("eldritch-rose.palette")

-- Eldritch Rose builds on rose-pine.nvim: the "main" variant supplies the
-- structure and backgrounds, these overrides swap the cool accents to eldritch
-- and set the neon-green cursor.
function M.load()
	local ok, rose = pcall(require, "rose-pine")
	if not ok then
		vim.notify("eldritch-rose: rose-pine.nvim is required", vim.log.levels.ERROR)
		return
	end

	rose.setup({
		variant = "main",
		dark_variant = "main",
		palette = {
			main = {
				text = palette.text,
				pine = palette.pine,
				foam = palette.foam,
				iris = palette.iris,
			},
		},
		highlight_groups = {
			Cursor = { fg = palette.base, bg = palette.leaf },
		},
	})

	-- call rose-pine's apply fn directly; a nested :colorscheme is a no-op
	-- when invoked from inside our own colors/ file
	rose.colorscheme("main")
	vim.g.colors_name = "eldritch-rose"
end

return M

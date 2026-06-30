-- Eldritch Rose palette: shared eldritch accents over a selectable dark ramp.
-- Variants change ONLY the ramp (base/surface/overlay/_nc + highlight grays);
-- accents and neutrals are shared. Select with:
--   require("eldritch-rose").setup({ variant = "void" })  -- or abyssal / miasma
local config = require("eldritch-rose.config")

-- accents + neutrals, identical across every variant
local shared = {
	ash = "#6e6a86",
	shroud = "#908caa",
	text = "#ebfafa",

	ichor = "#eb6f92",
	witchfire = "#e8be22",
	siren = "#f48fc9",
	rift = "#4d8bff",
	aether = "#04d1f9",
	umbra = "#a48cf2",
	blight = "#37f499",

	none = "NONE",
}

-- per-variant dark ramp
local ramps = {
	-- drowned: teal deep (default) — R'lyeh, the sunken
	drowned = {
		base = "#08161a", surface = "#0f2329", overlay = "#163139", _nc = "#050f12",
		highlight_low = "#20262a", highlight_med = "#3e4750", highlight_high = "#505a64",
	},
	-- void: near-black violet (the original eldritch base)
	void = {
		base = "#0e0218", surface = "#17112b", overlay = "#241a38", _nc = "#0a0214",
		highlight_low = "#21202e", highlight_med = "#403d52", highlight_high = "#524f67",
	},
	-- abyssal: deep cosmic blue
	abyssal = {
		base = "#0a1020", surface = "#141b30", overlay = "#1f2942", _nc = "#070b18",
		highlight_low = "#1f2330", highlight_med = "#3a4358", highlight_high = "#4c576e",
	},
	-- miasma: toxic deep green — for the dramatic
	miasma = {
		base = "#0a140e", surface = "#11201a", overlay = "#1a2e25", _nc = "#070f0a",
		highlight_low = "#1f2922", highlight_med = "#384e42", highlight_high = "#4a6055",
	},
}

local built = {}

-- Returns the merged palette for the configured variant. Memoized per variant
-- so the frequent parse_color() lookups don't rebuild it.
return function()
	local v = config.options.variant
	if v == "auto" then v = config.options.dark_variant end
	if not ramps[v] then v = "drowned" end
	if not built[v] then
		built[v] = vim.tbl_extend("force", {}, ramps[v], shared)
	end
	return built[v]
end

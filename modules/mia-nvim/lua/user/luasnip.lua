local ls = require "luasnip"
local types = require "luasnip.util.types"

-- Path for my snippets
require("luasnip.loaders.from_lua").load({ paths = "~/.config/nvim/snippets/" })

ls.config.set_config({
	-- Remembers your last luasnip
	history = true,

	-- Dynamic snippets
	updateevents = "TextChanged,TextChangedI",

	-- Autosnippets:
	enable_autosnippets = true,

	-- Yet to understand this
	ext_opts = {
		[types.choiceNode] = {
			active = {
				virt_text = { { "<-", "Error" } },
			},
		},
	},
})

--Key Maps

-- Expand
vim.keymap.set({ "i", "s" }, "<a-a>", function()
	if ls.expand_or_jumpable() then
		ls.expand_or_jump()
	end
end, { silent = true})


-- Jump
vim.keymap.set({ "i", "s" }, "<a-k>", function()
	if ls.jumpable(1) then
		ls.jump(1)
	end
end, { silent = true})

vim.keymap.set({ "i", "s" }, "<a-j>", function()
	if ls.jumpable(-1) then
		ls.jump(-1)
	end
end, { silent = true})

-- Cycle trough choices
vim.keymap.set({ "i", "s" }, "<a-l>", function()
	if ls.choice_active() then
		ls.change_choice(1)
	end
end, { silent = true})

vim.keymap.set({ "i", "s" }, "<a-h>", function()
	if ls.choice_active() then
		ls.change_choice(-1)
	end
end, { silent = true})

-- Source luasnips file again, handy QOL :)
vim.keymap.set("n", "<leader><leader>s", "<cmd>source ~/.config/nvim/lua/user/luasnip.lua<CR>")

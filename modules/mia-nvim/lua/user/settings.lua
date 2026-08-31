local set = vim.opt

----------------------------

-- Tab behaviour
set.tabstop = 4
set.shiftwidth = 4
set.softtabstop = 4
set.expandtab = false

-- Know position of cursor always
set.ruler = true

-- Show relative number
set.relativenumber = true

-- Colorscheme
set.termguicolors = true
vim.cmd('colorscheme kanagawa ')

-- Minimum pane width for windows.nvim plugin
set.winwidth = 15
set.winminwidth = 15
set.equalalways = false

-- Makes clipboard use the +/* register automatically
set.clipboard = 'unnamedplus'

-- Disable diagnostic virtual text
vim.diagnostic.config({
	virtual_text = false
})

-- Just changing the title of the tabline
local aeron = "Aeron lab"
set.showtabline = 2
set.tabline=aeron


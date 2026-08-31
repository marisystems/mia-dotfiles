-- Not sure what this does, but seems to not initialize plugin if not avaiable
local status_ok, toggleterm = pcall(require, "toggleterm")

if not status_ok then
	return
end

-- Setup itself
toggleterm.setup({
	size = 20,
	open_mapping = [[<C-\>]],
	hide_numbers = true,
	shade_filetypes = {},
	shade_terminals = true,
	shading_factor = 2,
	start_in_insert = true,
	insert_mappings = true,
	persist_size = true,
	direction = "float",
	close_on_exit = true,
	float_opts = {
		border = "curved",
		winblend = 0,
		highlights = {
			border = "Normal",
			background = "Normal",
		},
	},
})

-- Handy names
local Terminal = require("toggleterm.terminal").Terminal
local lazygit = Terminal:new({ cmd = "lazygit", hidden = true})

-- Global function declarations

function _LAZYGIT_TOGGLE()
	lazygit:toggle()
end


local python = Terminal:new({ cmd = "python", hidden = true })

function  _PYTHON_TOGGLE()
	python:toggle()
end


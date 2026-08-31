-- Where i manage all my plugin installs

return require('packer').startup(function(use)
	
	-- Packer can manage itself
	use 'wbthomason/packer.nvim'

	-- Terminal emulator
	use 'akinsho/toggleterm.nvim'

	-- Telescope
	use {'nvim-telescope/telescope.nvim', tag = '0.1.0',
	requires = {'nvim-lua/plenary.nvim'} }
	use 'nvim-treesitter/nvim-treesitter'

	-- Displays popup with possible keybindings for a command
	use 'folke/which-key.nvim'

	-- LSP server
	use 'neovim/nvim-lspconfig'

	-- Mason Packager for LSP Servers
	use 'williamboman/mason.nvim'

	-- CMP
	use 'hrsh7th/nvim-cmp'			-- Core of auto completion Plugin
	use 'hrsh7th/cmp-buffer'		-- Buffer completions
	use 'hrsh7th/cmp-path'			-- Path completions
	use 'hrsh7th/cmp-cmdline'		-- Cmdline completions
	use 'hrsh7th/cmp-nvim-lua'		-- Inbuilt completions for nvim lua API
	use 'hrsh7th/cmp-nvim-lsp'		-- Inbuilt completions for LSP server
	use 'onsails/lspkind.nvim'		-- Icons for the completion types

	-- LuaSnip
	use 'L3MON4D3/LuaSnip'			-- Snippet engine built on lua
	use 'saadparwaiz1/cmp_luasnip'	-- Snippet completions for cmp

	--DAP (Debugger adapter Protocol)
	use 'mfussenegger/nvim-dap'		-- Not quite sure yet what it does

	-- Misc Implementations
	use 'elkowar/yuck.vim'						-- Used in elkowar EWW yuck language
	use 'PrestonKnopp/tree-sitter-gdscript'		-- Tree sitter for Godot's Language GDscript

	-- Javascript
	use 'yuezk/vim-js'					--　I'll probably delete this later
	use 'maxmellon/vim-jsx-pretty'		-- And this one


	-- VISUAL --
	-- Status-line
	use {
		'nvim-lualine/lualine.nvim',
		requires = {'nvim-tree/nvim-web-devicons', opt = true}
	}

	-- Change pane focus with fancy animations
	use {"anuvyklack/windows.nvim", requires = {"anuvyklack/middleclass",
		"anuvyklack/animation.nvim"}
	}

	-- Notifications support
	use 'rcarriga/nvim-notify'

    -- Indent lines
    use 'lukas-reineke/indent-blankline.nvim'

	-- Auto close tags html
	use 'windwp/nvim-ts-autotag'

	-- Colorizer
	use 'norcalli/nvim-colorizer.lua'

	-- Colorscheme
	use 'cocopon/iceberg.vim'
	use "rebelot/kanagawa.nvim"
end)

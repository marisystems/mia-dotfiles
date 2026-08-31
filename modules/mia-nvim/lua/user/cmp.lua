local cmp = require'cmp'	-- Completion Engine
local lspkind = require'lspkind'	-- Pretty icons
local luasnip = require'luasnip'	-- Snip engine

cmp.setup({

	snippet = {
		-- Specifying the snippet engine
		expand = function(args)
			luasnip.lsp_expand(args.body)
		end,
	},

	window = {
		-- completion = cmp.config.window.bordered(),
		-- documentation = cmp.config.window.bordered(),
	},

	-- Add your keybindings here
	mapping = cmp.mapping.preset.insert({
		['<C-k>'] = cmp.mapping.select_prev_item(),
        ['<C-j>'] = cmp.mapping.select_next_item(),

		['<C-d>'] = cmp.mapping.scroll_docs(-4),
		['<C-f>'] = cmp.mapping.scroll_docs(4),
		['<C-Space>'] = cmp.mapping.complete(),	
		['<C-e>'] = cmp.mapping.abort(),
		['<C-a>'] = cmp.mapping.confirm({ select = true }),

	}),

	-- Configure the formatting of the cmp pop_up window
	formatting = ({
		format = lspkind.cmp_format({
		mode = 'symbol',
		maxwidth = 50,
		ellipsis_char = '...',
		}),
	}),

	-- Set the sources for cmp
	sources = cmp.config.sources({
		{ name = 'nvim_lua' },
		{ name = 'nvim_lsp' },
		{ name = 'path' },
		{ name = 'luasnip' },
		{ name = 'buffer', keyword_length = 3 },
	})

})


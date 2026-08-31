local ls = require "luasnip"

ls.snippets = {
	all = {
		ls.parser.parse_snippet("expand", "--A silly little comment!")
	},

	lua = {
		-- Lua specific snippets
	},
}


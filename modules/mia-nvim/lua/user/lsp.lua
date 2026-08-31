langs =
{
	'pyright',
	'clangd',
	'gopls',
	'lua_ls',
	'html',
	'eslint',
	'tsserver',
	'rust_analyzer',
}

for i, langs in ipairs(langs) do
	require('lspconfig')[langs].setup{}
end


-- CSS workaround for completions

local capabilities = vim.lsp.protocol.make_client_capabilities()
capabilities.textDocument.completion.completionItem.snippetSupport = true

require'lspconfig'.cssls.setup {
	capabilities = capabilities,
}

-- GdScript
local lsp_flags = {
	debounce_text_changes = 150,
}

require'lspconfig'.gdscript.setup{
	flags = lsp_flags,
	filetypes = { "gd", "gdscript", "gdscript3" },
}


-- Explicitly calling the options tolists buffers and enable icons
require('lualine').setup{
	options = {
		icons_enabled = true,
		theme = 'onedark',
		component_separators = '|',
		sections_separators = '',
	},
	sections = {
		lualine_a = {
			{
				'buffers',
			}
		}

	}

}

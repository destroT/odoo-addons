# Copyright 2022 CreuBlanca
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Web Dark",
    "summary": """
        Allow dark mode using Odoo CE""",
    "version": "17.0.1.0.0",
    "license": "AGPL-3",
    "author": "Tommaso Destro",
    "depends": ["web"],
    'data': [
        'views/webclient_templates.xml',
    ],
    "assets": {
        'web._assets_primary_variables': [
            # ('after', 'web/static/src/scss/primary_variables.scss', 'web_dark/static/src/**/*.variables.scss'),
            ('before', 'web/static/src/scss/primary_variables.scss', 'web_dark/static/src/scss/primary_variables.scss'),
        ],
        'web._assets_secondary_variables': [
            ('before', 'web/static/src/scss/secondary_variables.scss', 'web_dark/static/src/scss/secondary_variables.scss'),
        ],
        'web._assets_backend_helpers': [
            ('before', 'web/static/src/scss/bootstrap_overridden.scss', 'web_dark/static/src/scss/bootstrap_overridden.scss'),
        ],
        'web.assets_common': [
            'web_dark/static/src/views/navbar.scss',
        ],
        "web.assets_backend": [
            "web_dark/static/src/js/**",
            'web_dark/static/src/views/navbar.scss'
            # Don't include dark mode files in light mode
            # ('remove', 'web_enterprise/static/src/**/*.dark.scss'),
        ],
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'web_dark/static/src/scss/primary_variables.scss', 'web_dark/static/src/scss/primary_variables.dark.scss'),
            # ('before', 'web_dark/static/src/**/*.variables.scss', 'web_dark/static/src/**/*.variables.dark.scss'),
            # web._assets_secondary_variables
            ('before', 'web_dark/static/src/scss/secondary_variables.scss', 'web_dark/static/src/scss/secondary_variables.dark.scss'),
        ],
        "web.assets_web_dark": [
            ('include', 'web.dark_mode_variables'),
            # web._assets_backend_helpers
            ('before', 'web_dark/static/src/scss/bootstrap_overridden.scss', 'web_dark/static/src/scss/bootstrap_overridden.dark.scss'),
            ('after', 'web/static/lib/bootstrap/scss/_functions.scss', 'web_dark/static/src/scss/bs_functions_overridden.dark.scss'),
            # assets_backend
            'web_dark/static/src/**/*.dark.scss',
        ],
        
        # "web.dark_mode_variables": [
        #     (
        #         "before",
        #         "web_dark/static/src/scss/primary_variables.scss",
        #         "web_dark/static/src/scss/dark_variables.scss",
        #     ),
        # ],
        # "web.dark_mode_assets_common": [
        #     # ("include", "web.dark_mode_variables"),
        # ],
        # "web.dark_mode_assets_backend": [
        #     ("include", "web.dark_mode_variables"),
        #     "web_dark/static/src/scss/dark_mode.scss",
        # ],
    },
}

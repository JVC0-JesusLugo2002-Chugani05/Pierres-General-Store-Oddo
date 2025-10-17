{
    "name": "Pierre's Store Theme",
    "version": "17.0.1.0.0",
    "category": "Themes/Backend",
    "description": """Fork of Hue Backend Theme, by Cybrosys Techno Solutions,
    made with love for SSG homework of Multiplatform App Development formation""",
    "author": "JesusLugo2002",
    "depends": ["web", "mail"],
    "data": [
        "views/layout_templates.xml",
        "views/res_config_settings_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "pierres_store_theme/static/src/components/app_menu/side_menu.xml",
            "pierres_store_theme/static/src/layout/style/layout_colors.scss",
            "pierres_store_theme/static/src/components/app_menu/menu_order.css",
            "pierres_store_theme/static/src/layout/style/layout_style.scss",
            "pierres_store_theme/static/src/layout/style/sidebar.scss",
            "pierres_store_theme/static/src/components/app_menu/search_apps.js",
        ],
        "web.assets_frontend": [
            "pierres_store_theme/static/src/layout/style/login.scss",
        ],
    },
    "images": [
        "static/description/banner.png",
        "static/description/theme_screenshot.png",
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}

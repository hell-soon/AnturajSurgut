JAZZ_SETTINGS = {
    # Настройка сайта
    "site_title": "Антураж",
    "site_header": "Антураж",
    "welcome_sign": "Добро пожаловать в Антураж",
    "copyright": "Антураж",
    # Панель управления
    # моадльное окно
    "related_modal_active": True,
    "use_modal_dialog_for_popups": True,
    # Панель кастомизации(только на время разработки)
    "show_ui_builder": True,
    # гугл шрифты
    "use_google_fonts_cdn": True,
    # Навигация(sidebar)
    "navigation_expanded": True,
    # Models icons
    "icons": {
        "auth": "fas fa-users-cog",
        "users.CustomUser": "fas fa-users",
        "auth.Group": "fas fa-users",
        "DB.Product": "fa-solid fa-shirt",
        "DB.Catalog": "fa-solid fa-list-ul",
        "DB.Tags": "fa-solid fa-tags",
        "DB.Color": "fa-solid fa-palette",
        "DB.Size": "fa-solid fa-ruler",
        "DB.ProductImage": "fa-solid fa-image",
        "DB.Compound": "fa-solid fa-list-ol",
        "order.Order": "fa-solid fa-truck-fast",
        "order.Additionalservices": "fa-solid fa-plus",
        "order.OrderType": "fas fa-receipt",
        "order.OrderFace": "fa-solid fa-user-tie",
        "order.PaymentType": "fa-solid fa-credit-card",
        "reviews.Review": "fa-solid fa-comment",
        "reviews.Feedback": "fa-solid fa-certificate",
        "sitedb.Slider": "fa-solid fa-sliders",
        "sitedb.News": "fa-solid fa-newspaper",
        "sitedb.Service": "fa-solid fa-list",
        "sitedb.OurWork": "fa-solid fa-briefcase",
        "sitedb.OurWorkImage": "fa-solid fa-image",
        "sitedb.Sertificate": "fa-solid fa-certificate",
        "sitedb.SiteInfo": "fa-solid fa-house",
        "sitedb.Vacancy": "fa-solid fa-certificate",
        "telegram.TelegramImage": "fa-solid fa-image",
        "telegram.TelegramNews": "fa-solid fa-paper-plane",
        "smsru.Log": "fa-solid fa-sms",
    },
    # TOP MENU
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.Group"},
    ],
    # FORMS
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    # SIDE BAR LIST MODELS AND APP
    "order_with_respect_to": [
        "DB",
        "DB.Product",
        "DB.Catalog",
        "DB.SubCatalog",
        "DB.Tags",
        "DB.Color",
        "DB.Size",
        "DB.ProductImage",
        "Support",
        "order",
        "order.Order",
        "sitedb",
        "sitedb.Slider",
        "sitedb.Service",
        "sitedb.News",
        "sitedb.OurWork",
        "sitedb.Sertificate",
        "telegram",
        "telegram.TelegramNews",
    ],
    "custom_links": {
        "books": [
            {
                # Any Name you like
                "name": "Тест",
                # url name e.g `admin:index`, relative urls e.g `/admin/index` or absolute urls e.g `https://domain.com/admin/index`
                "url": "admin:index",
                # any font-awesome icon, see list here https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2 (optional)
                "icon": "fas fa-comments",
                # a list of permissions the user must have to see this link (optional)
            }
        ]
    },
    #
    # Скрыть модели
    "hide_apps": ["auth", "AuthToken"],
    "hide_models": ["auth.groups", "auth.tokens.Tokens", "DB.Type"],
    # "language_chooser": True,
    "search_model": ["DB.Product"],
}

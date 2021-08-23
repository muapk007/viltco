# -*- coding: utf-8 -*-
{
    'name': "HelpDesk Customization",

    'summary': """
       Make a HelpDesk Customization""",

    'description': """
       Make a HelpDesk Customization
    """,

    'author': "Viltco",
    'website': "https://viltco.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'helpdesk',
    'version': '14.0.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'helpdesk', 'stock', 'maintenance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/product_views.xml',
        'views/helpdesk_views.xml',
        'views/maintenance_views.xml',
        'views/request.xml',
        'views/site_type.xml',
    ],

}

# -*- coding: utf-8 -*-
{
    'name': "Odoo Tricks",

    'summary': """
        Odoo Tricks
        """,

    'description': """
        Odoo Trick and Tips
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'odoo_tricks/static/js/update_po.js',
        ],
    },
}

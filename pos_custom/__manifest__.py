# -*- coding: utf-8 -*-
{
    'name': "BIK | Pos Custom",
    'summary': '',
    'description': """""",
    'author': "Bayu Indra Kusuma",
    'website': "bayuik.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [

    ],
    'qweb': [
        'static/src/xml/Screens/ProductScreen/NumpadWidget.xml',
    ]
}

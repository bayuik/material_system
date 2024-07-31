# -*- coding: utf-8 -*-
{
    'name': "BIK | Material System",
    'summary': 'Module for registering materials for sale',
    'description': """Module for registering materials for sale""",
    'author': "Bayu Indra Kusuma",
    'website': "bayuik.dev",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/material_system_views.xml',
        'views/menuitems.xml',
    ],
}

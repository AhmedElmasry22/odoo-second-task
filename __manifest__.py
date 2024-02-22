# -*- coding: utf-8 -*-
{
    'name': "Letters Of Guarantee",

    'summary': """
       Letters Guarantee""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ahmed Salah",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/letter.xml',
        'wizard/letter_report_wizard.xml',
        'wizard_pages/letter_wizard_diff.xml',
        'views/sequance_view.xml',
        'reports/report.xml',


    ],
    # only loaded in demonstration mode

}

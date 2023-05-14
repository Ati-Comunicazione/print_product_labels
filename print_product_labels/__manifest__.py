{
    'name': "print_product_labels 1",

    'summary': """
        Print product labels
    """,

    'description': """
        Print product labels
    """,

    'author': "Huroos",
    'website': "https://www.huroos.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],
    'images': ['static/description/icon.png'],
    'data': [
        'data/report_paperformat.xml',
        'report/product_product_templates.xml',
        'report/product_reports.xml',
    ],
}

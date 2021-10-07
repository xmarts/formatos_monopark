# -*- coding: utf-8 -*-
{
    'name': "formatos_compra_inventario",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Xmarts",
    'Collaborators': "Gilberto Santiago Acevedo",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','contacts','stock','hr'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/reporte_pedido_compra.xml',
        'report/layout_formato_instalacion.xml',
        'report/template_formato_instalacion.xml',
        'report/layout_formato_entrega_cliente.xml',
        'report/template_formato_entrega_cliente.xml',
        'report/formato_vale_entrega.xml',
        'report/layout_vale_entrega.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
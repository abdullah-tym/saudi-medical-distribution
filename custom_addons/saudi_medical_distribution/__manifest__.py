{
    'name': 'Saudi Medical Distribution Compliance',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    'summary': 'SFDA Article 14 & Cold Chain Compliance',
    'depends': ['base', 'product', 'stock'],
    'data': [
        'views/product_view.xml',
        'views/stock_picking_view.xml',
        'views/stock_lot_view.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}

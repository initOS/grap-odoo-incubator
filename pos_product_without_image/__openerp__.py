# coding: utf-8
# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Point of Sale - Improve Display of Products without images',
    'summary': 'Improvements on Display of products images',
    'version': '8.0.1.0.0',
    'category': 'Point Of Sale',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'pos_default_empty_image',
    ],
    'data': [
        'views/templates.xml',
    ],
    'images': [
        'static/description/point_of_sale.png',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-
{
    'name': "Snail Mail",
    'description': """
Allows users to send documents by post
=====================================================
        """,
    'category': 'Tools',
    'version': '0.1',
    'depends': ['iap', 'base_setup'],
    'data': [
        'data/snailmail_data.xml',
        'views/res_config_settings_views.xml',
        'views/snailmail_views.xml',
        'security/ir.model.access.csv',
    ],
    'auto_install': True,
}

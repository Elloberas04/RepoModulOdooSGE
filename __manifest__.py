# -*- coding: utf-8 -*-
{
    'name': "Gestio de Reunions",

    'summary': "Mòdul per a la planificació, seguiment i documentació eficient de reunions empresarials.",

    'description': """
        Aquest mòdul proporciona una interfície àgil i amigable per a la gestió integral de reunions en entorns empresarials. S'integra perfectament amb mòduls existents com el calendari i els contactes a Odoo.

        Característiques clau:
        - Creació i planificació de noves reunions en un calendari centralitzat.
        - Assignació de participants i objectius de la reunió.
        - Recordatoris per garantir la puntualitat.
        - Gestió de documents importants relacionats amb la reunió.
        - Integració amb altres mòduls d'Odoo per millorar les funcionalitats.
        - Agenda interactiva per a una visualització clara de les reunions programades.
        - Vinculació amb altres tasques o projectes a Odoo.

        Aquest mòdul té com a objectiu millorar l'eficiència en la gestió del cicle de vida de les reunions, des de la planificació fins a la conclusió i documentació.
    """,

    'author': "My Company - Esteve Llobera",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Reunions',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/estate_property_reports.xml',
        'report/estate_property_templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
}


# -*- coding: utf-8 -*-
{
    'name': "Project Development",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "May Ghonimy",


    
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project','hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/task_sequence.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/employee_views.xml'
    ],

}


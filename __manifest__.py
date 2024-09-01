# -*- coding: utf-8 -*-
{
    'name': "Project Development",

    'summary': "Project Development",
    'description': """
    Module to track projects development progress and enhance the Project module in Odoo
    """,
    'author': "May Ghonimy",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['project','hr'],
    'data': [
        'security/ir.model.access.csv',
        'data/task_sequence.xml',
        'views/project_views.xml',
        'views/task_views.xml',
        'views/employee_views.xml',
        'report/project_report.xml',
    ],
}


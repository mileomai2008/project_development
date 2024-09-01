# -*- coding: utf-8 -*-
import json

from odoo import http
import logging

_logger = logging.getLogger(__name__)


class ProjectDevelopment(http.Controller):

    @http.route('/employee/projects', auth='user', type='json', method=['GET'])
    def employee_projects(self):
        """ API to get all employees and a list of their active projects"""
        _logger.info("***Searching for employees with projects***.")
        data = []

        records = http.request.env['hr.employee'].sudo().search([])
        for record in records:
            data.append({"employee": record.name,
                         "active_projects": [project.project_id.name for project in record.project_ids.filtered(lambda exp: exp.state == 'active')]
                         })
        _logger.info("***Data collected***.")
        return json.dumps(data)


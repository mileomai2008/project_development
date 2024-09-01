# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class HREmployee(models.Model):
    _inherit = "hr.employee"
    github_account = fields.Char("GitHub Account")
    project_ids = fields.One2many("project.employee", "employee_id", "Projects")
    project_count = fields.Integer(compute='_compute_project_count')

    def _compute_project_count(self):
        """To count the number of active projects for an employee"""
        for record in self:
            record.project_count = self.env["project.employee"].sudo().search_count([("employee_id", "=", record.id),
                                                                              ("state", "=", "active")])

    def write(self, vals):
        #To check if the active field is being set = False
        # and the project count is greater than zero raise an error
        for record in self:
            if "active" in vals and not vals.get("active") and record.project_count != 0.0:
                raise UserError(
                    _(
                        "You Cannot Archive An Employee While Whose Active On Project(s).\n"
                        "Please Deactivate Them From Project(s) First."
                    )
                )
        return super().write(vals)

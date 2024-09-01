# -*- coding: utf-8 -*-
from odoo import models, fields


class Project(models.Model):
    _inherit = "project.project"

    odoo_version = fields.Integer("Odoo Version")
    odoo_type = fields.Selection([("community", "Community"),
                                 ("enterprise", "Enterprise")], "Odoo Type")
    gitHub_repo_name = fields.Char("GitHub Repo. Name")
    gitHub_repo_url = fields.Char("GitHub Repo. URL")
    hosting = fields.Selection([("on_prem", "On Prem"),
                                ("cloud_hosting", "Cloud Hosting"),
                                ("odoo_sh", "Odoo SH"),
                                ("odoo_online", "Odoo Online")
                                ], "Hosting")
    hosting_description = fields.Text("Hosting Description")
    collaborator_ids = fields.One2many("project.employee", "project_id", "Collaborators")


class ProjectCollaborators(models.Model):
    _name = "project.employee"
    employee_id = fields.Many2one("hr.employee", "Employee")
    project_id = fields.Many2one("project.project", "Project")
    state = fields.Selection([
        ("active", "Active"),
        ('inactive', 'Inactive'),
    ], string='Status', copy=False, default="active")

    def make_active(self):
        """ Marks the Collaborator as Active"""
        for record in self:
            record.state = "active"

    def make_inactive(self):
        """ Marks the Collaborator as Inactive"""
        for record in self:
            record.state = "inactive"



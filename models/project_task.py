# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProjectTasK(models.Model):
    _inherit = "project.task"
    developer_id = fields.Many2one("hr.employee", "Developer")
    functional_consultant_id = fields.Many2one("hr.employee", "Functional Consultant")
    development_status = fields.Selection([("pending", "On Pending"),
                                           ("ongoing", "Ongoing"),
                                           ("delivered", "Delivered"),
                                           ("onhold", "Onhold"),
                                           ("cancelled", "Cancelled")
                                           ], "Development Status")
    module = fields.Char("Module")
    branch = fields.Char("Branch")
    release_notes = fields.Text("Release Notes")
    priority = fields.Selection(selection_add=[("1", "Medium"), ("2", "High")])
    internal_deadline = fields.Date("Internal Deadline")
    research_allocated_time = fields.Float("Research and Solution Design", default=0.00)
    develop_allocated_time = fields.Float("Development", default=0.00)
    test_allocated_time = fields.Float("Testing", default=0.00)
    task_allocated_time = fields.Float('Task Allocated Time', compute='_compute_task_duration')
    task_number = fields.Char("Task Number", default=lambda self: _('New'),
                              copy=False, readonly=True)

    @api.model
    def create(self, vals_list):
        """ Create a Sequence For Each Task """
        record = super().create(vals_list)
        record.task_number = self.env['ir.sequence'].next_by_code('task.sequence')
        return record

    def _compute_task_duration(self):
        """Compute Task Allocated Duration"""
        for record in self:
            record.task_allocated_time = (record.research_allocated_time +
                                          record.develop_allocated_time +
                                          record.test_allocated_time)




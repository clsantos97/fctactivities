# -*- coding: utf-8 -*-

from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class Activity(models.Model):
    _name = 'fctactivities.activity'

    name = fields.Char(string="Title", required=True)
    date = fields.Date(default=fields.Date.today)
    description = fields.Text()
    duration = fields.Float(digits=(6, 1), help="Duration in hours")
    remarks = fields.Text()
    owner = fields.Many2one('res.users', string="Pupil",default=lambda self: self.env.user,readonly=True)
#    owner = fields.Many2one('res.pupil', string="Pupil", default=lambda self: self.env.user, readonly=True)
#    owner = fields.Many2one('res.users', string="Pupil", default=lambda self: self.env.user, domain=[('isPupil', '=', True)], readonly=True)
    
    
    
    @api.constrains('duration')
    def _check_activity_duration(self):
        for r in self:
            if r.duration > 8:
                raise exceptions.ValidationError("Activity duration can't surpass 8 hours.")

# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'first_name'

    first_name = fields.Char(states={'draft': [('readonly', False)]}, readonly=True)
    last_name  = fields.Char(states={'draft': [('readonly', False)]}, readonly=True)
    father_name = fields.Char(states={'draft': [('readonly', False)]}, readonly=True)
    age = fields.Integer(states={'draft': [('readonly', False)]}, readonly=True)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')],
        states={'draft': [('readonly', False)]}, 
        readonly=True
    )
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('active', 'Active')],
        default='draft',
        states={'draft': [('readonly', False)]}, 
        readonly=True
    )

    @api.constrains('state')
    def check_state(self):
        for rec in self:
            if rec.age < 7 and rec.state == 'active':
                raise ValidationError("Not qualified")
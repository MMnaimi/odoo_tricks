# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name  = fields.Char()
    father_name = fields.Char()
    age = fields.Integer()
    active = fields.Boolean(default=True)
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')]
    )
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('active', 'Active')],
        default='draft'
    )
    teacher_id = fields.Many2one('teacher.teacher')

    @api.constrains('state')
    def check_state(self):
        for rec in self:
            if rec.age < 7 and rec.state == 'active':
                raise ValidationError("Not qualified")



class Teacher(models.Model):
    _name = 'teacher.teacher'
    _description = 'Teacher'
    _rec_name = 'first_name'

    first_name = fields.Char(required=True)
    last_name = fields.Char()
    age = fields.Integer()
    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        default='male'
    )
    student_id = fields.One2many('student.student', 'teacher_id')
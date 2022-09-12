# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# from lxml import etree
from datetime import date
class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'
    _rec_name = 'first_name'

    first_name = fields.Char()
    last_name  = fields.Char()
    father_name = fields.Char()
    dob = fields.Date(default=fields.Date.today)
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


    
    @api.onchange('dob')
    def _onchange_dob(self):
        today = date.today()
        if self.dob < today:
            self.age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
    
    @api.onchange('age')
    def _onchange_age(self):
        self.dob = date(date.today().year - self.age, self.dob.month,self.dob.day)

    @api.constrains('state')
    def check_state(self):
        for rec in self:
            if rec.age < 7 and rec.state == 'active':
                raise ValidationError("Not qualified")

    def action_varified(self):
        for rec in self:
            if rec.state != 'active' and rec.age > 7:
                rec.state = 'active'
                return {
                    'effect': {
                        'fadeout': 'slow',
                        'message': 'The student successfully varified!!!',
                        'img_url': 'odoo_tricks/static/img/bean.jpeg',
                        'type': 'rainbow_man'
                    }
                }
    # @api.model
    # def fields_view_get(self, view_id=None, view_type='form', toolbar=False, submenu=False):
    #     res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
    #     if view_type == 'form':
    #         doc = etree.XML(res.get('arch'))
    #         fields_teacher = doc.xpath("//field[@name='teacher_id']")
    #         if fields_teacher:
    #             fields_teacher[0].set('string', 'Student Teacher')
    #             print('>>>>>>>>>>>>>>>>>>>>', self.env.user)
    #         res['arch'] = etree.tostring(doc, encoding='unicode')
    #     return res

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
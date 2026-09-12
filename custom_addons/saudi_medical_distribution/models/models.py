# from odoo import models, fields, api


# class saudi_medical_distribution(models.Model):
#     _name = 'saudi_medical_distribution.saudi_medical_distribution'
#     _description = 'saudi_medical_distribution.saudi_medical_distribution'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


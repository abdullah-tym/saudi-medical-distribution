from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sfda_registration_no = fields.Char(string='SFDA Registration Number', tracking=True)
    is_cold_chain = fields.Boolean(string='Cold Chain Required', tracking=True)
    min_temperature = fields.Float(string='Min Temperature (°C)')
    max_temperature = fields.Float(string='Max Temperature (°C)')
    tracking = fields.Selection(selection_add=[('serial', 'By Unique Serial Number'), ('lot', 'By Lots')], ondelete={'serial': 'set default', 'lot': 'set default'})
    use_expiration_date = fields.Boolean(string='Expiration Date', default=True)

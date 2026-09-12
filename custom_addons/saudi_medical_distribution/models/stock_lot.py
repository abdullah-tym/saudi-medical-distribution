from odoo import models, fields

class StockLot(models.Model):
    _inherit = 'stock.lot'

    sfda_release_status = fields.Selection([
        ('pending', 'Pending SFDA Inspection'),
        ('approved', 'Approved for Distribution'),
        ('rejected', 'Rejected / Recalled')
    ], string='SFDA Release Status', default='pending', tracking=True, required=True)
    regulatory_certificate_no = fields.Char(string='Batch Certificate Reference', tracking=True)

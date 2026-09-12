from odoo import models, fields, api
from odoo.exceptions import UserError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    cold_chain_compliant = fields.Boolean(
        string='Cold Chain Verified',
        tracking=True
    )

    transit_temperature_recorded = fields.Float(
        string='Recorded Transit Temp (°C)',
        tracking=True
    )

    temperature_deviation_notes = fields.Text(
        string='Temperature Deviation Remarks'
    )

    @api.onchange('transit_temperature_recorded')
    def _onchange_transit_temperature(self):
        for picking in self:
            products = picking.move_ids.mapped('product_id')
            cold_products = products.filtered(
                lambda p: p.is_cold_chain
            )

            if not cold_products:
                picking.cold_chain_compliant = False
                continue

            min_t = min(cold_products.mapped('min_temperature'))
            max_t = max(cold_products.mapped('max_temperature'))

            picking.cold_chain_compliant = (
                min_t <= picking.transit_temperature_recorded <= max_t
            )

    def action_release_for_distribution(self):
        for picking in self:
            if not picking.cold_chain_compliant:
                raise UserError(
                    'Cannot release this shipment: '
                    'Cold Chain Verified is not satisfied.'
                )

            lots = picking.move_line_ids.mapped('lot_id')

            rejected_lots = lots.filtered(
                lambda lot: lot.sfda_release_status == 'rejected'
            )

            pending_lots = lots.filtered(
                lambda lot: lot.sfda_release_status != 'approved'
            )

            if rejected_lots:
                raise UserError(
                    'Cannot release this shipment: '
                    'one or more lots are rejected or recalled.'
                )

            if pending_lots:
                raise UserError(
                    'Cannot release this shipment: '
                    'all lots must be SFDA Approved.'
                )

        return True
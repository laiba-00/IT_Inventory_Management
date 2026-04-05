from odoo import models, fields


class ReorderWizard(models.TransientModel):
    _name = 'it.reorder.wizard'
    _description = 'IT Equipment Reorder Wizard'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    qty_to_order = fields.Float(string='Quantity to Order', default=1.0)
    partner_id = fields.Many2one('res.partner', string='Vendor')

    def action_create_purchase_order(self):
        self.ensure_one()
        purchase_order = self.env['purchase.order'].create({
            'partner_id': self.partner_id.id,
            'order_line': [(0, 0, {
                'product_id': self.product_id.id,
                'product_qty': self.qty_to_order,
                'price_unit': self.product_id.standard_price,
                'date_planned': fields.Datetime.now(),
                'product_uom': self.product_id.uom_po_id.id,
            })]
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Order',
            'res_model': 'purchase.order',
            'res_id': purchase_order.id,
            'view_mode': 'form',
            'target': 'current',
        }
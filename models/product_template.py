from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    it_device_type = fields.Selection([
        ('cctv', 'CCTV Camera'),
        ('access_point', 'Access Point'),
        ('network_switch', 'Network Switch'),
        ('router', 'Router'),
        ('other', 'Other'),
    ], string='Device Type')

    it_serial_number = fields.Char(string='Serial Number')
    it_warranty_date = fields.Date(string='Warranty Expiry Date')
    it_device_location = fields.Char(string='Device Location / Department')
    it_min_qty = fields.Float(string='Minimum Stock Quantity', default=0.0)

    it_low_stock_alert = fields.Boolean(
        string='Low Stock',
        compute='_compute_low_stock_alert',
        store=False
    )

    @api.depends('qty_available', 'it_min_qty')
    def _compute_low_stock_alert(self):
        for record in self:
            record.it_low_stock_alert = (
                record.it_min_qty > 0 and
                record.qty_available < record.it_min_qty
            )
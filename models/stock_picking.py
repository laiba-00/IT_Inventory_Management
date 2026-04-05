from odoo import models, fields


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Stock IN fields
    it_received_by = fields.Char(string='Received By')
    it_purchase_reference = fields.Char(string='Purchase Reference / Invoice No')

    # Stock OUT fields
    it_department = fields.Char(string='Issued To (Department)')
    it_issued_by = fields.Char(string='Issued By')
    it_purpose = fields.Selection([
        ('installation', 'Installation'),
        ('replacement', 'Replacement'),
        ('repair', 'Repair'),
        ('new_setup', 'New Setup'),
        ('other', 'Other'),
    ], string='Purpose')

    # Common
    it_remarks = fields.Text(string='Remarks')
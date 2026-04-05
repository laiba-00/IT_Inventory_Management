from odoo import models, fields, api
from odoo.http import request


class ItInventoryPortal(models.Model):
    _inherit = 'portal.mixin'
    _inherit = 'product.template'
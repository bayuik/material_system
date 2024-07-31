from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MaterialSystem(models.Model):
    _name = 'material.system'
    _description = 'Material System'

    name = fields.Char(string='Material Name', required=True)
    code = fields.Char(string='Material Code', required=True)
    material_type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton'),
    ], string='Material Type', required=True)
    res_partner_id = fields.Many2one('res.partner', string='Supplier', required=True)
    price_unit = fields.Float(string='Price Unit', required=True)

    @api.constrains('price_unit')
    def _check_material_buy_price(self):
        for record in self:
            if record.price_unit < 100:
                raise ValidationError('Material buy price cannot be less than 100')

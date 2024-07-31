from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError


class TestMaterialSystem(TransactionCase):

    def setUp(self):
        super(TestMaterialSystem, self).setUp()
        self.material_system = self.env['material.system']
        self.partner = self.env['res.partner'].create({
            'name': 'Test Supplier'
        })

    def test_create_material(self):
        material = self.material_system.create({
            'name': 'Test Material',
            'code': 'TM001',
            'material_type': 'fabric',
            'res_partner_id': self.partner.id,
            'price_unit': 150,
        })
        self.assertEqual(material.name, 'Test Material')

    def test_create_material_with_low_price(self):
        with self.assertRaises(ValidationError):
            self.material_system.create({
                'name': 'Test Material',
                'code': 'TM001',
                'material_type': 'fabric',
                'res_partner_id': self.partner.id,
                'price_unit': 50,
            })

    def test_update_material(self):
        material = self.material_system.create({
            'name': 'Test Material',
            'code': 'TM001',
            'material_type': 'fabric',
            'res_partner_id': self.partner.id,
            'price_unit': 150,
        })
        material.write({'price_unit': 200})
        self.assertEqual(material.price_unit, 200)

    def test_delete_material(self):
        material = self.material_system.create({
            'name': 'Test Material',
            'code': 'TM001',
            'material_type': 'fabric',
            'res_partner_id': self.partner.id,
            'price_unit': 150,
        })
        material_id = material.id
        material.unlink()
        material = self.material_system.search([('id', '=', material_id)])
        self.assertFalse(material)

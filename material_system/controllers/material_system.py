from odoo import http
from odoo.http import request, Response
import json


class MaterialSystemController(http.Controller):

    @http.route('/material_system/materials', type='json', auth='user')
    def get_materials(self):
        materials = request.env['material.system'].search([])
        data = []
        for material in materials:
            data.append({
                'name': material.name,
                'code': material.code,
                'material_type': material.material_type,
                'price_unit': material.price_unit,
                'supplier': material.res_partner_id.name
            })
        return data

    @http.route('/material_system/material', type='json', auth='user', methods=['POST'])
    def create_material(self, **kwargs):
        required_fields = ['name', 'code', 'material_type', 'price_unit', 'res_partner_id']
        for field in required_fields:
            if field not in kwargs:
                return Response(
                    json.dumps({'error': 'Missing required field: %s' % field}),
                    status=400,
                    content_type='application/json'
                )

        if kwargs['price_unit'] < 100:
            return Response(
                json.dumps({'error': 'Material buy price cannot be less than 100'}),
                status=400,
                content_type='application/json'
            )

        material = request.env['material.system'].create(kwargs)
        return material.read()[0]

    @http.route('/material_system/material/<int:material_id>', type='json', auth='user', methods=['PUT'])
    def update_material(self, material_id, **kwargs):
        material = request.env['material.system'].browse(material_id)
        if not material:
            return Response(
                json.dumps({'error': 'Material not found'}),
                status=404,
                content_type='application/json'
            )

        material.write(kwargs)
        return material.read()[0]

    @http.route('/material_system/material/<int:material_id>', type='json', auth='user', methods=['DELETE'])
    def delete_material(self, material_id):
        material = request.env['material.system'].browse(material_id)
        if not material:
            return Response(
                json.dumps({'error': 'Material not found'}),
                status=404,
                content_type='application/json'
            )

        material.unlink()
        return {'success': True}

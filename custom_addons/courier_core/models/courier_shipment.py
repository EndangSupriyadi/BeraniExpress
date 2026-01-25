from odoo import models, fields


class CourierShipment(models.Model):
    _name = 'courier.shipment'
    _description = 'Courier Shipment'

    name = fields.Char(
        string='No. Resi',
        required=True
    )
    customer_id = fields.Many2one(
        comodel_name='courier.customer',
        string='Pelanggan'
    )
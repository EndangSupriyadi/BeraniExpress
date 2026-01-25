from odoo import models, fields


class CourierCustomer(models.Model):
    _name = 'courier.customer'
    _description = 'Courier Customer'

    name = fields.Char(
        string='Nama Pelanggan',
        required=True
    )
    email = fields.Char(
        string='Email'
    )
    phone = fields.Char(
        string='Nomor Telepon'
    )
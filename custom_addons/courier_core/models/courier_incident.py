from odoo import models, fields
from odoo.exceptions import ValidationError


# Model untuk mencatat insiden yang terjadi pada pelanggan atau pengiriman
class CourierIncident(models.Model):
    # Definisi model CourierIncident
    _name = 'courier.incident'
    _description = 'Courier Incident'

    # Fields untuk model CourierIncident
    name = fields.Char(
        string='Judul Insiden',
        required=True
    )
    customer_id = fields.Many2one(
        comodel_name='courier.customer',
        string='Pelanggan',
        required=True
    )
    shipment_id = fields.Many2one(
        comodel_name='courier.shipment',
        string='No. Resi'
    )
    incident_type = fields.Selection(
        selection=[
            ('health', 'Health'),
            ('lost_item', 'Lost Item'),
            ('delay', 'Delay'),
            ('other', 'Other')
        ],
        string='Tipe',
        default='other'
    )
    incident_datetime = fields.Datetime(
        string='Waktu',
        required=True,
        default=fields.Datetime.now
    )
    severity = fields.Selection(
        selection=[
            ('low', 'Low'),
            ('medium', 'Medium'),
            ('high', 'High')
        ],
        string='Urgensi',
        default='low'
    )
    description = fields.Text(
        string='Kronologi'
    )
    followup_note = fields.Text(
        string='Catatan'
    )
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('followup', 'Follow Up'),
            ('done', 'Done')
        ],
        string='Status',
        default='draft'
    )
    resolved_at = fields.Datetime(
        string='Selesai pada',
        readonly=True
    )

    #sql constraints
    _sql_constraints = [
        (
            'unique_customer_incident',
            'unique(customer_id, incident_datetime, incident_type)',
            'Insiden dengan tipe yang sama untuk pelanggan yang sama pada waktu yang sama sudah ada.'

    )]
    # Python validations
    @api.constrains('state', 'followup_note')
    def _check_followup_note(self):
        for record in self:
            if record.state == 'done' and not record.followup_note:
                raise ValidationError("Catatan Follow Up wajib diisi sebelum menandai insiden sebagai Done.")

    # Methods untuk mengubah state insiden
    def action_followup(self):
        """Ubah state menjadi followup"""
        self.write({
            'state': 'followup'
        })

    def action_done(self):
        """Ubah state menjadi done dan isi resolved_at"""
        self.write({
            'state': 'done',
            'resolved_at': fields.Datetime.now()
        })
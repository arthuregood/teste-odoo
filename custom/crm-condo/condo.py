from odoo import models, fields

class ExtendLeadCondo(models.Model):
  _inherit = 'crm.lead'

  condo_units = fields.Integer('Units')
  condo_blocks = fields.Integer('Blocks')
  condo_residents = fields.Integer('Residents')
  condo_type = fields.Selection([ ('proprietary', 'Proprietary'),('third_party', 'Third Party')])
  condo_schedule = fields.Selection([ ('24h', '24 hours'),('12h', '12 hours')])

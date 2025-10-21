from odoo import fields, models


class ResCompany(models.Model):
    """
    To inherit res company model.
    """
    _inherit = 'res.company'

    background_image = fields.Binary(string="Background Image", attachment=True)

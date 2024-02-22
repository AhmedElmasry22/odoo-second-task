from odoo import api,fields,models
class SequenceModel(models.TransientModel):
    _name="letters.sequence.configuration"
    _description = 'Sequence Configuration'
    _rec_name = 'prefix'

    prefix = fields.Char(string="Prefix")

    @api.model
    def create(self,vals):

        sequence=self.env['ir.sequence'].browse(23)
        sequence.write({
             'prefix':vals['prefix']
         })

        return super(SequenceModel, self).create(vals)









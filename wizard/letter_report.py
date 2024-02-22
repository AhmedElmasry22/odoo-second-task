from odoo import api,fields,models
class LetterReportWizard(models.TransientModel):
    _name="letter.guarantee.wizard"
    _description="Search for Letters With Wizard"
    date_from=fields.Date(string="Release Date From")
    date_to=fields.Date(string="Release Date To")
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    bank_account = fields.Many2one('res.bank', string="Bank")

    def action_print_report(self):
        print(self.responsible_id)
        domain=[]
        if self.date_from:
            domain += [('release_data', '>=', self.date_from)]
        if self.date_to:
            domain+= [('release_data','<=',self.date_to)]

        if self.responsible_id:
            domain += [('responsible_id', '=', self.responsible_id.id)]

        if self.bank_account:
            domain += [('bank_account', '=', self.bank_account.id)]

        letters=self.env['letters.guarantee'].search_read(domain)
        data = {
            'form_data' : self.read()[0],


            'letters': letters
        }

        return self.env.ref('letters_guarantee.letter_report_wizard_act').report_action(self,data=data)

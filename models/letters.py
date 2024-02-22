from odoo import models, fields, api ,exceptions
from datetime import datetime

class Letters(models.Model):
     _name = 'letters.guarantee'
     _description = 'Letters Of Guarantee'
     _rec_name='ref'

     ref=fields.Char(default='New', readonly=True)
     number_phone=fields.Char(string="Phone Number")
     responsible_id = fields.Many2one('res.partner', ondelete='set null', string="Responsible", index=True)
     number_Letter = fields.Integer(string="Letter No")

     state= fields.Selection([('DRAFT','DRAFT'),('CONFIRMED','CONFIRMED'),('POSTED','POSTED'),('RETURNED','RETURNED'),('CANCELED','CANCELED')],default="DRAFT")
     letter_type= fields.Selection([('Primary','Primary'),('Ultimate','Ultimate'),('Advance Payment','Advance Payment')],string="Type of Litter")
     bank_account= fields.Many2one('res.bank',ondelete='set null', string="Bank",index=True)
     amount = fields.Float(string="Amount")
     merge_percent = fields.Float(string="Merge Percent")
     merge_amount = fields.Float(string="Merge Amount",readonly=False,compute='_compute_merge_amount' ,inverse='_inverse_compute')
     release_data = fields.Date(default=fields.Date.today,string="Release Data")
     expiry_data = fields.Date(default=fields.Date.today,string="Expiry Data")
     expiry_status = fields.Text(default="Running")

     number_edit=fields.Integer(default=0)

     renewal_data1 = fields.Date(string="Renewal Data 1")
     renewal_data2 = fields.Date(string="Renewal Data 2")
     renewal_data3 = fields.Date(string="Renewal Data 3")
     renewal_data4 = fields.Date(string="Renewal Data 4")




     def write(self, vals):

          if('renewal_data1'  in vals or 'renewal_data2' in vals or 'renewal_data3' in vals or 'renewal_data4' in vals  ):
               values = self.env['letters.guarantee'].browse(self._origin.id)
               vals['number_edit'] = values['number_edit'] + 1
               print(vals['number_edit'])
               if (vals['number_edit'] == 2):
                    nameNewExpireDate = 'renewal_data1'
               elif (vals['number_edit'] == 3):
                    nameNewExpireDate = "renewal_data2"
               elif (vals['number_edit'] == 4):
                    nameNewExpireDate = "renewal_data3"
               else:
                    nameNewExpireDate = "renewal_data4"
               if (datetime.strptime(vals[nameNewExpireDate], "%Y-%m-%d").date() < values['release_data']):
                    raise exceptions.ValidationError(f"A {nameNewExpireDate} Cant be  less than Release Date ")

               if (datetime.strptime(vals[nameNewExpireDate], "%Y-%m-%d").date() > values['release_data']):
                    vals['expiry_status'] = "Running"
               else:
                    vals['expiry_status'] = "Finishing"



          res = super(Letters, self).write(vals)
          return res


     @api.model
     def create(self,vals):
          if (vals['expiry_data'] > vals['release_data']):
               vals['expiry_status'] = "Runnining"

          else:
               vals['expiry_status'] = "Finishing"
          vals['number_edit']=1
          vals['ref']=self.env['ir.sequence'].next_by_code('property_seq')
          return super(Letters, self).create(vals)

     @api.depends('amount','merge_percent')
     def _compute_merge_amount(self):
          for i in self:
               if i.merge_percent !=0:
                    i.merge_amount = i.amount / i.merge_percent

     @api.depends('amount', 'merge_percent')
     def _compute_merge_amount(self):
          for i in self:
               if i.merge_percent != 0:
                    i.merge_amount = i.amount / i.merge_percent
     @api.depends('merge_amount')
     def _inverse_compute(self):
          for rec in self:
               rec.amount=rec.merge_percent*rec.merge_amount









     def action_posted(self):
          self.state = 'POSTED'
     def action_draft(self):
          self.state = 'DRAFT'
     def action_confirmed(self):
          self.state = 'CONFIRMED'
     def action_returned(self):
          self.state = "RETURNED"
     def action_cancel(self):
          self.state = "CANCELED"

     def action_automation_statues(self):
         letters_ids=self.search([])
         for rec in letters_ids:
              if rec.number_edit==1 and rec.expiry_data <=fields.date.today() and rec.expiry_status != "Finishing" :
                   rec.expiry_status = "Finishing"
              elif rec.number_edit==2 and rec.renewal_data1 <=fields.date.today() and rec.expiry_status != "Finishing":
                   rec.expiry_status = "Finishing"
              elif rec.number_edit==3 and rec.renewal_data2 <=fields.date.today() and rec.expiry_status != "Finishing":
                   rec.expiry_status = "Finishing"
              elif rec.number_edit==4 and rec.renewal_data3 <=fields.date.today() and rec.expiry_status != "Finishing":
                   rec.expiry_status = "Finishing"
              elif rec.number_edit==5 and rec.renewal_data4 <=fields.date.today() and rec.expiry_status != "Finishing":
                   rec.expiry_status = "Finishing"

     def action_print_report(self):
          action = self.env["ir.actions.actions"]._for_xml_id("letters_guarantee.action_report_letter")



          return action






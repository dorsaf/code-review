
from odoo import models, fields


class Slides(models.Model):
    _inherit = 'slide.slide'

    def _compute_slide_channel_count(self):
        read_group_res = self.env['slide.channel.partner'].sudo().read_group(
            [('partner_id', 'in', self.ids)],
            ['partner_id'], 'partner_id'
        )
        data = dict((res['partner_id'][0], res['partner_id_count']) for res in read_group_res)
        for partner in self:
            partner.slide_channel_count = data.get(partner.id, 0)



     def _compute_slide_channel_company_count(self):
            for partner in self:
                if partner.is_company:
                    partner.slide_channel_company_count = self.env['slide.channel'].sudo().search_count(
                        [('partner_ids', 'in', partner.child_ids.ids)]
                    )
                else:
                    partner.slide_channel_company_count = 0

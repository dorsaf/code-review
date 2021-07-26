    def _compute_slide_channel_count(self):
        read_group_res = self.env['slide.channel.partner'].sudo().read_group(
            [('partner_id', 'in', self.ids)],
            ['partner_id'], 'partner_id'
        )
        data = dict((res['partner_id'][0], res['partner_id_count']) for res in read_group_res)
        for partner in self:
            partner.slide_channel_count = data.get(partner.id, 0)
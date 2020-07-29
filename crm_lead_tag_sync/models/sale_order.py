# Copyright 2020 Iván Todorovich <ivan.todorovich@gmail.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('tag_ids')
    def _sync_tag_ids(self):
        """ Synchronizes tag_ids to the opportunity. """
        for rec in self:
            if not rec.opportunity_id:
                continue
            if rec.opportunity_id.tag_ids != rec.tag_ids:
                rec.opportunity_id.tag_ids = rec.tag_ids

    @api.constrains('opportunity_id')
    def _sync_opportunity_tag_ids(self):
        """ Resets tag_ids from the related opportunity, if changed. """
        for rec in self:
            if not rec.opportunity_id:
                continue
            if rec.opportunity_id.tag_ids != rec.tag_ids:
                rec.tag_ids = rec.opportunity_id.tag_ids

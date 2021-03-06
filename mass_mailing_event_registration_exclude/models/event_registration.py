# Copyright 2016 Tenativa - Antonio Espinosa
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, models
from .mail_mass_mailing import event_filtered_ids


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    @api.model
    def search_count(self, domain):
        res = super().search_count(domain)
        mass_mailing_id = self.env.context.get('exclude_mass_mailing', False)
        if mass_mailing_id:
            res_ids = event_filtered_ids(
                self, mass_mailing_id, domain, field='email')
            res = len(res_ids) if res_ids else 0
        return res

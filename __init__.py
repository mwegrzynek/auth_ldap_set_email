# -*- encoding: UTF-8 -*-

from openerp import api
from openerp.models import Model


class CompanyLDAP(Model):
    _name = 'res.company.ldap'
    _inherit = 'res.company.ldap'

    @api.model
    def map_ldap_attributes(self, conf, login, ldap_entry):
        values = super(CompanyLDAP, self).map_ldap_attributes(conf, login, ldap_entry)
        
        # Set e-mail and signature
        attrs = ldap_entry[1]
        
        values['email'] = attrs['mail'][0]   
        values['signature'] = '--<br>{0}<br>{1}'.format(
            attrs['cn'][0],
            attrs['description'][0]
        )
        
        return values
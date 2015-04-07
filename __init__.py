# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Management Solution
#    Copyright (C) 2005-Today Litex Service Sp. z o.o. 
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
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
        
        email = attrs.get('mail', [''])[0]
        description = attrs.get('description', [''])[0] 
        
        if email:
            values['email'] = email
            
           
        values['signature'] = '--<br>{0}{1}'.format(
            attrs['cn'][0],
            ('<br>' + description) if description else ''
        )
        
        return values
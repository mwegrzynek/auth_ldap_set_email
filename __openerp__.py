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
{
    'name': 'Set e-mail and signature for users autocreated by auth_ldap',

    'summary': '''Small extension module for correctly setting new user's email and signature based on data from LDAP directory''',
    'description': '''
        Small extension module for correctly setting new user's email and signature based on data from LDAP directory.
    ''',
    'author': 'Litex Service Sp. z o.o.',
    'website': 'http://www.litex.pl',
    'category': 'Authentication',
    'version': '1.0.1',
    'depends': [
        'auth_ldap'
    ],
    'data': [],
    'demo': [],
    'tests': [],
}

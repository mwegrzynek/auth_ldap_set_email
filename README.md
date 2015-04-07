#Set e-mail and signature for users autocreated by auth_ldap

Users created by auth_ldap get e-mail and signature from the selected template.
This module gets this data from the LDAP directory and sets:

  - user's e-mail to LDAP `mail` attribute
  - user's signature to
    ```
    
    --
    <full name>
    <description>
    ``` 
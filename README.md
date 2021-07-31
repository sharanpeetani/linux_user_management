# Linux User Management using Ansible Engine

# Linux User Management Presentation slides:
    - Slides: Linux User Management using Ansible.pptx
    
# Use Cases:

    1) Create users with CSV file
         - create user: playbooks/linux_user_mgmt_csv/create_user_csv.yml

    2) Create users with vars file
         - create user: playbooks/linux_user_mgmt_vars/create_user_vars.yml

    3) Create users using vault file
         - create user: playbooks/linux_user_mgmt_vault/create_user_vault.yml

    4) User management:
         - create user: playbooks/linux_user_mgmt/create_account.yml
         - Set/Change user password: playbooks/linux_user_mgmt/change_passwd.yml
         - lock user: playbooks/linux_user_mgmt/manage_account.yml [ account_action = lock ]
         - unlock user: playbooks/linux_user_mgmt/manage_account.yml [ account_action = unlock ]
         - revoke user: playbooks/linux_user_mgmt/manage_account.yml [ account_action = revoke ]

     5) User Management temp password:
          - create user with temp pd: playbooks/linux_user_mgmt_pd_gen/create_user_1.yml

     6) Create User:
          - playbook with module options example: playbooks/linux_user_mgmt_module/create_user_mod.yml

# Execute playbooks:

     $ ansible-playbook <path/of/playbook>.yml

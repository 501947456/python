playbooks/ansible.cfg
playbooks/hosts
playbooks/web-notls.yml
playbooks/web-tls.yml
playbooks/files/nginx.key
playbooks/files/nginx.crt
playbooks/files/nginx.conf
playbooks/templates/index.html.j2
playbooks/templates/nginx.conf.j2

testserver ansible_ssh_host=ec2-120 ansible_ssh_user=ubtun ansible_ssh_private_key_file=/path/to/keyfile.pem
ansible testserver -i hosts -m ping









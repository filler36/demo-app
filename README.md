# Feel The Notes 
![example workflow](https://github.com/filler36/demo-app/actions/workflows/dev_workflow.yml/badge.svg)


## Prerequisites
#### Docker:
- Install docker on server
- Add user to docker group: ***sudo usermod -aG docker ${USER}***
- relogin

#### Oracle Cloud
- Create Oracle Cloud Instance (Ubuntu)
- Install firewalld on server: ***sudo apt install firewalld***
- sudo firewall-cmd --zone=public --permanent --add-port=<port of the app>/tcp
- sudo firewall-cmd --reload
- Go to Networking -> Virtual Cloud Network -> Security Lists -> Choose Your Security List.
Change Ingress rule "ICMP traffic for: All" from localhost to 0.0.0.0/0
Add Ingress rule (Source CIDR: 0.0.0.0/0, IP Protocol: TCP, Destination Port Range: 8000)



## List of technologies
- Python
- Django
- Docker
- Docker compose
- Docker Hub
- GitHub
- GitHub Actions
- Oracle Cloud
- ?Telegram API
- ?HTML
- ?JS
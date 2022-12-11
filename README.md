# Aline Data Generation

## Usage
This Python package was developed to generate data to persist in a MySql database for testing our implementation of the Aline Financial Application. As such, these were meant to be configired and used by software engineers.

The Applicants generator leverages the Underwriter microservice. It requires initial configuration in the config.py file where methods can be set to run or not run and method values are also set.  

## Installation

# Requirements:
Docker Desktop
[VS Code](https://code.visualstudio.com)
    -[Docker extension](https://code.visualstudio.com/docs/containers/overview)

1. In a single folder, clone all Aline Financial repositories
[Aline Financial](https://git1.smoothstack.com/cohorts/2022/organizations/cyber-cumulus/lynda-foster) application repositories.

2. Initialize and merge submodules.

In aline-user-microservice and aline-underwriter-microservice run:
`git submodule deinit -f .`
`git submodule update --init --remote --merge`

3. Run microservices:

Right-click docker-compose.yml and select "Compose Up - Select Service" from menu. 

Check boxes for the following options:
`mysql`
`underwriter`
`user`

Click OK

4. Set up testing scripts:

In the devops-data-generato folder, modify config.py in your IDE or other text editor to verify which methods and variables are required to accomplish the tests needed. 

5. Run testing scripts:

Run main.py

In command line:  
`python main.py` or `python3 main.py`

## Support
lynda.foster@smoothstack.com<br>
[Cyber Cumulus Jira](https://cyber-cumulus-smoothstack.atlassian.net/jira/software/projects/CC/boards/1)

## Roadmap
- [ ] [Data Generation](https://git1.smoothstack.com/cohorts/2022/organizations/cyber-cumulus/lynda-foster/aline-data-generation)
    - [ ] User Data Producer
    - [ ] Banks and Branches
    - [x] Applicants
    - [ ] Applications
    - [ ] Transaction Data Producer
- [ ] Docker CI/CD
    - [ ] Dockerize Images
    - [ ] Docker Compose Local
    - [ ] Docker Compose Cloud
- [ ] Kubernetes CI/CD
    - [ ] Kubernetes Pod Local
    - [ ] Kubernetes Cloud EKS
- [ ] Terraform CI/CD
    - [ ] Create Base Infrastructure
- [ ] Jenkins CI/CD
    - [ ] Jenkins Pipelines
    - [ ] Jenkins Integration with Sonarqube
    - [ ] Docker Compose Jenkins
    - [ ] Kubernetes via Jenkins
    - [ ] Terraform Plan and Apply via Jenkins
- [ ] General CI/CD
    - [ ] Ansible Playbooks
    - [ ] Vanilla CloudFormation

## Acknowledgements
Developed by:

[Lynda Foster](https://git1.smoothstack.com/lynda.foster)

With support from the Cyber Cumulus Team:

[Anthony Foster](https://git1.smoothstack.com/anthony.foster)<br>
[Dennis Ghitas](https://git1.smoothstack.com/dennis.ghitas)<br>
[Sebastian Marzal](https://git1.smoothstack.com/sebastian.marzal)

## License
[MIT License](LICENSE.md)

## Project status
This project is in early development. 

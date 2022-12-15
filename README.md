# Aline Data Generation

## Usage
This Python package was developed to generate data to persist in a MySql database for testing our implementation of the Aline Financial app. These scripts were meant to be used by software engineers that need to smoke test the microservices.

The Applicants generator leverages the Underwriter microservice. It requires structuring in the `config.py` file (located in the `program` directory) where methods can be set to run or not run and method values are also set.

## Installation

# Requirements:
Docker Desktop

[VS Code](https://code.visualstudio.com)

[Docker extension](https://code.visualstudio.com/docs/containers/overview)

1. In a single folder, clone all [Aline Financial](https://git1.smoothstack.com/cohorts/2022/organizations/cyber-cumulus/lynda-foster) application repositories.

2. Initialize and merge submodules.

CD into the `aline-user-microservice` and `aline-underwriter-microservice` folders and run:

`git submodule deinit -f .`

`git submodule update --init --remote --merge`

3. Run microservices:

Right-click `docker-compose.yml` and select `Compose Up - Select Service` from menu. 

Check boxes for the following options:

`mysql`

`underwriter`

`user`

Click `OK`

4. Create a python environment, activate environment, and install requirements. 

`pip intstall -r requirements.txt`

5. Set up testing scripts:

In the `program` folder, modify `config.py` in your VS Code or other IDE to verify which methods and variables are required to accomplish the tests needed. 

6. Run `main.py`:

`python main.py` or `python3 main.py`

## Support
lynda.foster@smoothstack.com<br>
[Cyber Cumulus Jira](https://cyber-cumulus-smoothstack.atlassian.net/jira/software/projects/CC/boards/1)

## Roadmap
- [ ] [Data Generation](https://git1.smoothstack.com/cohorts/2022/organizations/cyber-cumulus/lynda-foster/devops-data-generator/-/branches)
    - [x] Applicants
    - [x] Applications
    - [x] User Data Producer
    - [x] Banks and Branches
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
Lead Developer:

[Lynda Foster](https://git1.smoothstack.com/lynda.foster)

With support from the Cyber Cumulus Team:

[Anthony Foster](https://git1.smoothstack.com/anthony.foster)<br>
[Dennis Ghitas](https://git1.smoothstack.com/dennis.ghitas)<br>
[Sebastian Marzal](https://git1.smoothstack.com/sebastian.marzal)

## License
[MIT License](LICENSE.md)

## Project status
This project is in early development. 

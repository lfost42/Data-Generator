# Aline Data Generation

## Usage
This Python package are smoke tests that generate data to persist in a MySql database. Smoke tests verify that the most important functionality in our application is working. They are a cost-effective method for identifying and fixing defects in software.

The data generators leverage the Underwriter, User, and Bank microservice. It requires structuring in the config.py file (located in the program directory) where methods can be set to run or not run and method values are also set.

![logo](diagram.png)

## Installation

### Install Requirements:

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. [VS Code](https://code.visualstudio.com)

### Set up Docker Images for the Aline Financial application:

1. Clone the [Smoke Test Data Generator](https://git1.smoothstack.com/cohorts/2022/organizations/cyber-cumulus/lynda-foster/devops-data-generator/-/tree/develop) repo. 

2. Pull docker hub images:
```
docker pull lyndasm/aline:mysql
docker pull lyndsm/aline:aline-gateway
docker pull lyndasm/aline:aline-underwriter
docker pull lyndasm/aline:aline-user
docker pull lyndasm/aline:aline-bank
```

3. Run microservices:

`docker compose -f "docker-compose.yml" up -d --build`

4. Create a python environment, activate environment, and install requirements. 

`pip intstall -r requirements.txt`

5. Set up testing scripts:

In the `main` folder, modify `config.py` in your VS Code or other IDE to verify which methods and variables are required for this test. 

6. Run `main`:

`py main` or `python3 main`

## Support
lynda.foster@smoothstack.com<br>
[Cyber Cumulus Jira](https://cyber-cumulus-smoothstack.atlassian.net/jira/software/projects/CC/boards/1)

## Roadmap
- [x] Data Generation=
    - [x] Applicants
    - [x] Applications
    - [x] User Data Producer
    - [x] Banks and Branches - in progress

## Acknowledgements
Lead Developer:

[Lynda Foster](https://git1.smoothstack.com/lynda.foster)

With support from the Cyber Cumulus Team:

[Anthony Foster](https://git1.smoothstack.com/anthony.foster)<br>
[Nathan Galler](https://git1.smoothstack.com/nathan.galler)<br>
[Dennis Ghitas](https://git1.smoothstack.com/dennis.ghitas)<br>
[Sebastian Marzal](https://git1.smoothstack.com/sebastian.marzal)

## License
[MIT License](LICENSE.md)

## Project status
This portion of the project is completing development. 
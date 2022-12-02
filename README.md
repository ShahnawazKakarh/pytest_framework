# pytest_framework
All settings are setup in this project for a beginer to learn pytest.

# Pytest Project Setup

Before running the app assuming that **python 3.7.9** , **mysql** and [virutalenv](http://python-guide-pt-br.readthedocs.io/en/latest/dev/virtualenvs/) is installed on machine

1. Create virtual environment with python3
```shell
$ virtualenv -p python3 envname
```
2. Activate the virtual environment
```shell
$ source envname/bin/activate
```
3. Install requisite packages:
```shell
$ sh scripts/install_requirements.sh
```

4. Temporary running solution:
- Run all tests under a project
```shell
$ pytest tests/{project_name}/ -vv --settings=settings.{deployment_details}
```
Where:
{project_name} = project_one, project_two, project_three & 
{deployment_details} = local, dev, qa, uat, rc, prd

- Run single tests under a project
```shell
$ pytest tests/{project_name}/test_file_name.py -vv -k 'test_name' --settings=settings.{deployment_details}
```

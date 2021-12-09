# Local Setup - teste-odoo


## Requirements

Use requirements script to install general requirements, pipenv for enviroment requirements and setup.py for odoo config
```
$ sudo sh requirements.sh
$ pipenv install
$ pipenv shell
$ cd odoo-12.0/
$ python3 setup.py install
```

## Postgree Database

```
$ createbd odootest
$ createuser odoouser
$ psql -U odoouser -d odootest
$ alter user odoouser with encrypted password 'root';
$ grant all privileges on database odootest to odoouser;
```


## First use

```
$ pipenv run odoo -c odoo.conf -i base
```

## Everyday use

```
pipenv run odoo -c odoo.conf
```

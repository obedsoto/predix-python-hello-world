# predix-python-hello-world
Predix hello world with python

**Project files:**

`hello-world.py`

A minimal Flask application externally visible.

`manifest.yml`

Manifest file to tell Cloud Foundry how to push and deploy our application.

`Procfile`

This file tells Cloud Foundry how to run your application or how to configure the application server, if a simple command is necessary to run your application, this can be passed through -c or in the manifest file.

`requirements.txt`

Application dependencies to be installed to run the application, for this only Flask is required. Everything is installed with pip (install -r requirements.txt).

`runtime.txt`

This file is used to indicate the python version required (i.e. python-3.5.0)

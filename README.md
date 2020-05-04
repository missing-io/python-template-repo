# Python Template

This repository is a Python template to create new applications.

[The porpouse of this project is to use MVC design pattern](https://www.geeksforgeeks.org/mvc-design-pattern/)

## Usage

```
$ ./python-template.py
```

## Description
> The default application port is 5000

## Structure

```
src
├── __init__.py
├── app.py
├── controller
│   ├── README.md
│   ├── __init__.py
│   └── example_controller.py
├── flask_config.py
└── service
    ├── README.md
    ├── __init__.py
    └── example_service.py
```

**Controller** - Application routes where you user service functions.

**Services** - Business rules for the application.

## TODO

> Create cookiecutter template for the other applications (Including the file names)
> Create CodeDeploy pipeline for deploying based on ECR image
> Improve README of how to use this repository

## License

Copyright © 2019 missing-io. All rights reserved.

# Django Skeleton Project

```bash
root
├── apps
│   ├── core
│   │   ├── apps.py
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── urls.py
│   ├── example_api
│   │   ├── api
│   │   │   ├── __init__.py
│   │   │   ├── v1
│   │   │   │   ├── __init__.py
│   │   │   │   ├── serializers.py
│   │   │   │   ├── services.py
│   │   │   │   ├── tests.py
│   │   │   │   ├── urls.py
│   │   │   │   └── views.py
│   │   │   └── v2
│   │   │       ├── __init__.py
│   │   │       ├── serializers.py
│   │   │       ├── services.py
│   │   │       ├── tests.py
│   │   │       ├── urls.py
│   │   │       └── views.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── management
│   │   │   ├── commands
│   │   │   │   ├── command.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── utils.py
│   └── __init__.py
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings
│   │   ├── base.py
│   │   ├── __init__.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── db
├── deployments
│   ├── dev
│   │   └── Dockerfile
│   ├── docker-compose.yaml
│   └── prod
├── docs
│   ├── CHANGELOG.md
│   ├── CONTRIBUTING.md
│   ├── deployment.md
│   ├── local-development.md
│   └── swagger.yaml
├── entrypoint.sh
├── manage.py
├── media
├── pyproject.toml
├── pytest.ini
├── README.md
├── requirements
│   ├── base.txt
│   ├── development.txt
│   ├── local.txt
│   └── production.txt
└── static
```
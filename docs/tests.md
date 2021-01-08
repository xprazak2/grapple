# How to test

1. Install dependencies. It is good to work inside virtual environment:

```
# Python 2:
virtualenv venv

# Python 3:
python3 -m venv venv

source env/bin/activate

pip install -r requirements.txt
```

2. Run tests with `pytest`

The test suite runs against the cluster checking for resources in 'theforeman-test' namespace. If you wish to run against a different namespace use: `pytest --namespace my-awesome-namespace`


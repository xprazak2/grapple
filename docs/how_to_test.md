# How to build images

Tests can be found in `molecule` folder.

1. Install dependencies

```
pip install -r requirements.txt && ansible-galaxy collection install -r requirements.yml
```

2. Run tests with molecule

```
molecule test
```
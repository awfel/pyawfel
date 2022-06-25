# pyawfel
Python implementation of the awfel library

## Developing

Install using pip by runnning:

```
pip install -e .[dev]
```

### Testing

Tests are run using pytest.

```
$ pytest --cov
```

### Managing depencies

A script `fix-requirements.sh` is provided for managing the requirements.txt file listing the dependencies. This will build a requirements.txt file listing only packages needed to run the application. Assuming that the script is being run from the root of the project and that `setup.py` is located in that folder:

```
$ bash ./utils/fix-requirements.sh .
```

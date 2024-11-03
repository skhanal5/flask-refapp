# Flask Reference App

## About
This is a reference API used to learn the Flask framework.

## Development

### Environment
This project uses poetry. Once you clone the repo, use `poetry install` to install the dependencies. Then, you
can activate the virtual environment with `poetry shell`.

### Starting the API
Run the app with `poetry run python run.py`. The server should run on http://127.0.0.1:5000/

### Testing
To run tests use `pytest` which will run all the tests in the **~/tests** directory. If you want to see the
code coverage, use ` pytest --cov-report=html --cov=flask_refapp --cov-report=term-missing` which will generate a 
report in the root directory under **~/htmlcov**.

### Code Quality
There is a `.pre-commit-config.yaml` file that contains a pre-commit hook. This hook will
lint the project files using `ruff` and automatically address any violations.

To manually lint the files, use `ruff check`. To format the files, use `ruff format`.

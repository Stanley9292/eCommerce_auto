## Setup

1. Install python to your local machine. (required version 3.9) (Check that it works: "python --version")
2. Check that you have installed pip (pip --version)
3. Install pipenv (pip install --user pipenv)
4. Run "pipenv install" from root directory to install all required packages.

## Run tests

1. Run "pipenv shell" to activate python VM. 
2. Run all tests: "pytest -v -s"
3. Run with a report: pytest -m "negative" --html=my_report.html.
4. Run in debug mode: pytest -m "negative" --pdb
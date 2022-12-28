## Setup

1. Install python to your local machine. (required version 3.9) (Check that it works: "python --version")
2. Check that you have installed pip (pip --version)
3. Install pipenv (pip install --user pipenv)
4. Run "pipenv install" from root directory to install all required packages.

## Run tests

1. Run "pipenv shell" to activate python VM. 
2. Run all tests: "pytest -v -s"
3. pytest -m "negative" --html=my_report.html.

## Setup Allure Report tool (optional)

1. Run in Powershell: "Set-ExecutionPolicy RemoteSigned -scope CurrentUser"
2. Run in Powershell: "iex (new-object net.webclient).downloadstring('https://get.scoop.sh')"
3. Run in Powershell: "scoop install allure".
4. Run in the root of the project: "allure serve .\reports\" to generate reports from reports directory.
5. Run "pytest . --alluredir=reports; allure serve .\reports\" to generate a report for all ran tests.
6. Remove everything from reports folder: "Get-ChildItem -Path C:\workspace\webportalautotesting\reports -Include * -File -Recurse | foreach { $_.Delete()}"

# Automationsetup (Page Object Model framework) 
This is the simple automation script for UAHEP project to test the login module.
## Pre-requisites
* python 2.7.18 installed
* allure 2.13.9 :to generate detailed html reports
* Chrome or Mozilla installed 
## Libraries used
* Selenium: to automate browser  
* pytest: to manage testcases  
* openpyxl: to read/write excelfiles  
* pytest-html: to generate simple html report  
* pytest-xdist: to execute testcases parallely  
* pytest-allure: to integrate allure json files  
additonally  



# Enviroment Setup without creating venv  

```console
pip install -r req.txt
```  
this will install all the required python libraries

```console
sudo apt-get update -y && sudo apt-get install -y allure

```  
this will install allure report (I use ubuntu)  

# Running the automation script
Make sure the you are in project directory.then run 
* ## Normal execution  
```console
pytest -s -v ./testcases/login_py
``` 
* ## Normal execution with generation of HTML report  
```console
pytest -s -v ./testcases/login_py --html=./Reports/demo.html
``` 
we provide the location where we want the reports to be generate to --html argument

* ## Normal execution with generation of allure and html report  
```console
pytest -s -v ./testcases/login_py --html=./Reports/demo.html --alluredir=./Reports/allure
``` 
we provide the location where we want the allure reports to be generate to --alluredir argument

* ## Parallel execution with generation of allure and html report  
```console
pytest -s -v -n=2  ./testcases/login_py --html=./Reports/demo.html --alluredir=./Reports/allure
``` 
we provide the number to instances to browser we want to use to the -n argument 

# processing the allure reports
```console
sudo allure serve {path to folder provided to --alluredir argument previously}
``` 

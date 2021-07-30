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



# Enviroment Setup 
For setting up the virtual enviroment please follow the link
https://linuxize.com/post/how-to-create-python-virtual-environments-on-ubuntu-18-04/

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
> add **python -m** command before following command if the following command dont work
* ## Normal execution  
```console
pytest -s -v ./testcases/login_py
``` 
* ## Normal execution with generation of HTML report  
```console
pytest -s -v ./testcases/login_py --html=./Reports/demo.html
``` 
Preferred directory location should be passed where reports are to be generated as argument for  --html 

* ## Normal execution with generation of allure and html report  
```console
pytest -s -v ./testcases/login_py --html=./Reports/demo.html --alluredir=./Reports/allure
``` 
Preferred directory location should be passed where allure reports are to be generated as argument for  --alluredir

* ## Parallel execution with generation of allure and html report  
```console
pytest -s -v -n=2  ./testcases/login_py --html=./Reports/demo.html --alluredir=./Reports/allure
``` 
Preferred number of instances of browser should be provided as argument to -n

# Processing the allure reports
```console
sudo allure serve {path to folder provided to --alluredir argument previously}
``` 

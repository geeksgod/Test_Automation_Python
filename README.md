# automationsetup
This is the simple automation script for UAHEP project to test the login module.I have  
* Selenium: to automate browser  
* pytest: to manage testcases  
* openpyxl: to read/write excelfiles  
* pytest-html: to generate simple html report  
* pytest-xdist: to execute testcases parallely  
* pytest-allure: to integrate allure json files  
which are all python library and additonally I have used
* allure reports:to generate detailed html reports


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

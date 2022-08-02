# Weather Man

## Overview

Weatherman is a console based applicaton which generates reports regarding **maximum**, **minimum temperature** and **humidity**, also **generate horizontal bar graph** of maximum amd minimum temperature values of every day of a month. There are two type of horizontal bar gaph program generates. 
- Bar graph of maximum and minimum value for every day of a month
- Bar graph of maximum and minimum value for every day of a month (Bars are shelfed side by side)
Two reports is generates:
- Maximum, minimum temperature and humidity report
- Average maximum, average minimum temperature and average mean humidity report
## Key Topics

* How to install the repo
* List of features that the code performs
* Example to run the code features
* How to run test cases

## Installling Repository

Follow following steps to install repository on your local system
1. Before install requirements, you should install Virtual Environment tools for python project, if you have installed then activite the virtual enivronment in your project, otherwise run this command to install virtual environment in your project **Python3 -m venv {project_name}**
2. The names of dependencies for this repository are stored in **requirements.txt** along with versions. You can install all the dependencies using one command **pip install -r requirements.txt** in you virtual environment.
3. To check the tools installed in your virtual environment, you can run command like **"pip list"**
4. I fyou have contributed in project and installed new dependencies as you requirements then to save new dependencies in **requirements.txt** file use command **"pip freeze > requirements.txt"** 
5. You should not push changes to repository along with requirement.txt which hold your dependencies. If you notice the virtual Environment file name is included in **.gitignore** file so that virtual environment does not pushed on to remote repository along with other changes. Anyone who need repo can install those dependencies with one single command.

## List of features that the code performs

- Generate report regarding maximum, minimum temperature and humidity of a year 
- Generate report regarding average maximum, average minimum temperature and average humidity in a month
- Generate Bar graph of maximum and minimum value for every day of a month
- Bar graph of maximum and minimum value for every day of a month (Bars are shelfed side by side). Red represents maximum temperature and blue represent minimum temperature values.
- Run the program using run button or using commands. Commands are prefered way to generate reports.

## Example to run the code features

- To generate maximum, minimum and humidity report:
>**python3 weatherman.py -p {path to zip file containing the weather data files} -e 2011**
- To generate average maximum, average minimum and avergae mean humidity report:
>**python3 weatherman.py -p {path to zip file containing the weather data files} -a 2011/5**

***Note:***
***Notice that the month is given as input imediately after backward slash '2011/5'. If you do not follow this convention then you will encounter error***
- To Generate different graphs:
To generate different graph there must be some input which differs the graphs for same data. But to generate graph of maximum and minimum values for every day in a month with bar line by line, the command is:
>**python3 weatherman.py -p {path to zip file containing the weather data files} -c 2011/5**

To generate bar graph with bars side by side of maximum and minimum tmeperature, the command should be like this:
>**python3 weatherman.py -p {path to zip file containing the weather data files} -c 2011/05**

***Note:***
***Notice that this is not the same command as shown earlier. This command contains single digit month with 0. This convention differs the graphs.***
- Commnds are prefered way to run the code. This is the ideal command to generate all tree reports:
> **python3 weatherman.py -p {path to zip file containing the weather data files} -e 2011 -a 2011/5 -c 2010/6 -c 2010/06** 

## How to run test cases

- Test cases are already included in repository, the file named **test_weatherman.py** contains tests.
- Library used to perform tests is **pytest v7.1.2**
***Note:***
***If you notice, this dependency pytest is already included with version in **'requirements.txt'** you can install it in your virtual environment using pip or install all dependencies with command***
> **pip install -r requirements.txt**
## How Test cases are implemented:
Test cases are implemented only for two functions, one function calculating maximum, minimum and humidity values and second function calculating average maximum, average minimum and average mean humidty values. The first functionwith maximum, minimum and humidity values calculate only for one entire year and second function with averages calculate values for one month of a year. 
Each test case is testing the function with all values avaible in database (weatherfiles.zip) according to their argument requirements. First function which takes a year as input for values calculation for entire year, tests are implemented in this way that the function is being tested for all posible years present in database so every possible input is test. Second function is also implemented the same with values being tested for all possible month in a year present in the database.

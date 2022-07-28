from statistics import mean
from typing import List
import os
import glob
from zipfile import ZipFile
import getopt
import sys

weather_data_of_each_day = {}
filtered_weather_data = []
# The first value is 'none' so we can easily keep track of indexes as there
# is no '0' month
months = [None, 'January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']
weather_data_variables = []

# Extract the 'Zip' file to a directory with same name in current directory
# where the program file is present
#
# This helps as the path is not fixed where the 'zip' file is present the
# program can automatically extract and already know the location of
# extracted file but the program to be successfully executed the 'zip' file
# should be in the same directory as the program
with ZipFile("./weatherfiles.zip", 'r') as zip_file:
    # Extract all the contents of zip file in current directory
    zip_file.extractall()

# Parsing through all the txt files and then converting the text from files to
# List then open any file and copy the weather variables and store them in a
# list
#
# Deleting all the repeated weather variables in all files and only
# storing weather data values.
f = open("./weatherfiles/Murree_weather_2004_Aug.txt")
weather_data_variables = f.readline().split(",")
for filename in glob.glob('./weatherfiles/*.txt'):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        for line in f:
            temporary = line.rstrip().split(",", 1)
            if(temporary[0] == 'PKT'):
                continue
            else:
                filtered_weather_data.append(temporary)
                weather_data_of_each_day[temporary[0]
                                         ] = temporary[1].split(",")


def index_of_weather_variable(weatherVariable):
    """Retrieve the weather variable name and returning the variable
    index to access that variable value present in weather_data_variables
    """
    try:
        index_element = weather_data_variables.index(weatherVariable)
        return index_element
    except ValueError:
        return None


def integer_conversion(s):
    """As all of the data is in textual format and to perform calculations we
    have to convert it to integer format, this function handles the Null
    values in the data and convert them to 0 so no disturbed mathematical
    calculations
    """
    return int(s) if s else 0


def temperature_humidity_calculator_of_year(year):
    """Search in the weather_data_of_each_day which contain data of every day
    for our input year data and store the data of that specific year in a list
    named max_temperature_values, min_temperature_values and mean_humidity_values

    As the data is in string format(textual), it should be converted to integer
    type data to perform our concerened calculations, then returning the our 
    result with the key of the result as to print the result with that specific
    date
    Example: Highest Temperature: 32C on June 18, here 'June 18' is printed 
    becouse of returning result with key
    """
    max_temperature_values = []
    min_temperature_values = []
    mean_humidity_values = []

    SearchedYear = [key for key,
                    val in weather_data_of_each_day.items() if year in key]

    for eachDay in SearchedYear:
        maxTemperatureOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            "Max TemperatureC")-1]
        minTemperatureOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            "Min TemperatureC")-1]
        MeanHumidityOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            " Mean Humidity")-1]

        integermax_temperature_values = integer_conversion(
            maxTemperatureOfOneDay)
        integerHumidityValue = integer_conversion(MeanHumidityOfOneDay)
        integermin_temperature_values = integer_conversion(
            minTemperatureOfOneDay)

        mean_humidity_values.append((integerHumidityValue, eachDay))
        max_temperature_values.append((integermax_temperature_values, eachDay))
        min_temperature_values.append((integermin_temperature_values, eachDay))
    return(max(max_temperature_values),
           min((value, date)
               for value, date in min_temperature_values if value != 0),
           max(mean_humidity_values))


def average_temperature_humidity_calculator_of_month(year, month):
    """Search in the weather_data_of_each_day which contain data of every day
    for our input year data and store the data of that specific year in a list
    named max_temperature_values, min_temperature_values and mean_humidity_values

    maxTemperatureOfOneDay, minTemperatureOfOneDay and MeanHumidityOfOneDay
    are used here to select only our concerened data.

    As the data is in string format(textual), it should be converted to 
    integer type data to perform our concerened calculations
    Example: Highest Average: 21.5 , here we do not need for any data of resut 
    to print as the result is average and it consist of all data.
    """
    max_temperature_values = []
    min_temperature_values = []
    mean_humidity_values = []

    searched_month_of_a_year = [key for key, val in weather_data_of_each_day.items() if year +
                                "-"+month +
                                "-" in key]

    for eachDay in searched_month_of_a_year:
        maxTemperatureOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            "Max TemperatureC")-1]
        minTemperatureOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            "Min TemperatureC")-1]
        MeanHumidityOfOneDay = weather_data_of_each_day[eachDay][index_of_weather_variable(
            " Mean Humidity")-1]

        integermax_temperature_values = integer_conversion(
            maxTemperatureOfOneDay)
        integerHumidityValue = integer_conversion(MeanHumidityOfOneDay)
        integermin_temperature_values = integer_conversion(
            minTemperatureOfOneDay)

        mean_humidity_values.append((integerHumidityValue))
        max_temperature_values.append((integermax_temperature_values))
        min_temperature_values.append((integermin_temperature_values))
    return (mean(max_temperature_values), mean(min_temperature_values), mean(mean_humidity_values))


def bar_chart_of_temperature_in_day(year, month):
    """Data for the specific input year is filtered out of all data and then
    get the specific weather variable which we need for our calculation, 
    storing that data in a specific variable and printing "+" that number of 
    times using another variables like max_temperature_valuesCountera and 
    min_temperature_valuesCounter to keep track of printing loops

    Using ANSI escape sequence to print colored text in print statement
    """
    searched_month_of_a_year = [key for key, val in weather_data_of_each_day.items() if year +
                                "-"+month +
                                "-" in key]

    print(year+" "+months[int(month)])
    for day in searched_month_of_a_year:
        max_temperature_values = weather_data_of_each_day[day][index_of_weather_variable(
            "Max TemperatureC")-1]
        min_temperature_values = weather_data_of_each_day[day][index_of_weather_variable(
            "Min TemperatureC")-1]

        max_temperature_values = integer_conversion(max_temperature_values)
        min_temperature_values = integer_conversion(min_temperature_values)
        # CounterVariables to keep tarck of the loops and prints
        max_temperature_valuesCounter = max_temperature_values
        min_temperature_valuesCounter = min_temperature_values
        # Using ANSI starting sequences to color print as we have to color one
        # complete line
        #
        # Starting Escape Sequence :033[1;32;31m
        print("\033[1;32;31m", day[-2:], end=" ")
        while(max_temperature_valuesCounter > 0):
            print("+", end="")
            max_temperature_valuesCounter = max_temperature_valuesCounter-1
        print(" ", end="")
        print(max_temperature_values, end="C")
        print("")

        print("\033[1;32;34m", day[-2:], end=" ")
        while(min_temperature_valuesCounter > 0):
            print("+", end="")
            min_temperature_valuesCounter = min_temperature_valuesCounter-1
        print(" ", end="")
        print(min_temperature_values, end="C")
        print("")


def bar_chart_of_temperature_in_day_on_same_line(year, month):
    """Data for the specific input year is filtered out of all data and then
    get the specific weather variable which we need for our calculation, 
    storing that data in a specific variable and printing "+" that number of 
    times using another variables like max_temperature_valuesCountera and 
    min_temperature_valuesCounter to keep track of printing loops

    Using ANSI escape sequence to print colored text in print statement and 
    also using 'ending' ANSI escape sequence to print different colors in 
    same line to differentiate between highest and lowest temperature
    """
    searched_month_of_a_year = [key for key, val in weather_data_of_each_day.items() if year +
                                "-"+month +
                                "-" in key]

    print(year+" "+months[int(month)])
    for day in searched_month_of_a_year:
        max_temperature_values = weather_data_of_each_day[day][index_of_weather_variable(
            "Max TemperatureC")-1]
        min_temperature_values = weather_data_of_each_day[day][index_of_weather_variable(
            "Min TemperatureC")-1]
        max_temperature_values = integer_conversion(max_temperature_values)
        min_temperature_values = integer_conversion(min_temperature_values)
        # Counter variable to keep track of loops and prints
        max_temperature_valuesCounter = max_temperature_values
        min_temperature_valuesCounter = min_temperature_values
        print(day[-2:], end="")

        while(max_temperature_valuesCounter > 0):
            # Using ANSI starting and ending escape sequences to color print
            # Starting Escape Sequence :033[1;32;31m
            # Ending Escape Sequence : \033[0;0m
            print("\033[1;32;31m" + " +" + "\033[0;0m", end="")
            max_temperature_valuesCounter = max_temperature_valuesCounter-1

        while(min_temperature_valuesCounter > 0):
            print("\033[1;32;34m" + " +" + "\033[0;0m", end="")
            min_temperature_valuesCounter = min_temperature_valuesCounter-1

        print(" ", end="")
        print(max_temperature_values, end="C ")
        print(min_temperature_values, end="C")
        print("")


def main():
    """Calling Functions according to given Command Line arguments using 
    'getopt' Library and defining the actions with each of the argument 
    after recieving
    After calling the specific argument oriented function the returned 
    results are printed here in the specified format
    Example: Highest Temperature: 32C on June 18, here Result with the
    data 'June 18'
    """
    year = None
    year_month = None
    month = None
    argv = sys.argv[1:]
    # Exception Handling if the given command line arguments are incorrect
    try:
        opts, args = getopt.getopt(argv, "e:a:c:")
    except:
        print("Error")
    # Obtaining the list of arguments as List and then search of each argument
    # using defined flags like '-a', '-e' and '-c' and then performing
    # operations for each argument
    for opt, arg in opts:
        if opt in ['-e']:
            year = arg
            temperature_humidity = temperature_humidity_calculator_of_year(
                arg)
            print("Highest Temperature: " +
                  str(temperature_humidity[0][0])+"C on "+months[int(temperature_humidity[0][1].split("-")[1])]+" "+str(
                      temperature_humidity[0][1].split("-")[2]))

            print("Lowest Temperature: " +
                  str(temperature_humidity[1][0])+"C on "+months[int(temperature_humidity[1][1].split("-")[1])]+" "+str(
                      temperature_humidity[1][1].split("-")[2]))

            print("Humidity: " +
                  str(temperature_humidity[2][0])+"% on "+months[int(temperature_humidity[2][1].split("-")[1])]+" "+str(
                      temperature_humidity[2][1].split("-")[2]))
        elif opt in ['-a']:
            year_month = arg
            year = year_month.split("/")[0]
            month = year_month.split("/")[1]
            mean_temperature_values = average_temperature_humidity_calculator_of_month(
                year, month)

            print("Highest Average: " +
                  str(mean_temperature_values[0]))

            print("Lowest Average: " +
                  str(mean_temperature_values[1]))

            print("Average Mean Humidity: " +
                  str(mean_temperature_values[2])+"%")
        elif opt in ['-c']:
            year_month = arg
            year_with_month = year_month.split("/")
            year = year_with_month[0]
            month = year_with_month[1]

            if(month[0] == "0"):
                bar_chart_of_temperature_in_day_on_same_line(
                    year, str(int(month)))
            else:
                bar_chart_of_temperature_in_day(
                    year, str(int(month)))


if __name__ == "__main__":
    main()

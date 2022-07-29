from statistics import mean
from zipfile import ZipFile
import os
import getopt
import sys
import gc

weather_data = {}
months = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def integer_conversion(s):
    """As all of the data is in textual format and to perform calculations we
    have to convert it to integer format, this function handles the Null
    values in the data and convert them to 0 so no disturbed mathematical
    calculations
    """
    return int(s) if s else 0


def temperature_humidity_calculator_of_year(year, dir_list):
    """Search in the weather_data_of_each_day which contain data of every day
    for our input year data and store the data of that specific year in a list
    named seperate_data_data
    """
    max = float("-inf")
    min = float("inf")
    huimidityMax = float("-inf")
    for file in dir_list:
        if(year in file):
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",", 1)
                weather_data[seperate_date_data[0]
                             ] = seperate_date_data[1].split(",")
                maxTemperature = integer_conversion(
                    weather_data[seperate_date_data[0]][0])
                minTemperature = integer_conversion(
                    weather_data[seperate_date_data[0]][2])
                humidity = integer_conversion(
                    weather_data[seperate_date_data[0]][6])
                if(maxTemperature > max):
                    max = maxTemperature
                if(minTemperature < min):
                    min = minTemperature
                if(humidity > huimidityMax):
                    huimidityMax = humidity

    date = seperate_date_data[0].split("-")
    print("Highest Temperature: "+str(max) +
          "C"+" "+months[int(date[1])]+" "+date[2])
    print("Lowest Temperature: "+str(min) +
          "C"+" "+months[int(date[1])]+" "+date[2])
    print("Humidity: "+str(huimidityMax) +
          "%"+" "+months[int(date[1])]+" "+date[2])
    weather_data.clear()
    del max
    del min
    del huimidityMax
    del seperate_date_data
    gc.collect()


def average_temperature_humidity_calculator_of_month(year, month, dir_list):
    maxTemperature = 0
    minTemperature = 0
    humidity = 0
    counter = 0
    for file in dir_list:
        if(year+"_"+(months[int(month)]) in file):
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",", 1)
                weather_data[seperate_date_data[0]
                             ] = seperate_date_data[1].split(",")
                maxTemperature += integer_conversion(
                    weather_data[seperate_date_data[0]][0])
                minTemperature += integer_conversion(
                    weather_data[seperate_date_data[0]][2])
                humidity += integer_conversion(
                    weather_data[seperate_date_data[0]][7])
                counter = counter+1
            break

    print('Highest Average: '+str(maxTemperature/counter)+'C')
    print("Lowest Average: "+str(minTemperature/counter)+"C")
    print("Average Mean Humidity: "+str(humidity/counter)+"%")
    weather_data.clear()
    del seperate_date_data
    del maxTemperature
    del minTemperature
    del humidity
    del counter
    gc.collect()


def bar_chart_of_temperature_everyday_of_month(year, month, dir_list):
    """ After searching through all the files names in dir_list, just open that
    file which contains monthly data of input month. After seperate the first 
    line containing weather data variables names and filtering only data values.
    Speciifed the index number of values that we need in list conatin data vales and get all data.
    """
    minTemperatureValuesOfAMonth = 0
    maxTemperatureValuesOfAMonth = 0
    day = 1
    day_with_leading_zeros = ""
    month_name = months[int(month)]
    for file in dir_list:
        if(year+"_"+month_name in file):
            f = open("./weatherfiles/"+file)
            print(year+" "+month_name)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",", 1)
                weather_data[seperate_date_data[0]
                             ] = seperate_date_data[1].split(",")
                maxTemperatureValuesOfAMonth = integer_conversion(
                    weather_data[seperate_date_data[0]][0])
                minTemperatureValuesOfAMonth = integer_conversion(
                    weather_data[seperate_date_data[0]][2])

                # Fill the spaces of single digit with zeros so the bar chart is uniform
                day_with_leading_zeros = str(day).zfill(2)
                print("\033[1;32;31m", day_with_leading_zeros, end=" ")
                print("+" * maxTemperatureValuesOfAMonth, end=" ")
                print(maxTemperatureValuesOfAMonth, end="C\n")

                print("\033[1;32;34m", day_with_leading_zeros, end=" ")
                print("+" * minTemperatureValuesOfAMonth, end=" ")
                print(minTemperatureValuesOfAMonth, end="C\n")

                day += 1
            break
    weather_data.clear()
    del minTemperatureValuesOfAMonth
    del maxTemperatureValuesOfAMonth
    del day_with_leading_zeros
    del day
    del month_name
    del seperate_date_data
    gc.collect()


def bar_chart_of_temperature_everyday_of_month_in_one_line(year, month, dir_list):
    """Searching for the year and month in files list and only opening that 
    specific file and saving weather data vlues in List and perform 
    calculations on List, after performing calculations deleting the used 
    variables, data structures and free memeory using Garbage Collector
    """
    minTemperatureValueOfAMonth = 0
    maxTemperatureValueOfAMonth = 0
    day = 1
    day_with_leading_zeros = ""
    month_name = months[int(month)]
    for file in dir_list:
        if(year+"_"+month_name) in file:
            f = open("./weatherfiles/"+file)
            print(year+" "+month_name)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",", 1)
                weather_data[seperate_date_data[0]
                             ] = seperate_date_data[1].split(",")
                maxTemperatureValueOfAMonth = integer_conversion(
                    weather_data[seperate_date_data[0]][0])
                minTemperatureValueOfAMonth = integer_conversion(
                    weather_data[seperate_date_data[0]][2])

                # Fill the spaces of single digit with zeros so the bar chart is uniform
                day_with_leading_zeros = str(day).zfill(2)
                # Color the text using the ANSI Escape Sequence
                print(day_with_leading_zeros, "\033[0;0m", end="")
                print("\033[1;32;31m" + "+" *
                      maxTemperatureValueOfAMonth + "\033[0;0m", end="")

                print("\033[1;32;34m" + "+" *
                      minTemperatureValueOfAMonth + "\033[0;0m", end=" ")
                print(maxTemperatureValueOfAMonth, end="C-")
                print(minTemperatureValueOfAMonth, end="C\n")

                day += 1
            break
    weather_data.clear()
    del minTemperatureValueOfAMonth
    del maxTemperatureValueOfAMonth
    del day_with_leading_zeros
    del month_name
    del seperate_date_data
    del day
    gc.collect()


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
    month = None
    argv = sys.argv[1:]
    # Exception Handling if the given command line arguments are incorrect
    try:
        opts, args = getopt.getopt(argv, "p:e:a:c:")
    except:
        print("Error")

    # Obtaining the list of arguments as List and then search of each argument
    # using defined flags like '-a', '-e' and '-c' and then performing
    # operations for each argument
    for opt, arg in opts:
        if opt in ['-p']:
            with ZipFile(arg, 'r') as zip_file:
                # Extract all the contents of zip file in current directory
                zip_file.extractall()

            dir_list = os.listdir("./weatherfiles")
        elif opt in ['-e']:
            temperature_humidity_calculator_of_year(arg, dir_list)
            print("")
        elif opt in ['-a']:
            month = (arg.split("/")[1])
            year = arg.split("/")[0]
            average_temperature_humidity_calculator_of_month(
                year, (month), dir_list)
            print("")
        elif opt in ["-c"]:
            if(arg.split("/")[1][0] == '0'):
                month = int(arg.split("/")[1])
                year = arg.split("/")[0]
                bar_chart_of_temperature_everyday_of_month_in_one_line(
                    year, str(month), dir_list)
                print("")
            else:
                month = (arg.split("/")[1])
                year = arg.split("/")[0]
                bar_chart_of_temperature_everyday_of_month(
                    year, month, dir_list)
                print("")
    del year
    del month
    del argv
    gc.collect()


if __name__ == "__main__":
    main()

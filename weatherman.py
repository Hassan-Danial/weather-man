from zipfile import ZipFile
import os
import getopt
import sys
import gc


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
    """Search through the files names, only open those files which match
    with our input and only parse through those files.

    Now the only the data which is use full is considered all data values
    which are of no use in are program are neglected only values required
    in our program are used like at seperate_date_data[1] at index 1 max
    temperature values are present and at every loop iteration will give
    us new value of new day, to find out the maxand min values the data
    values are compared with each other,
    """
    max_value_in_max_temp = (float("-inf"), "")
    min_value_in_min_temp = (float("inf"), "")
    huimidity_max = (float("-inf"), "")
    for file in dir_list:
        if(year in file):
            f = open("./weatherfiles/"+file)

            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",")[:10]

                max_temperature_value = integer_conversion(
                    seperate_date_data[1])
                min_temperature_value = integer_conversion(
                    seperate_date_data[3])
                humidity = integer_conversion(
                    seperate_date_data[7])

                if(max_temperature_value > max_value_in_max_temp[0]):
                    max_value_in_max_temp = max_temperature_value, seperate_date_data[0]
                if(min_temperature_value < min_value_in_min_temp[0]):
                    min_value_in_min_temp = min_temperature_value, seperate_date_data[0]
                if(humidity > huimidity_max[0]):
                    huimidity_max = humidity, seperate_date_data[0]
    return [str(max_value_in_max_temp), str(min_value_in_min_temp), str(huimidity_max)]


def average_temperature_humidity_calculator_of_month(year, month, dir_list):
    """" As the for loop at every iteration will give us new max and min
    temperature values, the addition of all the values and counting the
    number of lines in the file will give us the days in month which
    also give us the total number of days to find average of temperature
    """
    maxTemperature = 0
    minTemperature = 0
    humidity = 0
    number_of_days_in_month = 0
    for file in dir_list:
        if(year+"_"+months[int(month)] in file):
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",")[:10]
                maxTemperature += integer_conversion(
                    seperate_date_data[1])
                minTemperature += integer_conversion(
                    seperate_date_data[3])
                humidity += integer_conversion(
                    seperate_date_data[8])
                number_of_days_in_month += 1
            break
    return [maxTemperature/number_of_days_in_month, minTemperature/number_of_days_in_month, humidity/number_of_days_in_month]


def bar_chart_of_temperature_everyday_of_month(year, month, dir_list):
    """ After searching through all the files names in dir_list, just open that
    file which contains monthly data of input month. After seperate the first
    line containing weather data variables names and filtering only data values.
    """
    min_temperature_value_of_a_month = 0
    max_temperature_value_of_a_month = 0
    number_of_days_in_month = 1
    day_with_leading_zeros = ""
    month_name = months[int(month)]
    for file in dir_list:
        if(year+"_"+month_name in file):
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",")[:10]
                max_temperature_value_of_a_month = integer_conversion(
                    seperate_date_data[1])
                min_temperature_value_of_a_month = integer_conversion(
                    seperate_date_data[3])

                # Fill the spaces of single digit with zeros so the bar chart is uniform
                day_with_leading_zeros = str(number_of_days_in_month).zfill(2)
                print("\033[1;32;31m", day_with_leading_zeros, end=" ")
                print("+" * max_temperature_value_of_a_month,
                      "\033[0;0;0m", end="")
                print(max_temperature_value_of_a_month, end="C\n")

                print("\033[1;32;34m", day_with_leading_zeros, end=" ")
                print("+" * min_temperature_value_of_a_month,
                      "\033[0;0;0m", end="")
                print(min_temperature_value_of_a_month, end="C\n")

                number_of_days_in_month += 1
            break
    del seperate_date_data
    gc.collect()


def bar_chart_of_temperature_everyday_of_month_in_one_line(year, month, dir_list):
    """Searching for the year and month in files list and only opening that
    specific file and saving weather data vlues in List and perform
    calculations on List, after performing calculations deleting the used
    variables, data structures and free memeory using Garbage Collector
    """
    min_temperature_value_of_a_month = 0
    max_temperature_value_of_a_month = 0
    number_of_days_in_month = 1
    day_with_leading_zeros = ""
    month_name = months[int(month)]
    for file in dir_list:
        if(year+"_"+month_name) in file:
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                seperate_date_data = line.rstrip().split(",")[:10]
                max_temperature_value_of_a_month = integer_conversion(
                    seperate_date_data[1])
                min_temperature_value_of_a_month = integer_conversion(
                    seperate_date_data[3])

                # Fill the spaces of single digit with zeros so the bar chart is uniform
                day_with_leading_zeros = str(number_of_days_in_month).zfill(2)
                # Color the text using the ANSI Escape Sequence
                print(day_with_leading_zeros, "\033[0;0m", end="")
                print("\033[1;32;31m" + "+" *
                      max_temperature_value_of_a_month + "\033[0;0m", end="")

                print("\033[1;32;34m" + "+" *
                      min_temperature_value_of_a_month + "\033[0;0m", end=" ")
                print(max_temperature_value_of_a_month, end="C-")
                print(min_temperature_value_of_a_month, end="C\n")

                number_of_days_in_month += 1
            break
    del seperate_date_data
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
            print(temperature_humidity_calculator_of_year(arg, dir_list))
            print("")
        elif opt in ['-a']:
            month = (arg.split("/")[1])
            year = arg.split("/")[0]
            print(average_temperature_humidity_calculator_of_month(
                year, (month), dir_list))
            print("")
        elif opt in ["-c"]:
            if(arg.split("/")[1][0] == '0'):
                # Spliting the month string to get month and year
                month = int(arg.split("/")[1])
                year = arg.split("/")[0]
                print(bar_chart_of_temperature_everyday_of_month_in_one_line(
                    year, str(month), dir_list))
                print("")
            else:
                # Spliting the month string to get month and year
                month = (arg.split("/")[1])
                year = arg.split("/")[0]
                bar_chart_of_temperature_everyday_of_month(
                    year, month, dir_list)
                print("")
        else:
            print(
                "Command is in Wrong Format.\nWrite command like this : 'python3 weatherman.py -p ./weatherfiles.zip -e 2004 -a 2005/6 -c 2011/7'")
    del year
    del month
    del argv
    gc.collect()


if __name__ == "__main__":
    main()

from zipfile import ZipFile
import os
import getopt
import sys
import gc


MONTHS = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def convert_to_int(s):
    """As all of the data is in textual format and to perform calculations we
    have to convert it to integer format, this function handles the Null
    values in the data and convert them to 0 so no disturbed mathematical
    calculations
    """
    return int(s) if s else 0


def print_horizontal_bar_chart_with_max_min_values_in_different_lines(number_of_days_in_month,
                                                                      max_temperature_value_of_a_month,
                                                                      min_temperature_value_of_a_month):
    """Prints Horizontal Bar Graph for given data values for every day of a
    month. ANSI escape sequnce is used to color the text. No ending sequence
    is used, becouse we need to switch colors at every line.
    """
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


def get_print(number):
    return ("+"*number)


def print_horizontal_bar_chart_with_max_min_values_in_same_line(number_of_days_in_month,
                                                                max_temperature_value_of_a_month,
                                                                min_temperature_value_of_a_month):
    """Printing the bar graph with maximum and minimum values in same line
    using '+'. Colored the '+' using ANSI escape sequence. Staring and
    edding sequences are used to have two colors in the same line.
    """
    day_with_leading_zeros = str(number_of_days_in_month).zfill(2)
    # Color the text using the ANSI Escape Sequence
    print(day_with_leading_zeros, "\033[0;0m", end="")
    print("\033[1;32;31m" + "+" *
          max_temperature_value_of_a_month + "\033[0;0m", end="")

    print("\033[1;32;34m" + "+" *
          min_temperature_value_of_a_month + "\033[0;0m", end=" ")
    print(max_temperature_value_of_a_month, end="C-")
    print(min_temperature_value_of_a_month, end="C\n")


def get_temperature_humidity_of_a_year(year, directories_list):
    """Search through the files names, only open those files which match
    with our input and only parse through those files.

    Now the only the data which is use full is considered all data values
    which are of no use in are program are neglected only values required
    in our program are used like at seperate_date_data[1] at index 1 max
    temperature values are present and at every loop iteration will give
    us new value of new day, to find out the maxand min values the data
    values are compared with each other,
    """
    max_value_in_maximum_temperature_weather_variable = (float("-inf"), "")
    min_value_in_minimum_temperature_weather_variable = (float("inf"), "")
    max_value_in_huimidity_weather_variable = (float("-inf"), "")
    for file_name in directories_list:
        if(year in file_name):
            file_read_object = open("./weatherfiles/"+file_name)
            for line in file_read_object.readlines()[1:]:
                per_day_data_values = line.rstrip().split(",")[:10]

                max_temperature_value = convert_to_int(
                    per_day_data_values[1])
                min_temperature_value = convert_to_int(
                    per_day_data_values[3])
                humidity = convert_to_int(
                    per_day_data_values[7])

                if(max_temperature_value > max_value_in_maximum_temperature_weather_variable[0]):
                    max_value_in_maximum_temperature_weather_variable = max_temperature_value, per_day_data_values[
                        0]
                if(min_temperature_value < min_value_in_minimum_temperature_weather_variable[0]):
                    min_value_in_minimum_temperature_weather_variable = min_temperature_value, per_day_data_values[
                        0]
                if(humidity > max_value_in_huimidity_weather_variable[0]):
                    max_value_in_huimidity_weather_variable = humidity, per_day_data_values[0]
    return [(max_value_in_maximum_temperature_weather_variable), (min_value_in_minimum_temperature_weather_variable), (max_value_in_huimidity_weather_variable)]


def get_average_temperature_humidity_of_month(year, month, directories_list):
    """" As the for loop at every iteration will give us new max and min
    temperature values, the addition of all the values and counting the
    number of lines in the file will give us the days in month which
    also give us the total number of days to find average of temperature
    """
    max_temperature_values_sum = 0
    minimum_temperature_values_sum = 0
    humidity = 0
    number_of_days_in_month = 0
    for file in directories_list:
        if(year+"_"+MONTHS[int(month)] in file):
            f = open("./weatherfiles/"+file)
            for line in f.readlines()[1:]:
                per_day_data_values = get_convert_read_file_content_lines_to_list(
                    line)
                max_temperature_values_sum += convert_to_int(
                    per_day_data_values[1])
                minimum_temperature_values_sum += convert_to_int(
                    per_day_data_values[3])
                humidity += convert_to_int(
                    per_day_data_values[8])
                number_of_days_in_month += 1
            break
    return [(max_temperature_values_sum/number_of_days_in_month), (minimum_temperature_values_sum/number_of_days_in_month), (humidity/number_of_days_in_month)]


def bar_chart_of_temperature_everyday_of_month(year, month, directories_list):
    """ After searching through all the files names in directories_list, just open that
    file which contains monthly data of input month. After seperate the first
    line containing weather data variables names and filtering only data values.
    """
    number_of_days_in_month = 1
    month_name = MONTHS[int(month)]
    for file in directories_list:
        if(year+"_"+month_name in file):
            file_read_object = open("./weatherfiles/"+file)
            for line in file_read_object.readlines()[1:]:
                per_day_data_values = get_convert_read_file_content_lines_to_list(
                    line)
                # Fill the spaces of single digit with zeros so the bar chart is uniform
                print_horizontal_bar_chart_with_max_min_values_in_different_lines(
                    number_of_days_in_month,
                    convert_to_int(per_day_data_values[1]),
                    convert_to_int(per_day_data_values[3]))
                number_of_days_in_month += 1
            break
    del per_day_data_values
    gc.collect()


def get_convert_read_file_content_lines_to_list(line):
    """This module is used to convert the line present in the text files to
    list so we can access data values saperately acoording to our calculation.

    Only first 10 value are selected every line, becouse all other data is 
    irrelevent and we don't need them in our calculations so why store them.
    """
    return line.rstrip().split(",")[:10]


def bar_chart_of_temperature_everyday_of_month_in_one_line(year, month, directories_list):
    """Searching for the year and month in files list and only opening that
    specific file and saving weather data vlues in List and perform
    calculations on List, after performing calculations deleting the used
    variables, data structures and free memeory using Garbage Collector
    """
    number_of_days_in_month = 1
    month_name = MONTHS[int(month)]
    for file_name in directories_list:
        if(year+"_"+month_name) in file_name:
            file_read_object = open("./weatherfiles/"+file_name)
            for line in file_read_object.readlines()[1:]:
                per_day_data_values = get_convert_read_file_content_lines_to_list(
                    line)
                print_horizontal_bar_chart_with_max_min_values_in_same_line(
                    number_of_days_in_month,
                    convert_to_int(per_day_data_values[1]),
                    convert_to_int(per_day_data_values[3]))
                number_of_days_in_month += 1
            break


def command_line_arguments():
    """This modile is used to execute program using commands and providing all
    relevent information to program before the execution of program.
    """
    year = None
    month = None
    argv = sys.argv[1:]
    # Exception Handling if the given command line arguments are incorrect
    try:
        opts, args = getopt.getopt(argv, "p:e:a:c:")
    except:
        print("Please give arguments in sequence, you should give path command in this format:")
        print(
            "'python3 weatherman.py -p {path} -e 2005 -c 2005/11 -c 2005/05 -a 2011/5'")

    # Obtaining the list of arguments as List and then search of each argument
    # using defined flags like '-p' '-a', '-e' and '-c' and then performing
    # operations for each argument
    try:
        for opt, arg in opts:
            if opt in ['-p']:
                with ZipFile(arg, 'r') as zip_file:
                    # Extract all the contents of zip file in current directory
                    zip_file.extractall()
                    # Selecting only txt files as there are other files in the
                    # databse causing problems in dataflow
                directories_list = [file_in_folder for file_in_folder in os.listdir(
                    "./weatherfiles") if file_in_folder.endswith('.txt')]
            elif opt in ['-e']:
                print(get_temperature_humidity_of_a_year(arg, directories_list))
                print("")
            elif opt in ['-a']:
                month = (arg.split("/")[1])
                year = arg.split("/")[0]
                print(get_average_temperature_humidity_of_month(
                    year, (month), directories_list))
                print("")
            elif opt in ["-c"]:
                if(arg.split("/")[1][0] == '0'):
                    # Spliting the month string to get month and year
                    month = int(arg.split("/")[1])
                    year = arg.split("/")[0]
                    print(bar_chart_of_temperature_everyday_of_month_in_one_line(
                        year, str(month), directories_list))
                    print("")
                else:
                    # Spliting the month string to get month and year
                    month = (arg.split("/")[1])
                    year = arg.split("/")[0]
                    bar_chart_of_temperature_everyday_of_month(
                        year, month, directories_list)
                    print("")
            else:
                print(
                    "Command is in Wrong Format.\nWrite command like this : 'python3 weatherman.py -p ./weatherfiles.zip -e 2004 -a 2005/6 -c 2011/7'")
    except:
        print(
            "\033[0;32;31m", "Please Recheck Your command \nYour command must be in this format :\n'python3 weatherman.py -p {path} -e 2005 -c 2005/11 -c 2005/05 -a 2011/5'")
        print("The Months should be immediately after backward slash like: '2005/6', also write valid month")
        print("You must provide the zip folder location after '-p' indicator\n\n")
    del year
    del month
    del argv
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
    command_line_arguments()


if __name__ == "__main__":
    main()

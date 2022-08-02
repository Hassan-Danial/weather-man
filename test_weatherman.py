import weatherman
import os
from zipfile import ZipFile


with ZipFile("/Users/hassandanial/W/weatherfiles.zip", 'r') as zip_file:
    # Extract all the contents of zip file in current directory
    zip_file.extractall()

DIRECTORIES_LIST = [file_in_folder for file_in_folder in os.listdir(
    "./weatherfiles") if file_in_folder.endswith('.txt')]

YEARS = []
YEAR_WITH_MONTH = []
# Filtering the years present in databse to test values for each year.
for file in DIRECTORIES_LIST:
    if(len(file.split("_")) > 2):
        year = (file.split("_")[2])
        if(year in YEARS):
            year_in_list = YEARS.index((year))
        else:
            YEARS.append(year)
            year_in_list = YEARS.index((year))
# Filtering the months with year present in databse to test every possible month input for each year.
for file in DIRECTORIES_LIST:
    if(len(file.split("_")) > 2):
        year = (file.split("_")[2])
        month = (file.split("_")[3].split(".")[0])
        if((year, month) in YEAR_WITH_MONTH):
            year_and_month_in_list = YEAR_WITH_MONTH.index((year, month))
        else:
            YEAR_WITH_MONTH.append((year, month))
            year_and_month_in_list = YEAR_WITH_MONTH.index((year, month))

del year


def test_temperature_humidity_calculator_of_year():
    max_value_in_max_temp = float("-inf")
    min_value_in_min_temp = float("inf")
    humidity_max = float("-inf")
    temperature_humidity_values_of_one_year = []
    for year in YEARS:
        for file in DIRECTORIES_LIST:
            if(str(year) in file):

                read_object = open("./weatherfiles/"+file)

                for line in read_object.readlines()[1:]:
                    seperate_date_data = weatherman.get_convert_read_file_content_lines_to_list(
                        line)

                    max_temperature_value = weatherman.convert_to_int(
                        seperate_date_data[1])
                    min_temperature_value = weatherman.convert_to_int(
                        seperate_date_data[3])
                    humidity = weatherman.convert_to_int(
                        seperate_date_data[7])
                    if(max_temperature_value > max_value_in_max_temp):
                        max_value_in_max_temp = max_temperature_value
                    if(min_temperature_value < min_value_in_min_temp):
                        min_value_in_min_temp = min_temperature_value
                    if(humidity > humidity_max):
                        humidity_max = humidity
        # assert will keep the test running until it recieves false until then
        # assert keep assuring that values are equal
        temperature_humidity_values_of_one_year = weatherman.get_temperature_humidity_of_a_year(
            year, DIRECTORIES_LIST)
        assert temperature_humidity_values_of_one_year[0][0] == max_value_in_max_temp and temperature_humidity_values_of_one_year[
            1][0] == min_value_in_min_temp and temperature_humidity_values_of_one_year[2][0] == humidity_max
        max_value_in_max_temp = float("-inf")
        min_value_in_min_temp = float("inf")
        humidity_max = float("-inf")


def test_average_temperature_humidity_calculator_of_month():
    max_temperature_values_sum = 0
    min_temperature_values_sum = 0
    humidity = 0
    number_of_days_in_month = 0
    for year_and_month in YEAR_WITH_MONTH:
        for file in DIRECTORIES_LIST:
            if(year_and_month[0]+"_"+year_and_month[1] in file):
                read_object = open("./weatherfiles/"+file)
                for line in read_object.readlines()[1:]:
                    seperate_date_data = weatherman.get_convert_read_file_content_lines_to_list(
                        line)
                    max_temperature_values_sum += weatherman.convert_to_int(
                        seperate_date_data[1])
                    min_temperature_values_sum += weatherman.convert_to_int(
                        seperate_date_data[3])
                    humidity += weatherman.convert_to_int(
                        seperate_date_data[8])
                    number_of_days_in_month = number_of_days_in_month+1
                break
        average_max_min_temperature_and_humidity = weatherman.get_average_temperature_humidity_of_month(
            year_and_month[0], weatherman.MONTHS.index(year_and_month[1]), DIRECTORIES_LIST)
        assert (average_max_min_temperature_and_humidity[0]) == (max_temperature_values_sum/number_of_days_in_month) and (
            average_max_min_temperature_and_humidity[1]) == (min_temperature_values_sum/number_of_days_in_month) and (average_max_min_temperature_and_humidity[2]) == (humidity/number_of_days_in_month)
        max_temperature_values_sum = 0
        min_temperature_values_sum = 0
        humidity = 0
        number_of_days_in_month = 0

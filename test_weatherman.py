import weatherman
import os
from zipfile import ZipFile


with ZipFile("/Users/hassandanial/W/weatherfiles.zip", 'r') as zip_file:
    # Extract all the contents of zip file in current directory
    zip_file.extractall()

dir_list = [f for f in os.listdir(
    "./weatherfiles") if f.endswith('.txt')]

Years = []
Yearwithmonth = []
for file in dir_list:
    if(len(file.split("_")) > 2):
        year = (file.split("_")[2])
        if(year in Years):
            ItemNumber = Years.index((year))
        else:
            Years.append(year)
            ItemNumber = Years.index((year))
for file in dir_list:
    if(len(file.split("_")) > 2):
        year = (file.split("_")[2])
        month = (file.split("_")[3].split(".")[0])
        if((year, month) in Yearwithmonth):
            ItemNumber = Yearwithmonth.index((year, month))
        else:
            Yearwithmonth.append((year, month))
            ItemNumber = Yearwithmonth.index((year, month))


def test_temperature_humidity_calculator_of_year():
    max_value_in_max_temp = float("-inf")
    min_value_in_min_temp = float("inf")
    humidity_max = float("-inf")
    List = []
    for x in Years:
        for file in dir_list:
            if(str(x) in file):

                f = open("./weatherfiles/"+file)

                for line in f.readlines()[1:]:
                    seperate_date_data = line.rstrip().split(",")[:11]

                    max_temperature_value = weatherman.integer_conversion(
                        seperate_date_data[1])
                    min_temperature_value = weatherman.integer_conversion(
                        seperate_date_data[3])
                    humidity = weatherman.integer_conversion(
                        seperate_date_data[7])
                    if(max_temperature_value > max_value_in_max_temp):
                        max_value_in_max_temp = max_temperature_value
                    if(min_temperature_value < min_value_in_min_temp):
                        min_value_in_min_temp = min_temperature_value
                    if(humidity > humidity_max):
                        humidity_max = humidity

        print(max_value_in_max_temp, min_value_in_min_temp, humidity_max)
        List = weatherman.temperature_humidity_calculator_of_year(
            x, dir_list)
        print(List)
        assert int(List[0]) == max_value_in_max_temp and int(
            List[1]) == min_value_in_min_temp and int(List[2]) == humidity_max
        max_value_in_max_temp = float("-inf")
        min_value_in_min_temp = float("inf")
        humidity_max = float("-inf")


def test_average_temperature_humidity_calculator_of_month():
    maxTemperature = 0
    minTemperature = 0
    humidity = 0
    number_of_days_in_month = 0
    for x in Yearwithmonth:
        for file in dir_list:
            if(x[0]+"_"+x[1] in file):
                f = open("./weatherfiles/"+file)
                for line in f.readlines()[1:]:
                    seperate_date_data = line.rstrip().split(",")[:10]
                    maxTemperature += weatherman.integer_conversion(
                        seperate_date_data[1])
                    minTemperature += weatherman.integer_conversion(
                        seperate_date_data[3])
                    humidity += weatherman.integer_conversion(
                        seperate_date_data[8])
                    number_of_days_in_month = number_of_days_in_month+1
                break

        print(maxTemperature/number_of_days_in_month, minTemperature /
              number_of_days_in_month, humidity/number_of_days_in_month)
        List = weatherman.average_temperature_humidity_calculator_of_month(
            x[0], weatherman.months.index(x[1]), dir_list)
        print(List)
        assert (List[0]) == (maxTemperature/number_of_days_in_month) and (
            List[1]) == (minTemperature/number_of_days_in_month) and (List[2]) == (humidity/number_of_days_in_month)
        maxTemperature = 0
        minTemperature = 0
        humidity = 0
        number_of_days_in_month = 0

import glob                         # this module helps in selecting files 
import pandas as pd                 # this module helps in processing CSV files
import xml.etree.ElementTree as ET  # this module helps in processing XML files.
from datetime import datetime

def extract_from_csv(file_to_process):
    dataframe = pd.read_csv(file_to_process)
    return dataframe

def extract_from_json(file_to_process):
    dataframe = pd.read_json(file_to_process, lines= True)
    return dataframe

def extract_from_xml(file_to_process):
    dataframe = pd.DataFrame(columns=["car_model", "year_of_manufacture", "price", "fuel"])
    tree = ET.parse(file_to_process)
    root = tree.getroot()
    for car in root:
        car_model = car.find("car_model").text
        year_of_manufacture = int(car.find("year_of_manufacture").text)
        price = float(car.find("price").text)
        fuel = car.find("fuel").text
        dataframe = dataframe.append({"car_model":car_model, "yar_of_manufacture":year_of_manufacture, 
                                    "price":price, "fuel":fuel}, ignore_index=True)
    return dataframe

def extract():
    extracted_data = pd.DataFrame(columns=['car_model','year_of_manufacture','price', 'fuel']) # create an empty data frame to hold extracted data
    
    #process all csv files
    for csvfile in glob.glob("ETL/*.csv"):
        extracted_data = extracted_data.append(extract_from_csv(csvfile), ignore_index=True)
        
    #process all json files
    for jsonfile in glob.glob("ETL/*.json"):
        extracted_data = extracted_data.append(extract_from_json(jsonfile), ignore_index=True)
    
    #process all xml files
    for xmlfile in glob.glob("ETL/*.xml"):
        extracted_data = extracted_data.append(extract_from_xml(xmlfile), ignore_index=True)
        
    return extracted_data

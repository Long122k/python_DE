from extract import extract
from transform import transform
from load import load
from log import log


tmpfile    = "dealership_temp.tmp"               # file used to store all extracted data
logfile    = "dealership_logfile.txt"            # all event logs will be stored in this file
targetfile = "dealership_transformed_data.csv"   # file where transformed data is stored

log("ETL Job Started")

log("Extract phase Started") 
extracted_data = extract() 
log("Extract phase Ended")

log("Transform phase Started") 
transformed_data = transform(extracted_data) 
log("Transform phase Ended")

log("Load phase Started") 
load(targetfile,transformed_data) 
log("Load phase Ended")

log("ETL Job Ended")
# print(extracted_data)
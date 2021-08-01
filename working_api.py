import requests
import pandas as pd

url = "http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=f988634b0bc5e560be7136d04d952a5b"  
text = requests.get(url)

df = pd.DataFrame(columns=["", "Rate"])
jtext = text.json()['rates']

for key, value in jtext.items():
    df= df.append({"":key, "Rate":value}, ignore_index = True)
    
file_name = 'exchange_rates_1.csv'
df.to_csv(file_name, index = False)
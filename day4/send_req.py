


import requests
import json
import pandas as pd
url = "http://api.open-notify.org/iss-now.json"

header = {
    "User-Agent":"Nasa"
}

n = 0
arr_data = []
while n < 2:
    data = requests.get(url,headers=header)
    print(data)
    js_data = json.loads(data.text)
    print(js_data)
    long = js_data["iss_position"]["longitude"]
    lat = js_data["iss_position"]["latitude"]
    new_js = {
        "lat":lat,
        "long":long
    }
    arr_data.append(new_js)
    n = n +1

df = pd.DataFrame(arr_data)
df.to_csv("out.csv")

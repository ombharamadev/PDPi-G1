
import requests
import json
import pandas as pd
url = "https://vegetablemarketprice.com/api/dataapi/market/himachalpradesh/daywisedata?date=2024-07-25"
header = {
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Google Chrome\";v=\"127\", \"Chromium\";v=\"127\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "cookie": "_ga=GA1.1.579592366.1719805178; JSESSIONID=38C46DB9AF31C7615CEA99E25DB537BF; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1721968664:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1721968664:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1721968664:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; FCNEC=%5B%5B%22AKsRol_gVgIw70rNTHtKXRH7HNLVSjRH0OwYyx-SF6oIpx2Cx7CAUL_Igzqai36PYs2KfJBNNHQvXV4BEDuEvrW_8aV7gdAXcU-OD7YPlMIVdxbPMJj2e9MT2uIOjDfylixMFne_R5AxcABLpoI55zkQyoa1zVhq0Q%3D%3D%22%5D%5D; _ga_2RYZG7Y4NC=GS1.1.1721968580.5.1.1721968613.0.0.0",
    "Referer": "https://vegetablemarketprice.com/market/himachalpradesh/today",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Referrer-Policy": "strict-origin-when-cross-origin"
  }

data = requests.get(url,headers=header)
print(data)

js_data = json.loads(data.text)
arr_data = []
for api in js_data["data"]:
    veg_id = api["id"]
    veg_name = api["vegetablename"]
    whole_price = api["price"]
    retail_price = api["retailprice"]
    shop_price= api["shopingmallprice"]
    units =api["units"]
    new_js = {
      "veg_id":veg_id,
      "veg_name":veg_name,
      "whole_price":str(whole_price),
      "retail_price":str(retail_price),
      "shop_mall_price":str(shop_price),
      "units":str(units)
    }
    arr_data.append(new_js)
    #input("....")
  
df = pd.DataFrame(arr_data)
df.to_csv("out.csv")

from datetime import datetime , timedelta

start_date = datetime(2024,5,1)
end_date = datetime(2024,6,30)

current_date = start_date
date_arr = []
while current_date <= end_date:

    save_date = current_date.strftime("%Y-%m-%d")

    date_arr.append(save_date)
    current_date = current_date + timedelta(days=1)

print(date_arr)

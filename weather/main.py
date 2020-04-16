import requests
from weather.data import Location,WeatherElement

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)  #向html提出get請求
json_content = html_content.json()  #將內容轉為json

records = json_content.get('records')
location = records.get('location')
#取得欄位資料, location是list
# for i in range(len(location)):
#     print(location[i])

allLocations = []
for l in location:
    location_site = Location()
    location_site.from_json(l)
    location.append(location_site)

    weather_element_json = l.get('weatherElement')
    element = WeatherElement()
    element.from_json(weather_element_json)
    l.set_weather_element(element)

    allLocations.append(l)

for i in len(allLocations):
    print(allLocations)

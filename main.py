import requests
from data import Location,WeatherElement

url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0003-001?Authorization=rdec-key-123-45678-011121314'
html_content = requests.get(url)  #向html提出get請求
json_content = html_content.json()  #將內容轉為json

records = json_content.get('records')
location = records.get('location')
#取得欄位資料, location是list
# for i in range(len(location)):
#     print(location[i])

allLocations = []
for item in location:
    l = Location()
    l.from_json(item)

    weather_element_json = item.get('weatherElement')
    element = WeatherElement()
    element.from_json(weather_element_json)
    l.set_waeather_element(element)

    allLocations.append(l)


    #
    # lat = l.get('lat')
    # lon = l.get('lon')
    # locationName = l.get('locationName')
    # stationId= l.get('stationId')
    # time = l.get('time').get('obstime') #obstime=>>None
    #
    # print(lat, lon, locationName, stationId, time)
    #
    # #取得觀測資料
    # weatherElement = item.get('weatherElement')
    # for element in weatherElement:
    #     elementName = element.get('elementName')
    #     elementValue = element.get('elementValue')

    #     print(elementName, elementValue)
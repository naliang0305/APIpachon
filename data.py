class Location:
    def __init__(self, location_name=None, lat=None, lon=None,
                 station_id=None, time=None, weather_element=None):
        self.locationName = location_name
        self.lat = lat
        self.lon = lon
        self.stationId = station_id
        self.time = time
        self.weatherElement = weather_element
    def from_json(self, json_data):
        self.locationName = json_data.get('locationName')
        self.lat = json_data.get('lat')
        self.lon = json_data.get('lon')
        self.stationId = json_data.get('stationId')
        self.time = json_data.get('time').get('obstime')

class WeatherElement:
    def __init__(self, wdir=None, wdsd=None, temp=None, humd=None, h24r=None):
        self.wdir = wdir
        self.wdsd = wdsd
        self.temp = temp
        self.humd = humd
        self.h24r = h24r

    def from_json(self, weather_element):
        for element in weather_element:
            element_name = element.get('elementName')
            element_value = element.get('elementValue')

            if element_name == 'WDIR':
                self.wdsd = element_value

            if element_name == 'WDSD':
                self.wdsd = element_value

            if element_name == 'TEMP':
                self.temp = element_value

            if element_name == '24R':
                self.h_24r = element_value


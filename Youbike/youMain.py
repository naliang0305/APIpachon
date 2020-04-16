import requests

url = 'http://opendata.hccg.gov.tw/dataset/1f334249-9b55-4c42-aec1-5a8a8b5e07ca/resource/3f2d8472-7bae-48d0-909f-546591a34d34/download/20191231090605186.json'
html_content = requests.get(url)  #向html提出get請求
print(html_content.status_code)
# print(json_content)
records = json_content.get()
location = records.get('站點名稱')
for i in range(len(location)):
    print(location[i])
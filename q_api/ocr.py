# https://ocr.space/OCRAPI
# https://i.pinimg.com/474x/34/8b/c5/348bc51a10af4a96dea207318f88cc6b.jpg
# https://hanasia.com/_sys/_upload/image/201906/12/15603238171847.jpg
import requests
import json

url = "https://api.ocr.space/parse/imageurl?apikey=K81226607288957&url=https://hanasia.com/_sys/_upload/image/201906/12/15603238171847.jpg&language=kor&isOverlayRequired=true"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data['ParsedResults'][0]['ParsedText'])

# print(json.dumps(data, ensure_ascii=False, indent=2))
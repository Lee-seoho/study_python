import json
import platform
import requests
import config
import auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('NCSICL71UDGTN3KG', 'D51PFE3KNIONBDLSTYWRO9HJGOYW5WCY')

data = {
    "message": {
        "to": "01072970766",
        "from": "01039553856",
        "text": "서호야"
    }
}
print(json.dumps(data, ensure_ascii=False))
response = requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)
print(response.status_code)
print(response.text)

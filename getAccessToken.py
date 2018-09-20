import json
import requests
import time

def getNew(data):
    url = 'https://accounts.spotify.com/api/token'
    params = {"grant_type": "refresh_token", "refresh_token": data['refresh_token'], "client_id": data['client_id'], "client_secret": data['client_secret'] }
    expireTime = int(time.time()) + 3600
    # print(expireTime)
    r = requests.post(url, params)
    # print(r.text)
    res = eval(r.text)
    # print(res['access_token'])
    
    updateData = {"access_token": res['access_token'], "expires_at": expireTime}
    with open('settings.json', 'r') as infile:
        jsonData = json.load(infile)
        jsonData.update(updateData)
        # print(jsonData)
        with open('settings.json', 'w') as outfile:
            json.dump(jsonData, outfile)
            return jsonData
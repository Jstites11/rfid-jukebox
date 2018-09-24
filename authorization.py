import urllib.parse
import requests
import json
import getAccessToken
# The purpose of this file is to generate a refresh token for your spotify account
# STEP 1
# go to your spotify application and add to the redirect uris section: http://example.com/callback
# run authorization.py and go to the link to autorize yourself as a user

# Put your client_id and client secret here
client_id = ""

client_secret = ""

if(client_id == "" and client_secret == ""):
    print("Make sure to add your client_id and client_secret. \n To get your client_id and client_secret, create a spotify app at https://developer.spotify.com/dashboard/")
    raise SystemExit

# You can use any URL you want but because I am not getting a callback to an actual website, I am just using this as a way to get the code
redirect_uri = 'http://example.com/callback'


# When you get your code after step 1, paste it here and run authorization.py again the code should be in your URL bar after ?code=.....
code = ""



if(code == ""):
    print("You are not authorized! Please click on the link below to add your account to the application")
    print()
    scopes = 'user-modify-playback-state%20playlist-read-collaborative%20user-read-currently-playing%20user-read-playback-state'
    paramsDict = {'client_id': client_id, 'response_type': 'code', 'redirect_uri': redirect_uri, 'scope': scopes}

    params = urllib.parse.urlencode(paramsDict)


    print('https://accounts.spotify.com/authorize/?'+ params)

# STEP 2
# your webbrowser url field should have something like
# http://example.com/callback?code=....
# Copy the value after "?code=" and paste it in the variable "code" above then run authorization again

if(code != ""):
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect_uri, "client_id": client_id, "client_secret": client_secret}
    r = requests.post(url, data)
    print(r)
    print("If the response is 200 then that means the refresh token and access token have been added to settings.json \n You can run \"python ./main.py\" now.")
    print("If the response is not 200 then please post an issue on github and I will try and help.")
    jsonData = eval(r.text)
    data['access_token'] = jsonData['access_token']
    data['refresh_token'] = jsonData['refresh_token']
    # print(data)
    with open('settings.json', 'w') as outfile:
        json.dump(data, outfile)
    getAccessToken.getNew(data)





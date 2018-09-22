import requests
import json
import time
   

def getPlayInfo(data):
    time.sleep(1)
    
    url = "https://api.spotify.com/v1/me/player"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    if(r.status_code != 200):
        return "There was an error controlling your music. Make sure you are running spotify on one of your devices!"
    playData =json.loads(r.text)
    song_name = playData['item']['name']
    all_artists = ""
    num_artists = len(playData['item']['artists'])
    count = 0
    for artists in playData['item']['artists']:
        if(num_artists == 1):
            all_artists += artists['name']
            count += 1
        elif(count < num_artists-1):
            all_artists += artists['name'] + ', '
            count += 1
        else:
            all_artists += artists['name'] 
    return ("Now playing " + song_name + " by " + all_artists)
    


def playSong(data, uri):
    url = "https://api.spotify.com/v1/me/player/play"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    body = "{\"context_uri\":\"" + uri + "\"}"
    requests.put(url, headers=headers, data=body)
    return getPlayInfo(data)

    

def nextSong(data):
    url = "https://api.spotify.com/v1/me/player/next"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    requests.post(url, headers=headers)
    return getPlayInfo(data)

def prevSong(data):
    url = "https://api.spotify.com/v1/me/player/previous"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    requests.post(url, headers=headers)
    return getPlayInfo(data)

def pauseSong(data):
    url = "https://api.spotify.com/v1/me/player/pause"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    requests.put(url, headers=headers)
    return "Paused song"

def resumeSong(data):
    url = "https://api.spotify.com/v1/me/player/play"
    access_token = "Bearer " + data['access_token']
    headers = {"Authorization": access_token, "Accept": "application/json", "Content-Type": "application/json"}
    requests.put(url, headers=headers)
    return getPlayInfo(data)

# def increaseVolume():


# def decreaseVolume():

# def toggleShuffle():


# def toggleRepeat():

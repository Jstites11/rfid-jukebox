import parseJSON
import getAccessToken
import time
import spotifyRequests
import json

if __name__ == "__main__":
    # Retreieve RFID's and the corresponding spotify URI
    rfid = {}
    rfid = parseJSON.getSpotifyDict()

    # check to see if there is a saved refresh token, if not tell user to run authorization.py
    with open('settings.json') as file:
        data = json.load(file)
    inputVal = ""
    playing = ""
    if('refresh_token' in data):
        while(True):
            inputVal = input("RFID(type \"exit\" to exit): ")
            if(data['expires_at'] < int(time.time())):
                data.update(getAccessToken.getNew(data))
                print('Got new access_token!')
            if(inputVal == "exit"):
                raise SystemExit     
            elif(inputVal not in rfid):
                print('Unrecognized RFID tag')
            elif(rfid[inputVal] == "resume"):
                print(spotifyRequests.resumeSong(data))
                
            elif(rfid[inputVal] == "pause"):
                print(spotifyRequests.pauseSong(data))
                
            elif(rfid[inputVal] == "next"):
                print(spotifyRequests.nextSong(data))
                
            elif(rfid[inputVal] == "back"):
                print(spotifyRequests.prevSong(data))
                
            else:
                print(spotifyRequests.playSong(data, rfid[inputVal]))
                
            




    else:
        print("You do not have proper authentication to run the jukebox!")
        print("Please follow the instructions in autorization.py to obtain the refresh_token needed for authorization")
        raise SystemExit

    
    
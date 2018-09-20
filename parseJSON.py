import csv
import json

# I was using CSV files but figured JSON would be much simpler
# def getSpotifyDict():
#     spotifyDict = {}
#     with open('spotifyData.csv') as csv_file:   
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         for row in csv_reader:
#             spotifyDict[row[0]] = row[1]
#     return spotifyDict 

def getSpotifyDict():
    with open("spotifyData.json") as file:
        data = json.load(file)
        # print(data)
        return data
    
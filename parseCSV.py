import csv

def getSpotifyDict():
    spotifyDict = {}
    with open('spotifyData.csv') as csv_file:   
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            spotifyDict[row[0]] = row[1]
    return spotifyDict 
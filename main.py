import parseCSV
import spotifyRequests


if __name__ == "__main__":
    spotifyDict = parseCSV.getSpotifyDict()
    print(spotifyDict)
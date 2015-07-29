# Program to create a playlist out of the words of a message


from nltk import trigrams
from pandas import Series
import spotipy


# Fetch the message and split it into most popular phrases 
message = raw_input("Enter text  : ")
grams = Series(trigrams(message.split()))

list_of_phrases = []
for phrase in grams:
    list_of_phrases.append(' '.join(phrase))


#Search each phrase in Spotify db and return matching track and it's corresponding artist
spotify = spotipy.Spotify()
def generator(substr):  
    try:
        trackList = []
        singleQueryTrackList = []
        apiResponse = spotify.search(q='track:' + substr, type='track') 
        tracks = apiResponse.get("tracks")
        items = tracks.get('items')
        for item in items:   
            print item.get('name') + " : by " + item.get("artists")[0].get('name')
            singleQueryTrackList.append(item.get('name') + ": by " + item.get("artists")[0].get('name'))
        #print ' - - - - -\n'
            break
        trackList.append(singleQueryTrackList)
        return trackList
    except IndexError:
        'null'


#Calling the user defined function: generator        
for item in list_of_phrases:
    generator(item)
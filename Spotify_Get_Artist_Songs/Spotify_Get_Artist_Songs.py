def Spotify_Get_Artist_Songs(source="jazzland.csv",client_id = '7573e737126b419fb79adaad8144ee52',client_secret = 'f0a4f41a239a4886b7337a809dc9dba7'):
    import spotipy
    import random
    from urlextract import URLExtract
    from spotipy.oauth2 import SpotifyClientCredentials
    import pandas as pd

    # From csv file of library, get all artists
    data = pd.read_csv(source)
    df = pd.DataFrame(data)
    pd.set_option('display.max_columns', None)
    artists = df['Artist Name'].tolist()
    uniqart = list(set(artists))

   # Setting spotify information
    client_id = client_id
    client_secret = client_secret
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)  # spotify object to access API

    # Printing top songs of each artists' related artists
    tracklist = list()
    for elem0 in uniqart:
        try:
            # Searching through spotify data for artist Id
            result = sp.search(elem0)
            resulto = str(result)
            result = str(result).split("}")
            x = 0
            for elem in result:
                if '\'id\':' in elem and x == 0:
                    x = x + 1
                    artisturi = 'spotify:artist:' + elem.split('\'id\': ')[1].split(",")[0].split("\'")[1]

            # Searching through artists related artists' data on spotify for Id
            resultrel = sp.artist_related_artists(artisturi)
            relartstring = str(resultrel)
            extractor = URLExtract()
            urls = extractor.find_urls(relartstring)
            uniqurl = list(set(urls))
            relurllist = list()
            for elem in uniqurl:
                if 'art' in elem and 'open' in elem:
                    relurllist.append('spotify:artist:' + elem.split("/")[-1])

            # For each related artist searching through top songs on spotify for name and song titles
            for elem1 in relurllist:

                # Generating name
                x = 0
                relarttop = sp.artist_top_tracks(elem1)
                relarttopstr = str(relarttop)
                # print(relarttopstr)
                namer = relarttopstr.split("name\': \'")[1].split("\'")[0]

                # Checking artist not in my library
                for elem2 in uniqart:
                    if elem2 == namer:
                        x = 1
                if x == 0:

                    # Generating 'name - song titles'
                    relarttopstrsplt = relarttopstr.split("name\': \'")
                    for elem3 in relarttopstrsplt:
                        if elem3.split("\', \'")[1].split("\'")[0] != 'type':
                            if elem3.split("\', \'")[1].split("\'")[0] != 'release_date':
                                songname = elem3.split("\'")[0]
                                if songname != namer:
                                    if songname not in '{}(),':
                                        nameandsong = namer + " - " + songname
                                        if nameandsong not in tracklist:
                                            randn = random.randint(0, 5)
                                            if randn == 0:
                                                tracklist.append(nameandsong)
                                                print(nameandsong)
        except:
            None

Spotify_Get_Artist_Songs("jazzland.csv")
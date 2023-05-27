import urllib.request
import json
name=input()
with urllib.request.urlopen("https://api.tvmaze.com/search/shows?q="+name) as show:
    details = json.loads(show.read())
    #print(type(details))
    dict = details[0]
    url = dict["show"]["url"]
    print(url)
    show_name = dict["show"]["name"]
    language = dict["show"]["language"]
    started = dict["show"]["premiered"]
    ended = dict["show"]["ended"]
    officialSite = dict ["show"]["officialSite"]
    print(show_name)
    print("The show url is: ",url)
    print(language)
    print(started)
    print(ended)
    print(officialSite)
    
    

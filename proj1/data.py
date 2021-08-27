import requests
import json

API_KEY= '28678d0ad03244d192eee521c72705db'

def gettopheadlines():
    url='https://newsapi.org/v2/top-headlines'
    querystring={
        'apikey' : API_KEY,
        'country' : 'in'
    }
    responce=requests.get(url,params=querystring)
    data=responce.json()
    articles=data['articles']
    return articles
def getevery(search_keyword=None):
    if not search_keyword:
        return gettopheadlines()
    url='https://newsapi.org/v2/everything'
    querystring={
        'apikey' : API_KEY,
        'q' : search_keyword
    }
    responce=requests.get(url,params=querystring)
    data=responce.json()
    print(json.dumps(data,indent=4))
    articles=data['articles']
    return articles


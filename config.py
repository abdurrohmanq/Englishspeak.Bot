import requests
app_id = "674823af"
app_key = "2813b1c3f5f81ba0767ff077f6c84a73"
language = "en-gb"

def getdifinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res=r.json()
    if 'error' in res.keys():
      return False

    output={}
    senses=res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions=[]
    for sens in senses:
      definitions.append(f"{sens['definitions'][0]}")
    output['definitions']="\n".join(definitions)

    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
	    output['audio']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output

if __name__=='__main__':
	from pprint import pprint as print
	print(getdifinitions('Great Britain'))
	print(getdifinitions('america'))







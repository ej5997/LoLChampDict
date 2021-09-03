import urllib.request, json

"""
creates and returns a dictionary that maps each champion's id to its name

i.e: champDict[266] = Aatrox
     champDict[103] = Ahri
    
keys are ints (champion id) and values are strings (champion name)     
"""
def makeChampDict():
    # gets the latest version of datadragon available (ensures all champs are in dict)
    patches_URL = "https://ddragon.leagueoflegends.com/api/versions.json"
    with urllib.request.urlopen(patches_URL) as url:
        patch = json.loads(url.read().decode())[0]
    
    # creates the id->name pair dictionary
    champDict = {}
    URL = "http://ddragon.leagueoflegends.com/cdn/" + patch + "/data/en_US/champion.json"
    with urllib.request.urlopen(URL) as url:
        fullData = json.loads(url.read().decode())
        champData = fullData["data"]
        for key in champData:
            champName = champData[key]["name"]
            champId = int(champData[key]["key"])
            champDict[champId] = champName
    return champDict
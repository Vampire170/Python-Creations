import requests
import json
import webbrowser
print('Welcome to CMS')
webbrowser.open('https://cricketdata.org/')
key=input('Enter the key: ')
url = f'https://api.cricapi.com/v1/cricScore?apikey={key}'
r = requests.get(url)
wdict = json.loads(r.text)


for match in wdict["data"]:
    print("DateTime (GMT):", match["dateTimeGMT"])
    print("Match Type:", match["matchType"])
    print("Team 1:", match["t1"])
    print("Team 2:", match["t2"])
    print("Team 1 Score:", match["t1s"])
    print("Team 2 Score:", match["t2s"])
    print("Status:", match["status"])
    print("-" * 40) 
print('Made by Vampire with ❤️')
rt=input('Press Enter to exit')

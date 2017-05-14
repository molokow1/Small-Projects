#A Fun script that will copy a random cat fact to your clip board every 0.5 second
#Happy Spamming!
import requests
import json
from subprocess import check_call
import time
from msvcrt import getch


print("ENJOY YOUR CAT FACTS, PRESS ESC TO BREAK")
while(True):
    r = requests.get("http://catfacts-api.appspot.com/api/facts")
    result = r.json()
    fact = result['facts'][0]
    cmd = 'echo ' + fact.strip() +'|clip'
    check_call(cmd, shell=True)
    time.sleep(0.5)
    key = ord(getch())
    if key == 27:
        break

print("SEE YOU!")
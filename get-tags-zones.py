import requests
import json



response = requests.get(f"https://192.168.55.10/restapi/v9.1/Policies/SecurityRules?location=vsys&vsys=vsys1",verify=False, 
    headers={"X-PAN-KEY": "YOUR-API-KEY"
    }
)

tag       = "Transit"
from_zone = "Private"
to_zone   = "Public"

# convert json to Python object 
data = response.json()

#for loop to iterate through the tag variable and print the security rule that matches the tag
print(f"\n#### TAG NAME: {tag} ####\n")
for stuff in data['result']['entry']:
    for morestuff in stuff['tag']['member']:
        if (morestuff == tag):
            #print(morestuff)
            print(f"Security Rule Name with Tag \"{tag}\": {stuff['@name']}")

#for loop to iterate through the "from_zone" variable and print the security rule that matches that zone
print(f"\n#### SOURCE ZONE: {from_zone} ####\n")
for stuff in data['result']['entry']:
    for morestuff in stuff['from']['member']:
        if (morestuff == from_zone):
            #print(morestuff)
            print(f"Security Rule Name with source zone \"{from_zone}\": {stuff['@name']}")

#for loop to iterate through the "to_zone" variable and print the security rule that matches that zone
print(f"\n#### DEST ZONE: {to_zone} ####\n")
for stuff in data['result']['entry']:
    for morestuff in stuff['to']['member']:
        if (morestuff == to_zone):
            #print(morestuff)
            print(f"Security Rule Name with destination zone \"{to_zone}\": {stuff['@name']}")


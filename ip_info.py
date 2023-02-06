import requests
import pandas as pd

#ip Sort-out before the code runs
lines_seen = set() # holds lines already seen
outfile = open("/Users/ovin.gamage/Documents/Python Projects/IP Project/outfilename.txt", "w") 
for line in open("/Users/ovin.gamage/Documents/Python Projects/IP Project/iplist.txt", "r"): 
    if line not in lines_seen: 
        outfile.write(line)
        lines_seen.add(line)
outfile.close()

#code for open the ipfile (outfilename.txt) 
file = open("/Users/ovin.gamage/Documents/Python Projects/IP Project/outfilename.txt", "r")
x = file.readlines() 
y = []

def get_location():
    for each in x:
        response = requests.get(f'https://ipapi.co/{each.rstrip()}/json/', verify=False).json() #rstrip tp remove the /n
        location_data = {
            "ip": response.get("ip"),
            "city": response.get("city"),
            "region": response.get("region"),
            "country": response.get("country_name"),
            "organization" : response.get("org"),
        }
        y.append (location_data)
        print(y)
    df = pd.DataFrame(data=y)

    # convert into excel
    df.to_excel("list_output.xlsx", index=False) 
    print("Dictionary converted into excel...")

get_location()
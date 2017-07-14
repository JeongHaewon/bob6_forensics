import json

import pythonwhois

fout = open('url', 'rt')
lines = fout.readlines()
fout.close()

for line in lines:
    print line

    WHOIS_DATA = pythonwhois.net.get_whois_raw(line, with_server_list=False)
    print WHOIS_DATA

    WHOIS_JSON = json.JSONEncoder().encode({line:WHOIS_DATA})
  
    file = open("file.p","wb")
    file.write(WHOIS_JSON)
    file.close()
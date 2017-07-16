import json
import sys
import pythonwhois

argument = sys.argv [1]
fout = open(argument, 'rt')
lines = fout.readlines()
fout.close()

file = open("file.p","wb")

for line in lines:
    print line

    WHOIS_DATA = pythonwhois.net.get_whois_raw(line, with_server_list=False)
    print WHOIS_DATA

    WHOIS_JSON = json.JSONEncoder().encode({line:WHOIS_DATA})
 
    file.write(json.dumps(WHOIS_JSON))
    
file.close()

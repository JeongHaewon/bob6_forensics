import pythonwhois

data = pythonwhois.net.get_whois_raw("goodle.com", with_server_list=False)

print data[0]

import argparse # add args parsing

print data[Domain name] #read domains from a file


import json # json

whois_json = json.dumps(data) #parse whois output (json)

data2 = json.loads(whois_json)
fileobj = open ("whois_output",'wt') #store output as a file


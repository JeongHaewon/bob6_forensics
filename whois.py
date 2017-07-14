"""Getting whois data from website"""

import argparse # add args parsing
import json # json
import pythonwhois

data = pythonwhois.net.get_whois_raw( 'http://google.com', with_server_list=False)
print DATA[0]

parser = argparse.ArgumentParser(description='Hi')
parser .add_argument('--Domain', action='store', dtest='Domain')

output = parser.parse_args[data] #read domains from a file
print (output)


whois_json = json.dumps(data) #parse whois output (json)
data2 = json.loads(whois_json)

fileobj = open("whois_output", 'wt') #store output as a file
fileobj.write(data2)
fileobj.close()
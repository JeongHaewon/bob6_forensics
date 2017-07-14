"""Getting whois data from website"""

import argparse # add args parsing
import json # json
import pythonwhois

whois_data = pythonwhois.net.get_whois_raw( 'http://google.com', with_server_list=False)
print (whois_data)

parser = argparse.ArgumentParser(description='Hi')
parser .add_argument('--Domain', action='store', dtest='Domain')

whois_output = parser parse_args[whois_data] #read domains from a file
print (whois_output)


whois_json = json.dumps(whois_data) #parse whois output (json)
whois_data2 = json.loads(whois_json)

fileobj = open("whois_output", 'wt') #store output as a file
fileobj.write(whois_data2)
fileobj.close()

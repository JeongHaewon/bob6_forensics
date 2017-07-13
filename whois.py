import pythonwhois

data = pythonwhois.net.get_whois_raw("goodle.com", with_server_list=False)

print data[0]

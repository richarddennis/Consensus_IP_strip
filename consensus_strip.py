import re 
import urllib2

for line in urllib2.urlopen("http://http://86.59.21.38/tor/status-vote/current/consensus.txt"):
    print line
    ipAddress = re.findall(r"[0-9]+(?:\.[0-9]+){3}", line)
    print ipAddress

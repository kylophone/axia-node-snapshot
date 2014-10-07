import os, sys, telnetlib

tn = telnetlib.Telnet("10.27.37.121", "93")

tn.write("SRC\n")
sourceList = tn.read_until("END")
#tn.write("DST\n")
#destinationList = tn.read_until("END")
#tn.write("IP\n")
#networkList = tn.read_until("hostname")
#tn.write("VER\n")
#versionList = tn.read_until("END")

print networkList
print sourceList
print destinationList
#print versionList

tn.close()

#!/usr/bin/python

from factom import Factomd, FactomWalletd
import settings, time, re, os
factomd = Factomd()
walletd = FactomWalletd()

walletd.host = settings.WalletdHost
factomd.host = settings.FactomdHost

Extid1 = 'Test chain entries '
Extid2 = time.strftime("%Y-%m-%d %H:%M")
Extid3 = 'Chain creation  '
Content = 'Chain entries are dummy values'

print factomd.entry_credit_balance(settings.EntryCredits)
result = walletd.new_chain(factomd, [Extid1, Extid2, Extid3], Content, settings.EntryCredits)
print factomd.entry_credit_balance(settings.EntryCredits)
print result

if "chainid" in result:
  print "Setting CHAIN_ID = " + result["chainid"]
  
  file = open("CHAIN_ID.txt","w") 
  file.write(result["chainid"])
  file.close()
 
  print "http://red2.logicethos.com:8090/search?input=" + result["chainid"] + "&type=chainhead"
else:
  print "No chain created"

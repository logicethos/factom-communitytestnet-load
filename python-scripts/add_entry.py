#!/usr/bin/python

from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time, settings
factomd = Factomd()
walletd = FactomWalletd()

walletd.host = settings.WalletdHost
factomd.host = settings.FactomdHost

timeBetweenEntries = float(settings.TimeInterval)

if timeBetweenEntries < 2:
  timeBetweenEntries = 2

start=1701
end=9000

#####################################
## Open File containing prime numbers
## Store all values in primes array
#####################################
f = open("P-1000000.txt","r")
primes = []
for line in f:
    primes.append(line)


#####################################
## Set entry credit address to spend from
## Set chain ID to add entries to
## Set default values for Extid1 and 2
#####################################
entryCredit = settings.EntryCredits
chainID     = settings.ChainID
Extid1	    = 'PrimeNumbers.txt'
Extid2      = 'P-1000000.txt'

if not entryCredit:
  print "No Entry Credits address"
  exit()

if not chainID:
  print "No Chain ID set"
  exit()


## Write to Factom chain
while True:
  for item in primes[start:end]:
    print Extid1
    print Extid2
    Extid3=strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print Extid3
    Content = item
    print Content
    time.sleep(timeBetweenEntries)
    result = walletd.new_entry(factomd, chainID, [Extid1, Extid2, Extid3], Content, entryCredit)


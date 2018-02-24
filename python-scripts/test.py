import sys
sys.path.insert(0,'/home/bondiblues/.local/lib/python2.7/site-packages')
from time import gmtime, strftime
from factom import Factomd, FactomWalletd
import time
factomd = Factomd()
walletd = FactomWalletd()


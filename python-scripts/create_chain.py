from factom import Factomd, FactomWalletd
import settings, time
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
#print result

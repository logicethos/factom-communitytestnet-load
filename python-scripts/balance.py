from factom import Factomd, FactomWalletd
import settings
factomd = Factomd()
walletd = FactomWalletd()
walletd.host = factomd.host = settings.Host

print factomd.entry_credit_balance(settings.EntryCredits)

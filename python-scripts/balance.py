from factom import Factomd, FactomWalletd
import settings
factomd = Factomd()
walletd = FactomWalletd()

walletd.host = settings.WalletdHost
factomd.host = settings.FactomdHost

print factomd.entry_credit_balance(settings.EntryCredits)

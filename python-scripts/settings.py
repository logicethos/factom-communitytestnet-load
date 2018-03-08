import os

if 'FACTOMD_HOST' in os.environ:
    FactomdHost = os.environ['FACTOMD_HOST']
else:
    FactomdHost = "http://factomd_node:8088/v2"
    
if 'WALLETD_HOST' in os.environ:
    WalletdHost = os.environ['WALLETD_HOST']
else:
    WalletdHost = "http://factomd_node:8089"

    
EntryCredits = os.environ['ENTRYCREDITS']

if 'CHAIN_ID' in os.environ:
    ChainID = os.environ['CHAIN_ID']

if 'SECS' in os.environ:
    TimeInterval = os.environ['SECS']
else:
    TimeInterval=30

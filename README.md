# Community Testnet Load scripts


docker build -t test-load github.com/logicethos/factom-communitytestnet-load

docker run --rm -it \
	-e FACTOM_HOST="http://localhost:8088/v2"" \
	-e ENTRYCREDITS="EC......" \
	-e CHAIN_ID="" \
	test-load

CHAIN_ID (if known)

To create a new chain id:

python create_chain.py

Then to set it it:
export CHAIN_ID = <your new chain id>
# Community Testnet Load scripts


    docker build -t test-load github.com/logicethos/factom-communitytestnet-load

To run on federated server (note port 8089 must be exposed)

    docker run --rm -it \
            --net communitytestnet_factomd \
            -e ENTRYCREDITS="EC......" \
            -e CHAIN_ID="" \
            test-load

To run on external factomd and factomwalletd node

    docker run --rm -it \
            -e FACTOMD_HOST="http://localhost:8088/v2" \
            -e WALLETD_HOST="http://localhost:8089" \
            -e ENTRYCREDITS="EC......" \
            -e CHAIN_ID="" \
            test-load



Note leave CHAIN_ID empty if not yet created

To create a new chain id:

    ./create_chain.py

Then set your new chain id as an environment variable:

    export CLASSPATH=$(cat CHAIN_ID)


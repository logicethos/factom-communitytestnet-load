# Community Testnet Load scripts

**To Build**

    docker build -t test-load github.com/logicethos/factom-communitytestnet-load

Note, when running on a federated server, port 8089 must be "exposed" which it wasn't on the original version.
If your running on a remote or personal node, see options (below).

**To create a new Chain ID:**

    docker run --rm -it \
            --net communitytestnet_factomd \
            -e ENTRYCREDITS="EC......" \
            test-load create_chain.py

**To start writing test data:**

    docker run --rm -it \
            --net communitytestnet_factomd \
            -e ENTRYCREDITS="EC......" \
            -e CHAIN_ID="....." \
            test-load


**Optional network settings (remove --net communitytestnet_factomd):**

    -e FACTOMD_HOST="http://localhost:8088/v2" \
    -e WALLETD_HOST="http://localhost:8089" \

**Optional Time Interval between writes:**

    -e SECS="10"



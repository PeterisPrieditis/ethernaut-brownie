# ABI is stored here to reduce size of helpful_scripts.py
#
# We can get ABI in console by typing JSON.stringify(ethernaut.abi)

import json
from brownie import (
    Contract,
)

f = open(
    "./scripts/ethernaut_abi.json",
)
ETHERNAUT_ABI = json.load(f)

# brownie run scripts/abi.py
def main():
    print("testing console!!!")
    ethernautContract = Contract.from_abi(
        "ethernaut", "0xD991431D8b033ddCb84dAD257f4821E9d5b38C33", ETHERNAUT_ABI
    )
    print(ethernautContract.owner())

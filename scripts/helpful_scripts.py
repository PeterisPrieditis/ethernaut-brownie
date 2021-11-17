import types

from brownie import (
    network,
    accounts,
    config,
    Contract,
)


from scripts.abi import (
    ETHERNAUT_ABI,
)

ETHERNAUT_ADDRESS = "0xD991431D8b033ddCb84dAD257f4821E9d5b38C33"

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]


def get_account(index=None, id=None):
    if index:
        return accounts[index]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    if id:
        return accounts.load(id)
    return accounts.add(config["wallets"]["from_key"])


# brownie run scripts/helpful_scripts.py
def get_new_instance():
    contractLevel = "0x4E73b858fD5D7A5fc1c3455061dE52a53F35d966"

    print("--- getting new level instance ---")
    account = get_account()
    ethernautContract = Contract.from_abi("ethernaut", ETHERNAUT_ADDRESS, ETHERNAUT_ABI)

    tx = ethernautContract.createLevelInstance(contractLevel, {"from": account})
    tx.wait(1)
    event_items = tx.events["LevelInstanceCreatedLog"].items()
    # event_items example
    # (('player', '0x0dBAb356D341F5E6cFC3248F138e5e546f466543'), ('instance', '0xB42063Cb92E317E1EBB2838400F0C0d6fD2E559D'))
    instance_event = [event for event in event_items if event[0] == "instance"]
    instance_address = instance_event[0][1]
    print(instance_address)
    return instance_address


def main():
    get_new_instance()

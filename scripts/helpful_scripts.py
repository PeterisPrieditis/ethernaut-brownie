import json

from brownie import (
    network,
    accounts,
    config,
    Contract,
)

# main game contract address - ethernaut.address
# ETHERNAUT_ADDRESS = "0xD991431D8b033ddCb84dAD257f4821E9d5b38C33"
ETHERNAUT_ADDRESS = config["levels"]["ethernaut_address"]

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "rinkeby-fork",
    "binance-fork",
    "matic-fork",
]


def get_account(id=0):
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[id]
    return accounts.add(config["wallets"]["from_key_" + str(id)])


# brownie run scripts/helpful_scripts.py --network rinkeby-fork
def get_new_instance(level_contract_name="00_hello_ethernaut", instance_value_wei=0):
    # print("===--- Get new instance for level - " + level_contract_name)
    level_contract_address = config["levels"][level_contract_name]
    account = get_account()
    ethernaut_contract = get_contract_from_abi_json(
        "Ethernaut", ETHERNAUT_ADDRESS, "ethernaut_abi.json"
    )
    tx = ethernaut_contract.createLevelInstance(
        level_contract_address, {"from": account, "value": instance_value_wei}
    )
    tx.wait(1)
    # event_items should receive
    # (('player', '0x0dBAb356D341F5E6cFC3248F138e5e546f466543'), ('instance', '0xB42063Cb92E317E1EBB2838400F0C0d6fD2E559D'))
    event_items = tx.events["LevelInstanceCreatedLog"].items()
    instance_event = [event for event in event_items if event[0] == "instance"]
    instance_address = instance_event[0][1]
    # print("===--- Instance for level address - " + instance_address)
    return instance_address


# ABI is stored here to reduce size of helpful_scripts.py
# We can get ABI in console by typing -> JSON.stringify(ethernaut.abi) or JSON.stringify(contract.abi)
def get_contract_from_abi_json(contract_name, address, file_name):
    file = open(
        "./interfaces/" + file_name,
    )
    abi_json = json.load(file)
    contract = Contract.from_abi(contract_name, address, abi_json)
    return contract


def get_level_contract(level_name, interface_contract, instance_value_wei=0):
    instance_address = get_new_instance(level_name, instance_value_wei)
    level_contract = Contract.from_abi(
        interface_contract._name, instance_address, interface_contract.abi
    )
    return level_contract


def submit_instance(level_contract_address):
    # print("===--- Submit instance for level address - " + level_contract_address)
    account = get_account()
    ethernaut_contract = get_contract_from_abi_json(
        "Ethernaut", ETHERNAUT_ADDRESS, "ethernaut_abi.json"
    )
    # Added "Gas limit" because of level 18
    tx = ethernaut_contract.submitLevelInstance(
        level_contract_address, {"from": account, "allow_revert": True, "gas": 500000}
    )
    # print(tx.info())
    tx.wait(1)
    # There will be an error if LevelCompletedLog event did occure
    try:
        event_items = tx.events["LevelCompletedLog"].items()
    except:
        return False
    return True


def print_out_if_level_solved(level_solved, level_name):
    if level_solved:
        print("You have completed level -> " + level_name)
    else:
        print(f"Looks like you haven't cracked level {level_name} just yet!")


# brownie run scripts/helpful_scripts.py --network rinkeby-fork
# brownie run scripts/helpful_scripts.py --network rinkeby
def main():
    get_new_instance("00_hello_ethernaut")

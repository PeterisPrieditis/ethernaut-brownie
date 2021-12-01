from brownie import web3, GatekeeperTwo, GatekeeperTwoAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "14_gatekeeper_two"
INTERFACE_CONTRACT = GatekeeperTwo
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()
    gatekeepertwo_attack = GatekeeperTwoAttack.deploy(level_contract, {"from": account})


# brownie run scripts/_14_gatekeeper_two.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

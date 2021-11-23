LEVEL_NAME = "00_hello_ethernaut"
ABI_JSON_FILE_NAME = "lvl_00_hello_ethernaut_abi.json"

from scripts.helpful_scripts import (
    get_account,
    get_new_instance,
    submit_instance,
    get_contract_from_abi_json,
)


def get_level_contract():
    instance_address = get_new_instance(LEVEL_NAME)
    level_contract = get_contract_from_abi_json(
        "Instance", instance_address, ABI_JSON_FILE_NAME
    )
    return level_contract


def solve_level(level_contract):
    password = level_contract.password()
    tx = level_contract.authenticate(password, {"from": get_account()})
    tx.wait(1)


# brownie run scripts/_00_hello_ethernaut.py --network rinkeby-fork
def main():
    # account = get_account()
    # print("Balance -> " + str(account.balance()))
    level_contract = get_level_contract()
    # Contract info() function creates Namespace collision. Created stackoverflow question.
    # https://stackoverflow.com/questions/70021317/brownie-classmethod-contract-from-abi-creates-namespace-error-for-info-funct
    #
    # /home/peteris/.local/pipx/venvs/eth-brownie/lib/python3.8/site-packages/brownie/network/contract.py:794:
    # BrownieEnvironmentWarning: Namespace collision between contract function and brownie `Contract` class member: 'Instance.info'
    # The info function will not be available when interacting with Instance
    # replies = level_contract.info()
    print()
    print("level_contract.info1() -> " + level_contract.info1())
    print("level_contract.info2('hello') -> " + level_contract.info2("hello"))
    print("level_contract.infoNum() -> " + str(level_contract.infoNum()))
    print("level_contract.info42() -> " + level_contract.info42())
    print("level_contract.theMethodName() -> " + level_contract.theMethodName())
    print("level_contract.method7123949() -> " + level_contract.method7123949())
    print("level_contract.password() -> " + level_contract.password())
    print()
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    if level_solved:
        print("You have completed level -> " + LEVEL_NAME)
    else:
        print(f"Looks like you haven't cracked level {LEVEL_NAME} just yet!")
    return level_solved

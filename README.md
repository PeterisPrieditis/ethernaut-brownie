# Ethernaut solutions - brownie

This is a repo with Ethernaut solutions in [Brownie](https://eth-brownie.readthedocs.io/en/stable/) to [Ethernaut CTF](https://ethernaut.openzeppelin.com/). A great list with solutions from other people can be found at [Ethernaut Community Solutions](https://forum.openzeppelin.com/t/ethernaut-community-solutions/561).

I used:
- https://cmichel.io/ethernaut-solutions/
- https://forum.openzeppelin.com/t/ethernaut-community-solutions/561#nicole-zhu-series-3
- https://medium.com/@appsbylamby/ethernaut-24-puzzle-wallet-walkthrough-mastering-the-proxy-pattern-cc830dc364ce
- https://medium.com/@appsbylamby/ethernaut-25-motorbikewalkthrough-3e1feeee6a4c

## Prerequisites

Please install or have installed the following:

- [nodejs and npm](https://nodejs.org/en/download/)
- [python](https://www.python.org/downloads/)
## Installation

1. [Install Brownie](https://eth-brownie.readthedocs.io/en/stable/install.html). Here is a simple way to install brownie.


```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
# restart your terminal
pipx install eth-brownie
```
Or, if that doesn't work, via pip
```bash
pip install eth-brownie
```

2. Clone from source:
```bash
git clone https://github.com/PeterisPrieditis/ethernaut-brownie
cd ethernaut-brownie
```

3. Create environment variables file:
Copy file ".env_example" and rename it to ".env". Environment variables need:
- Infura project id in order to run local network fork
- Private key in order to solve chalange on the real Rinkeby network

## Forking Rinkeby

Ethernaut uses Rinkeby network and some solutions will need local fork. We can remove and add network configuration with commands:
```bash
brownie networks delete rinkeby-fork
brownie networks add development rinkeby-fork cmd=ganache-cli host=http://127.0.0.1 fork='https://rinkeby.infura.io/v3/$WEB3_INFURA_PROJECT_ID' accounts=10 mnemonic=brownie port=8545
```

#### Running solutions

It is necessary to read [solutions](https://github.com/PeterisPrieditis/ethernaut-brownie/tree/master/solutions) in order to solve challenge on the real Rinkeby network. All solutions can be run locally a local Rinkeby fork. An example on how to run specific solution on a local Rinkeby fork:
```bash
# fork rinkeby but run locally
brownie run scripts/_00_hello_ethernaut.py --network rinkeby-fork
```

#### Testing solutions

Tests can be run by:
```bash
# to run all tests locally
brownie test --network rinkeby
# to run a specific test locally
brownie test -k test_00_hello_ethernaut --network rinkeby
```

# Solutions

## 00 Hello Ethernaut

### Explanation

This is introduction chalange in order to get familiar how to play the game.

### Solution in console

To solve challange in browser console it is necessary to write:
```bash
    await contract.info()
    await contract.info1()
    await contract.info2("hello")
    await contract.infoNum()
    await contract.theMethodName()
    await contract.method7123949()
    let password = await contract.password()
    await contract.authenticate(password)
```

### Solution in Brownie

Solution uses abi file from interface folder and not solidity code because at start of challange solidity code is not yet visible. We can get abi from console with:
```bash
JSON.stringify(ethernaut.abi)
```

To solve chalange in Brownie:
```bash
# to solve on the real Rinkeby network:
brownie run scripts/_00_hello_ethernaut.py --network rinkeby-fork
# to solve on a local Rinkeby network fork:
brownie run scripts/_00_hello_ethernaut.py --network rinkeby
```

## 02 Fallback

### Explanation

Requires you to exploit a poorly implemented [Fallback Function](https://docs.soliditylang.org/en/v0.8.10/contracts.html?highlight=Fallback#fallback-function) to gain control of someone else’s smart contract..

### Solution in console

To solve challange in browser console it is necessary to write:
```bash
# Show contract abi in a table
console.table(contract.abi)
# Show contract owner
await contract.owner();
# Send one Wei to contribute()
await contract.contribute.sendTransaction({value: 1})
# We can see that "contributions[msg.sender] > 0" will give "true" value
console.table(await contract.contributions(player))
# Send one Wei to the fallback function to become owner
await contract.sendTransaction({value: 1});
# Our address
player;
# We can see that our address is set as an owner
await contract.owner();
# Reduce contract balance to 0
await contract.withdraw();
```

## 03 Coin Flip

This levels requires you to correctly guess the outcome of a coin flip, ten times in a row. It would be very hard to win level through console so it is necessary to deploy a custom contract simulating the same coin flipping logic and calling the real contract.

## 04 Telephone

This levels requires you to know difference between tx.origin vs msg.sender to claim ownership of the contract. If you send transaction from smart contract then tx.origin != msg.sender is true.
- msg.sender (address): sender of the message (current call)
- tx.origin (address): sender of the transaction (full call chain)
[Block and Transaction Properties](https://docs.soliditylang.org/en/develop/units-and-global-variables.html#block-and-transaction-properties)

## 05 Telephone

The goal of this level is to hack the basic token contract. You are given 20 tokens to start with and you will beat the level if you get additional tokens. Starting from [Solidity v0.8.0](https://docs.soliditylang.org/en/v0.8.10/080-breaking-changes.html#solidity-v0-8-0-breaking-changes) has revert on underflow and overflow however our contract uses v0.6 and doesn't have check for overflows and underflows. It is necessary to use second wallet in order to send tokens.

## 06 Delegation

Delegation contract forwards calls to Delegate contract by using delegatecall in fallback function. Delegatecall will use logic from Delegation contract however it will still use Delegation contract storage variables.

We can solve this also via console:
```bash
await sendTransaction({
  from: player,
  to: contract.address,
  data: web3.eth.abi.encodeFunctionSignature("pwn()")
});
```

## 07 Force

In solidity, for a contract to be able to receive ether, the function must be marked payable. However, there is no way to stop an attacker from sending ether to a contract by self destroying. Hence, it is important not to count on the invariant address(this).balance == 0 for any contract logic.

## 08 Vault

Password is private so other contracts are not allowed to read it. It is still possible to read password from storage variable.

We can solve this also via console:
```bash
# Get password from storage
const password = await web3.eth.getStorageAt(contract.address, 1)
# Transform password from bytes32 so we would be able to see it
web3.utils.hexToAscii(password)
# Unlock vault
await contract.unlock(password)
});
```

## 09 King

Contract below represents a very simple game: whoever sends it an amount of ether that is larger than the current prize becomes the new king. When you submit the instance back to the level, the level is going to reclaim kingship. You will beat the level if you can avoid such a self proclamation. It is necessary to write a contract that does not accept payments.

## 10 Re-entrancy

Contract has a re-entrancy vulnerability.

## 11 Elevator

It is necessary to implement a custom contract with a function "isLastFloor(uint256) external returns (bool)". With first call it would return "false" and second "true".

## 12 Privacy

It is necessary to read contract storage in order to complete the challenge.

We can solve this also via console:
```bash
# read from storage slot number 5
var slot_5 = await web3.eth.getStorageAt(contract.address, 5)
# unlock with first 16 bytes
await contract.unlock(slot_5.slice(0, 34))
});
```

## 13 Gatekeeper One

It is necessary to pass three modifier checks:
1) Requires msg.sender != tx.origin so transaction must go through smart contract.
2) Remaining gas must have specific amount.
3) It is neccessary to find _gateKey:
require(uint32(uint64(_gateKey)) == uint16(tx.origin)
=> says that _gateKey bytes #5,6 must be 00 and #7,8 will be last bytes from tx.origin
require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey))
=> says that _gateKey bytes #5,6 must be 00
require(uint32(uint64(_gateKey)) != uint64(_gateKey)
=> says that bytes #1-4 must have something filled somewhere

## 14 Gatekeeper Two

It is necessary to pass three modifier checks:
1) Requires msg.sender != tx.origin so transaction must go through smart contract.
2) Transaction must be forwarded through constructor because: During initialization code execution, EXTCODESIZE on the address should return zero, which is the length of the code of the account while CODESIZE should return the length of the initialization code.
3) It is neccessary to find _gateKey. To find the _gateKey it is necessary to know Bitwise Operations
A xor B = C
A xor C = B

## 15 Naught Coin

ERC20 Spec has two functions for token transfer and Naught Coin has implementation only for one of them. Naught Coin has implementation only for function transfer however it is still possible to transfer tokens with function transferFrom.

## 16 Preservation

It is necessary to exploit a contract by calling a delegatecall function. Solution of level 6, 8 and 12 will help to solve this chalange. LibraryContract modifies the state at slot 0. We can set attacker contract address with first setFirstTime call and with second call we will invoke attacker contract.

## 17 Recovery

Contract was created by a factory contract. We have access to the factory contract however child contract address is unknown. It is necessary to find child contract address and call destroy function.

Contract addresses are deterministic and are calculated by keccack256(address, nonce) where the address is the address of the contract (or ethereum address that created the transaction) and nonce is the number of contracts the spawning contract has created (or the transaction nonce, for regular transactions). There is a second way how to create contracts by using CREATE2 which generates a different address but this factory contract uses the standard one. 

## 18 MagicNumber

It is necessary to deploy a contract that returns 42 and contract can't be larger than 10 opcodes. Here is an explanation [how to get necessary opcodes](https://medium.com/coinmonks/ethernaut-lvl-19-magicnumber-walkthrough-how-to-deploy-contracts-using-raw-assembly-opcodes-c50edb0f71a2) 

## 19 Alien Codex

To complete the level it is necessary to understand [Layout of State Variables in Storage](https://docs.soliditylang.org/en/v0.4.25/miscellaneous.html#layout-of-state-variables-in-storage)

## 20 Denial

It is necessary to create a custom controct and set as partner contract. .call function is being used for transfer and doesn't have specified gas amount. Custom contract must use assert in order to consume all gas and fail transaction.

## 21 Shop

This level is similar to 11 Elevator. During first price() call it is necessary to return high value and during second call low value. It is a "view" function so calling contract can't change state but it is possible to monitor value of Shop(msg.sender).isSold()

## 22 Dex

Swap function gives the wrong price. Dex balance is decreasing afther each swap.
Initial balance:
Token1 - account balance: 10 dex balance: 100
Token2 - account balance: 10 dex balance: 100
Swap 1:
Token1 - account balance: 0 dex balance: 110
Token2 - account balance: 20 dex balance: 90
Swap 3:
Token1 - account balance: 24 dex balance: 86
Token2 - account balance: 0 dex balance: 110

## 23 Dex Two

Create custom ERC20 and add liquidity. Use unlimited custom token to drain DEX.

## 24 Puzzle Wallet

It is necessary to use storage collisions in order to solve this level:
1) Become owner of PuzzleWallet by calling PuzzleProxy.proposeNewAdmin().
2) We can add our address to white list because we are the PuzzleWallet owner.
3) Create multicall to drain wallet.
4) Use PuzzleWallet.setMaxBalance() to set PuzzleProxy.admin.

## 25 Motorbike

It is necessary to:
1) create custom contract with a selfdestruct() in a function.
2) upgrade old contract with the new custom contract.
3) call selfdestruct() function for the new implementation contract

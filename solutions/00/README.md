## Explanation

This is introduction chalange in order to get familiar how to play the game.

## Solution in console

During the game it is necessary to write in console:
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

To solve chalange in Brownie:
```bash
# to solve on the real Rinkeby network:
brownie run scripts/_00_hello_ethernaut.py --network rinkeby-fork
# to solve on a local Rinkeby network fork:
brownie run scripts/_00_hello_ethernaut.py --network rinkeby
```
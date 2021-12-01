# Ethernaut solutions - brownie

This is a repo with solutions in [Brownie](https://eth-brownie.readthedocs.io/en/stable/) to [Ethernaut CTF](https://ethernaut.openzeppelin.com/). In-depth explanations for each level are visible [solutions](https://github.com/PeterisPrieditis/ethernaut-brownie/tree/master/solutions) folder. A great list with solutions from other people can be found at [Ethernaut Community Solutions](https://forum.openzeppelin.com/t/ethernaut-community-solutions/561).

I was using:
https://cmichel.io/ethernaut-solutions/
https://forum.openzeppelin.com/t/ethernaut-community-solutions/561#nicole-zhu-series-3

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
from scripts._00_hello_ethernaut import test_level as test_00

# brownie test -k test_00_hello_ethernaut --network rinkeby-fork -s
# brownie test -k test_00_hello_ethernaut --network rinkeby -s
def test_00_hello_ethernaut():
    level_completed = test_00()
    assert level_completed is True

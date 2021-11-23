from scripts._00_hello_ethernaut import main as test_00
from scripts._01_fallback import main as test_01

# brownie test --network rinkeby-fork
# brownie test -k test_00_hello_ethernaut --network rinkeby-fork -s
# brownie test -k test_00_hello_ethernaut --network rinkeby -s
def test_00_hello_ethernaut():
    level_completed = test_00()
    assert level_completed is True


# brownie test -k test_01_fallback --network rinkeby-fork -s
def test_01_fallback():
    level_completed = test_01()
    assert level_completed is True

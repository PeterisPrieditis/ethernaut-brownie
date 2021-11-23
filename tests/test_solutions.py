from scripts._00_hello_ethernaut import main as test_00
from scripts._01_fallback import main as test_01
from scripts._02_fallout import main as test_02
from scripts._03_coin_flip import main as test_03
from scripts._04_telephone import main as test_04
from scripts._05_token import main as test_05

# brownie test --network rinkeby-fork -s
# brownie test --network rinkeby -s
# brownie test -k test_00_hello_ethernaut --network rinkeby-fork -s
# brownie test -k test_00_hello_ethernaut --network rinkeby -s
def test_00_hello_ethernaut():
    level_completed = test_00()
    assert level_completed is True


# brownie test -k test_01_fallback --network rinkeby-fork -s
def test_01_fallback():
    level_completed = test_01()
    assert level_completed is True


# brownie test -k test_02_fallout --network rinkeby-fork -s
def test_02_fallout():
    level_completed = test_02()
    assert level_completed is True


# brownie test -k test_03_coin_flip --network rinkeby-fork -s
def test_03_coin_flip():
    level_completed = test_03()
    assert level_completed is True


# brownie test -k test_04_telephone --network rinkeby-fork -s
def test_04_telephone():
    level_completed = test_04()
    assert level_completed is True


# brownie test -k test_05_token --network rinkeby-fork -s
def test_05_token():
    level_completed = test_05()
    assert level_completed is True

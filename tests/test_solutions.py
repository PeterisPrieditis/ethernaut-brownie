from scripts._00_hello_ethernaut import main as test_00
from scripts._01_fallback import main as test_01
from scripts._02_fallout import main as test_02
from scripts._03_coin_flip import main as test_03
from scripts._04_telephone import main as test_04
from scripts._05_token import main as test_05
from scripts._06_delegation import main as test_06
from scripts._07_force import main as test_07
from scripts._08_vault import main as test_08
from scripts._09_king import main as test_09
from scripts._10_re_entrancy import main as test_10
from scripts._11_elevator import main as test_11
from scripts._12_privacy import main as test_12
from scripts._13_gatekeeper_one import main as test_13
from scripts._14_gatekeeper_two import main as test_14
from scripts._15_naught_coin import main as test_15
from scripts._16_preservation import main as test_16
from scripts._17_recovery import main as test_17
from scripts._18_magic_number import main as test_18

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


# brownie test -k test_06_delegation --network rinkeby-fork -s
def test_06_delegation():
    level_completed = test_06()
    assert level_completed is True


# brownie test -k test_07_force --network rinkeby-fork -s
def test_07_force():
    level_completed = test_07()
    assert level_completed is True


# brownie test -k test_08_vault --network rinkeby-fork -s
def test_08_vault():
    level_completed = test_08()
    assert level_completed is True


# brownie test -k test_09_king --network rinkeby-fork -s
def test_09_king():
    level_completed = test_09()
    assert level_completed is True


# brownie test -k test_10_re_entrancy --network rinkeby-fork -s
def test_10_re_entrancy():
    level_completed = test_10()
    assert level_completed is True


# brownie test -k test_11_elevator --network rinkeby-fork -s
def test_11_elevator():
    level_completed = test_11()
    assert level_completed is True


# brownie test -k test_12_privacy --network rinkeby-fork -s
def test_12_privacy():
    level_completed = test_12()
    assert level_completed is True


# brownie test -k test_13_gatekeeper_one --network rinkeby-fork -s
def test_13_gatekeeper_one():
    level_completed = test_13()
    assert level_completed is True


# brownie test -k test_14_gatekeeper_two --network rinkeby-fork -s
def test_14_gatekeeper_two():
    level_completed = test_14()
    assert level_completed is True


# brownie test -k test_15_naught_coin --network rinkeby-fork -s
def test_15_naught_coin():
    level_completed = test_15()
    assert level_completed is True


# brownie test -k test_16_preservation --network rinkeby-fork -s
def test_16_preservation():
    level_completed = test_16()
    assert level_completed is True


# brownie test -k test_17_recovery --network rinkeby-fork -s
def test_17_recovery():
    level_completed = test_17()
    assert level_completed is True


# brownie test -k test_18_magic_number --network rinkeby-fork -s
def test_18_magic_number():
    level_completed = test_18()
    assert level_completed is True

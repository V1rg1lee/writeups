// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

interface IEldorion {
    function attack(uint256 damage) external;
}

contract AttackEldorion {
    IEldorion public target;

    constructor(address _target) {
        target = IEldorion(_target);
    }

    function attackThreeTimes() external {
        target.attack(100);
        target.attack(100);
        target.attack(100);
    }
}
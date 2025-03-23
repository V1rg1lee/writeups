# Challenge description

Welcome to the realms of Eldoria, adventurer. You’ve found yourself trapped in this mysterious digital domain, and the only way to escape is by overcoming the trials laid before you. But your journey has barely begun, and already an overwhelming obstacle stands in your path. Before you can even reach the nearest city, seeking allies and information, you must face Eldorion, a colossal beast with terrifying regenerative powers. This creature, known for its ""eternal resilience"" guards the only passage forward. It's clear: you must defeat Eldorion to continue your quest.

# Soluce

Here is the code of the blockchain:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract Eldorion {
    uint256 public health = 300;
    uint256 public lastAttackTimestamp;
    uint256 private constant MAX_HEALTH = 300;
    
    event EldorionDefeated(address slayer);
    
    modifier eternalResilience() {
        if (block.timestamp > lastAttackTimestamp) {
            health = MAX_HEALTH;
            lastAttackTimestamp = block.timestamp;
        }
        _;
    }
    
    function attack(uint256 damage) external eternalResilience {
        require(damage <= 100, "Mortals cannot strike harder than 100");
        require(health >= damage, "Overkill is wasteful");
        health -= damage;
        
        if (health == 0) {
            emit EldorionDefeated(msg.sender);
        }
    }

    function isDefeated() external view returns (bool) {
        return health == 0;
    }
}
```

and:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

import { Eldorion } from "./Eldorion.sol";

contract Setup {
    Eldorion public immutable TARGET;
    
    event DeployedTarget(address at);

    constructor() payable {
        TARGET = new Eldorion();
        emit DeployedTarget(address(TARGET));
    }

    function isSolved() public view returns (bool) {
        return TARGET.isDefeated();
    }
}
```

The contract `Eldorion` is a beast with 300 health points that regenerates to full health every time it is the timestamp of the block is greater than the last attack timestamp. The `attack` function allows to attack the beast with a damage between 0 and 100. If the health of the beast reaches 0, the `EldorionDefeated` event is emitted. The `isDefeated` function allows to check if the beast is defeated. 

In a normal transaction, each `attack` will be in a new block, so the beast will regenerate to full health every time. We need to attack the beast in the same block to defeat it.

We need to call the `attack` function three times in a single transaction. All the timestamps of the blocks must be the same. We can do this by using a contract that calls the `attack` function three times in the same transaction with 100 damage each time.

We will use npm to push the contract to the blockchain. First, we need to install the dependencies:

```sh
mkdir attack-eldorion
cd attack-eldorion
npm init -y
npm install --save-dev hardhat
npx hardhat
```

Choose `Create a JavaScript project`.

After that, remove all the dependencies in the `package.json`.
Then, we need to install all the packages:

```sh
npm install ethers@5.7.2 --save-dev
npm install --save-dev hardhat
npm install --save-dev @nomiclabs/hardhat-waffle@2.0.6 --legacy-peer-deps
npm install --save-dev "@nomiclabs/hardhat-ethers@^2.0.0" "@types/sinon-chai@^3.2.3" "ethereum-waffle@*"
```

Now we can add a new contract in the `contracts` folder, [AttackEldorion.sol](code/AttackEldorion.sol).

Now, we will add a script to deploy the contract in the `script` folder, [deploy.js](code/deploy.js).

Here is the result:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ npx hardhat run script/deploy.js --network custom
Deploying contracts with account: 0xAE3F1671fb8BDcc403A2a55Cdd1ad10C079763e3
AttackEldorion deployed to: 0xC39770fcda7efD80B2780F291A65e57734fa35e2
```

Now, we will add a script to call the `attackThreeTimes` function in the `script` folder, [attack.js](code/attack.js).

Here is the result:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ npx hardhat run script/attack.js --network custom
TTransaction sent: 0x611441f96acf548e0e315566e4442789a7978b7c12663bf105753be554653863
Attack successful
```

Now, we can ask the flag:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ nc 94.237.59.147 57172
1 - Get connection information
2 - Restart instance
3 - Get flag
Select action (enter number): 3
HTB{w0w_tr1pl3_hit_c0mbo_ggs_y0u_defe4ted_Eld0r10n}
```

So the flag is `HTB{w0w_tr1pl3_hit_c0mbo_ggs_y0u_defe4ted_Eld0r10n}`.
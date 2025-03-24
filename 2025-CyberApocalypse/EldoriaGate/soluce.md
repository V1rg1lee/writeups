# Challenge description

At long last, you stand before the EldoriaGate, the legendary portal, the culmination of your perilous journey. Your escape from this digital realm hinges upon passing this final, insurmountable barrier. Your fate rests upon the passage through these mythic gates. These are no mere gates of stone and steel. They are a living enchantment, a sentinel woven from ancient magic, judging all who dare approach. The Gate sees you, divining your worth, assigning your place within Eldoria's unyielding order. But you seek not a place within their order, but freedom beyond it. Become the Usurper. Defy the Gate's ancient magic. Pass through, yet leave no trace, no mark of your passing, no echo of your presence. Become the unseen, the unwritten, the legend whispered but never confirmed. Outwit the Gate. Become a phantom, a myth. Your escape, your destiny, awaits.

# Soluce

Here is the code of the blockchain:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

/***
    Malakar 1b:22-28, Tales from Eldoria - Eldoria Gates
  
    "In ages past, where Eldoria's glory shone,
     Ancient gates stand, where shadows turn to dust.
     Only the proven, with deeds and might,
     May join Eldoria's hallowed, guiding light.
     Through strict trials, and offerings made,
     Eldoria's glory, is thus displayed."
  
                   ELDORIA GATES
             *_   _   _   _   _   _ *
     ^       | `_' `-' `_' `-' `_' `|       ^
     |       |                      |       |
     |  (*)  |     .___________     |  \^/  |
     | _<#>_ |    //           \    | _(#)_ |
    o+o \ / \0    ||   =====   ||   0/ \ / (=)
     0'\ ^ /\/    ||           ||   \/\ ^ /`0
       /_^_\ |    ||    ---    ||   | /_^_\
       || || |    ||           ||   | || ||
       d|_|b_T____||___________||___T_d|_|b
  
***/

import { EldoriaGateKernel } from "./EldoriaGateKernel.sol";

contract EldoriaGate {
    EldoriaGateKernel public kernel;

    event VillagerEntered(address villager, uint id, bool authenticated, string[] roles);
    event UsurperDetected(address villager, uint id, string alertMessage);
    
    struct Villager {
        uint id;
        bool authenticated;
        uint8 roles;
    }

    constructor(bytes4 _secret) {
        kernel = new EldoriaGateKernel(_secret);
    }

    function enter(bytes4 passphrase) external payable {
        bool isAuthenticated = kernel.authenticate(msg.sender, passphrase);
        require(isAuthenticated, "Authentication failed");

        uint8 contribution = uint8(msg.value);        
        (uint villagerId, uint8 assignedRolesBitMask) = kernel.evaluateIdentity(msg.sender, contribution);
        string[] memory roles = getVillagerRoles(msg.sender);
        
        emit VillagerEntered(msg.sender, villagerId, isAuthenticated, roles);
    }

    function getVillagerRoles(address _villager) public view returns (string[] memory) {
        string[8] memory roleNames = [
            "SERF", 
            "PEASANT", 
            "ARTISAN", 
            "MERCHANT", 
            "KNIGHT", 
            "BARON", 
            "EARL", 
            "DUKE"
        ];

        (, , uint8 rolesBitMask) = kernel.villagers(_villager);

        uint8 count = 0;
        for (uint8 i = 0; i < 8; i++) {
            if ((rolesBitMask & (1 << i)) != 0) {
                count++;
            }
        }

        string[] memory foundRoles = new string[](count);
        uint8 index = 0;
        for (uint8 i = 0; i < 8; i++) {
            uint8 roleBit = uint8(1) << i; 
            if (kernel.hasRole(_villager, roleBit)) {
                foundRoles[index] = roleNames[i];
                index++;
            }
        }

        return foundRoles;
    }

    function checkUsurper(address _villager) external returns (bool) {
        (uint id, bool authenticated , uint8 rolesBitMask) = kernel.villagers(_villager);
        bool isUsurper = authenticated && (rolesBitMask == 0);
        emit UsurperDetected(
            _villager,
            id,
            "Intrusion to benefit from Eldoria, without society responsibilities, without suspicions, via gate breach."
        );
        return isUsurper;
    }
}
```

and:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

contract EldoriaGateKernel {
    bytes4 private eldoriaSecret;
    mapping(address => Villager) public villagers;
    address public frontend;

    uint8 public constant ROLE_SERF     = 1 << 0;
    uint8 public constant ROLE_PEASANT  = 1 << 1;
    uint8 public constant ROLE_ARTISAN  = 1 << 2;
    uint8 public constant ROLE_MERCHANT = 1 << 3;
    uint8 public constant ROLE_KNIGHT   = 1 << 4;
    uint8 public constant ROLE_BARON    = 1 << 5;
    uint8 public constant ROLE_EARL     = 1 << 6;
    uint8 public constant ROLE_DUKE     = 1 << 7;
    
    struct Villager {
        uint id;
        bool authenticated;
        uint8 roles;
    }

    constructor(bytes4 _secret) {
        eldoriaSecret = _secret;
        frontend = msg.sender;
    }

    modifier onlyFrontend() {
        assembly {
            if iszero(eq(caller(), sload(frontend.slot))) {
                revert(0, 0)
            }
        }
        _;
    }

    function authenticate(address _unknown, bytes4 _passphrase) external onlyFrontend returns (bool auth) {
        assembly {
            let secret := sload(eldoriaSecret.slot)            
            auth := eq(shr(224, _passphrase), secret)
            mstore(0x80, auth)
            
            mstore(0x00, _unknown)
            mstore(0x20, villagers.slot)
            let villagerSlot := keccak256(0x00, 0x40)
            
            let packed := sload(add(villagerSlot, 1))
            auth := mload(0x80)
            let newPacked := or(and(packed, not(0xff)), auth)
            sstore(add(villagerSlot, 1), newPacked)
        }
    }

    function evaluateIdentity(address _unknown, uint8 _contribution) external onlyFrontend returns (uint id, uint8 roles) {
        assembly {
            mstore(0x00, _unknown)
            mstore(0x20, villagers.slot)
            let villagerSlot := keccak256(0x00, 0x40)

            mstore(0x00, _unknown)
            id := keccak256(0x00, 0x20)
            sstore(villagerSlot, id)

            let storedPacked := sload(add(villagerSlot, 1))
            let storedAuth := and(storedPacked, 0xff)
            if iszero(storedAuth) { revert(0, 0) }

            let defaultRolesMask := ROLE_SERF
            roles := add(defaultRolesMask, _contribution)
            if lt(roles, defaultRolesMask) { revert(0, 0) }

            let packed := or(storedAuth, shl(8, roles))
            sstore(add(villagerSlot, 1), packed)
        }
    }

    function hasRole(address _villager, uint8 _role) external view returns (bool hasRoleFlag) {
        assembly {
            mstore(0x0, _villager)
            mstore(0x20, villagers.slot)
            let villagerSlot := keccak256(0x0, 0x40)
        
            let packed := sload(add(villagerSlot, 1))
            let roles := and(shr(8, packed), 0xff)
            hasRoleFlag := gt(and(roles, _role), 0)
        }
    }
}
```

and

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

import { EldoriaGate } from "./EldoriaGate.sol";

contract Setup {
    EldoriaGate public TARGET;
    address public player;

    event DeployedTarget(address at);

    constructor(bytes4 _secret, address _player) {
        TARGET = new EldoriaGate(_secret);
        player = _player;
        emit DeployedTarget(address(TARGET));
    }

    function isSolved() public returns (bool) {
        return TARGET.checkUsurper(player);
    }
}
```

The EldoriaGate contract uses a kernel (EldoriaGateKernel) that manages authentication and identity evaluation of “villagers”.

- Secret storage :

    - The secret (eldoriaSecret) is stored in slot 0 in clear text, and although it is declared as private, it can be accessed via storage read.

- Assembly authentication:

    - The authenticate function compares the passphrase supplied (after a 224-bit offset) with the secret.

- Contribution calculation and roles :

    - In evaluateIdentity, the assigned role is calculated by adding ROLE_SERF (value 1) to the contribution sent (converted to uint8).

    - By sending 255 wei, the contribution is 255, giving 1 + 255 = 256. As only the 8 least significant bits are considered, 256 becomes 0.

The attacker can :

1. Read the secret: By reading storage slot 0, extract the last 4 bytes (the real secret, in this case 0xdeadfade).
2. Authenticate correctly: use this secret as a passphrase to pass the authenticate check.
3. Manipulate roles: By sending exactly 255 wei when calling enter, the contribution forces the role calculation to 256, which becomes 0 after truncation on 8 bits.

    - Effect: The player is authenticated, but finds himself without any role assigned, which corresponds to the case of a usurper.

4. Validation: the checkUsurper function considers an authenticated user without a role to be a usurper, thus validating the challenge.

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

Now, we will add a script to exploit the vulnerability in the `script` folder, [attack.js](code/attack.js).

Here is the result:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ npx hardhat run script/attack3.js --network custom
Kernel address: 0xaB9E854215D37e5116B80080e18711F0c6F49075
Raw storage slot 0: 0x00000000000000000000000000000000000000000000000000000000deadfade
Extracted secret (passphrase): 0xdeadfade
Transaction sent: 0x87b8825cba54a8f67ad3e6064ed1b153716fab20a4b5e9011c00052a7fdad3b1
Transaction confirmed.
```

Now, we can ask the flag:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ nc 83.136.251.194 55363                                                                                                                                 
1 - Get connection information
2 - Restart instance
3 - Get flag
Select action (enter number): 3
HTB{unkn0wn_1ntrud3r_1nsid3_Eld0r1a_gates}
```

So the flag is `HTB{unkn0wn_1ntrud3r_1nsid3_Eld0r1a_gates}`.
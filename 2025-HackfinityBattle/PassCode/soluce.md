# Challenge description


We may have found a way to break into the DarkInject blockchain, exploiting a vulnerability in their system. This might be our only chance to stop them—for good.

Note: To start the target machine, click the Start Machine button:

Wait 1-2 minutes for the target machine to start. Once it has fully booted, the target machine IP will appear here:

10.10.94.98

You can then use the AttackBox or your own machine to attack the target machine's IP address.

```sh
root@attacker:~# RPC_URL=http://10.10.94.98:8545
root@attacker:~# API_URL=http://10.10.94.98
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

We can now use the `cast` tool to interact with the contract and read the storage slots.
Cast is a command-line tool provided by the Foundry framework, designed to quickly and easily interact with Ethereum smart contracts. It allows you to perform operations such as sending signed transactions, calling contract functions, and reading storage slots on the blockchain without writing additional code. Thanks to its concise and accessible syntax, cast is particularly popular in the context of security testing or Web3 CTFs, as it facilitates rapid analysis and direct manipulation of contracts.

We will read the contract storage to find the flag with the following command:

```sh
┌──(virgile㉿localhost)-[~]
└─$ for i in {0..30}; do
  echo "Slot $i:"
  cast storage $CONTRACT_ADDRESS $i --rpc-url $RPC_URL
done
Slot 0:
0x54484d7b776562335f6834636b316e675f636f64657d0000000000000000002c
Slot 1:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 2:
0x000000000000000000000000000000000000000000000000000000000000014d
Slot 3:
0x54686520636f646520697320333333000000000000000000000000000000001e
Slot 4:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 5:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 6:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 7:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 8:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 9:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 10:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 11:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 12:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 13:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 14:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 15:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 16:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 17:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 18:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 19:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 20:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 21:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 22:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 23:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 24:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 25:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 26:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 27:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 28:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 29:
0x0000000000000000000000000000000000000000000000000000000000000000
Slot 30:
0x0000000000000000000000000000000000000000000000000000000000000000
```

With this command, we can convert the hex values to ASCII and find the flag:

```sh
┌──(virgile㉿localhost)-[~]
└─$ echo "54484d7b776562335f6834636b316e675f636f64657d0000000000000000002c" | xxd -r -p
THM{web3_h4ck1ng_code},
```

So the flag is `THM{web3_h4ck1ng_code}`.
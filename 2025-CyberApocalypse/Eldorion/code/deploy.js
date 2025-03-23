async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with account:", deployer.address);
    
    // Replace this address with the address of the deployed Eldorion contract
    const targetAddress = "0xF9C353a092b2Af98a0aE28d3Abaa5D5F0C8fA66F";
    
    const AttackEldorion = await ethers.getContractFactory("AttackEldorion");
    
    const attackContract = await AttackEldorion.deploy(targetAddress);
    await attackContract.deployed();
    
    console.log("AttackEldorion deployed to:", attackContract.address);
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
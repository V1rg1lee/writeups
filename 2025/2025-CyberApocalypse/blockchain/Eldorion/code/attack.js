async function main() {
    // Replace this address with the address of the deployed contract
    const attackContractAddress = "0xC39770fcda7efD80B2780F291A65e57734fa35e2";
    
    const AttackEldorion = await ethers.getContractFactory("AttackEldorion");
    const attackContract = AttackEldorion.attach(attackContractAddress);
    
    const tx = await attackContract.attackThreeTimes();
    console.log("Transaction sent:", tx.hash);
    
    await tx.wait();
    console.log("Attack successful");
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error);
      process.exit(1);
    });
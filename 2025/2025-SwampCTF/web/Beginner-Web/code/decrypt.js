const CryptoJS = require('crypto-js');

function decryptFlag(ciphertext, password) {
    const decrypted = CryptoJS.AES.decrypt(ciphertext, password);
    return decrypted.toString(CryptoJS.enc.Utf8);
  }
  
  const key = 'flagPart2_3';
  
  const part2 = decryptFlag('U2FsdGVkX1/oCOrv2BF34XQbx7f34cYJ8aA71tr8cl8=', key);
  const part3 = decryptFlag('U2FsdGVkX197aFEtB5VUIBcswkWs4GiFPal6425rsTU=', key);
  
  console.log('Flag part 2:', part2);
  console.log('Flag part 3:', part3);
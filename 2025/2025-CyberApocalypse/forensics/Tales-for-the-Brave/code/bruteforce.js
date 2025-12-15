var CryptoJS = require('crypto-js');

const checkboxIDs = ["c1", "c2", "c3", "c4"];
const expectedHash = "18m0oThLAr5NfLP4hTycCGf0BIu0dG+P/1xvnW6O29g=";

function generateSequences(currentSequence, maxLength) {

  if (currentSequence.length > 0) {
    const joined = currentSequence.join("");
    const hash = CryptoJS.SHA256(joined).toString(CryptoJS.enc.Base64);
    if (hash === expectedHash) {
      console.log("Found :", currentSequence, "->", hash);
    }
  }

  if (currentSequence.length === maxLength) {
    return;
  }

  for (let i = 0; i < checkboxIDs.length; i++) {
    currentSequence.push(checkboxIDs[i]);
    generateSequences(currentSequence, maxLength);
    currentSequence.pop();
  }
}

generateSequences([], 10);
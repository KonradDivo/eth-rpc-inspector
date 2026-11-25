import os
from dotenv import load_dotenv
from web3 import Web3

# Charge les variables depuis le fichier .env
load_dotenv()

def check_blockchain_status() -> None:
    # 1. Connexion à un RPC : Alchemy
     #Vérifie la connexion RPC, diagnostique les erreurs et lit les soldes ETH + USDC.
    result = {"success": False, "error": "", "eth_balance": 0.0, "usdc_balance": 0.0}
    alchemy_env_var = "ALCHEMY_RPC_URL"
    rpc_url = os.getenv("ALCHEMY_RPC_URL", "")

    if not rpc_url:
        result["error"] = "La variable " + alchemy_env_var + " est absente du fichier .env."
    else:
        w3 = Web3(Web3.HTTPProvider(rpc_url))
        try:
            # Appel direct (getter JSON-RPC) : lève une exception détaillée en cas d'échec réseau/HTTP
            latest_block = w3.eth.block_number
            gas_price_gwei = w3.from_wei(w3.eth.gas_price, "gwei")

            # 2. Lire le solde USDC d'un portefeuille public (ex: Vitalik Buterin)
            # Ici on met l'adresse du smart contract USDC 
            usdc_contract_address = w3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
            # et là on met l'adresse publique du compte de Vitalik Buterin, le créateur de la blockchain Etherium
            target_wallet = w3.to_checksum_address("0xd8dA6BF26964aF9D7eEd9e03E53415D37aA96045")

            # 3. Lecture du solde natif en ETH (retourné en Wei)
            raw_eth_wei = w3.eth.get_balance(target_wallet)
            eth_balance = float(w3.from_wei(raw_eth_wei, "ether"))

            # 4. Lecture du solde du Smart Contract ERC-20 (USDC)
            minimal_erc20_abi = [
                {
                    "constant": True,
                    "inputs": [{"name": "_owner", "type": "address"}],
                    "name": "balanceOf",
                    "outputs": [{"name": "balance", "type": "uint256"}],
                    "type": "function"
                },
                {
                    "constant": True,
                    "inputs": [],
                    "name": "decimals",
                    "outputs": [{"name": "", "type": "uint8"}],
                    "type": "function"
                }
            ]
            usdc_contract = w3.eth.contract(address=usdc_contract_address, abi=minimal_erc20_abi)
            raw_usdc = usdc_contract.functions.balanceOf(target_wallet).call()
            decimals = usdc_contract.functions.decimals().call()
            usdc_balance = raw_usdc / (10 ** decimals)

            print("Connecté à Ethereum Mainnet via Alchemy !")
            print(f"Dernier bloc miné         : #{latest_block}")
            print(f"Prix actuel du Gas        : {gas_price_gwei:.2f} Gwei")
            print(f"Solde ETH du portefeuille : {eth_balance:,.4f} ETH")
            print(f"Solde USDC du portefeuille: {usdc_balance:,.2f} USDC")

            result["success"] = True
            result["eth_balance"] = eth_balance
            result["usdc_balance"] = usdc_balance

        except Exception as err:
            result["error"] = f"Échec de communication RPC : {type(err).__name__} -> {err}"
            print(result["error"])

    return result

if __name__ == "__main__":
    check_blockchain_status()


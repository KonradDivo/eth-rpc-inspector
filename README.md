# 🔍 eth-rpc-inspector

A lightweight, deterministic Python utility for verifying EVM JSON-RPC node connectivity, inspecting real-time Gas metrics, and querying both native ETH balances and ERC-20 Smart Contract states (USDC) without relying on heavy third-party indexers.

## Features
- **Explicit RPC Diagnostics:** Direct JSON-RPC calls with detailed exception catching (bypassing silent boolean connection checks).
- **Dual Balance Inspection:** Queries native Wei balances (`eth_getBalance`) alongside ERC-20 contract calls (`balanceOf`, `decimals`) via minimal ABIs.
- **Secure Configuration:** Environment-driven RPC endpoint management via `.env`.

## Prerequisites & Free RPC Setup
Public unauthenticated RPC nodes frequently rate-limit or block automated scripts. To run this tool reliably:
1. Create a free account at [Alchemy](https://alchemy.com) (select the **Free \$0/mo** tier).
2. Create a new App on **Ethereum Mainnet**.
3. Copy your full **Ethereum HTTPS Endpoint** (e.g., `https://alchemy.com`).

## Installation & Quickstart

```bash
# 1. Clone the repository
git clone https://github.com
cd eth-rpc-inspector

# 2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your RPC endpoint
cp .env.example .env
# Open .env and paste your full Alchemy Ethereum Endpoint into ALCHEMY_RPC_URL

# 5. Run the inspector
python3 test_connection.py
```

## Example Output
```text
Connecté à Ethereum Mainnet via Alchemy !
Dernier bloc miné         : #26488585
Prix actuel du Gas        : 0.18 Gwei
Solde ETH du portefeuille : 5.7996 ETH
Solde USDC du portefeuille: 41.19 USDC
```

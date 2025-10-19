from web3 import Web3

def connect_web3(rpc_url: str):
    """Connect to the Ethereum RPC endpoint."""
    w3 = Web3(Web3.HTTPProvider(rpc_url))
    if not w3.is_connected():
        raise ConnectionError("Unable to connect to Ethereum network. Check your RPC URL.")
    return w3

def get_eth_balance(w3: Web3, address: str):
    """Fetch ETH balance for a given address."""
    try:
        balance_wei = w3.eth.get_balance(address)
        balance_eth = w3.from_wei(balance_wei, 'ether')
        return float(balance_eth)
    except Exception as e:
        return f"Error: {str(e)}"

def check_wallets(rpc_url: str, addresses: list):
    """Check balances for multiple addresses."""
    results = []
    w3 = connect_web3(rpc_url)
    for addr in addresses:
        balance = get_eth_balance(w3, addr)
        results.append({
            "address": addr,
            "balance_eth": balance
        })
    return results

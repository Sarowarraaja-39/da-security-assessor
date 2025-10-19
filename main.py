import argparse
from da_security_assessor.utils import load_config
from da_security_assessor.wallet_checker import check_wallets
from da_security_assessor.contract_scanner import scan_contracts
from da_security_assessor.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description="Digital Assets Security Assessor")
    parser.add_argument("--config", required=True, help="Path to YAML configuration file")
    parser.add_argument("--output", default="reports/report.md", help="Path to output report file")
    args = parser.parse_args()

    config = load_config(args.config)
    rpc_url = config.get("eth_rpc")
    addresses = config.get("addresses", [])
    contracts = config.get("contracts", [])

    if not rpc_url:
        raise ValueError("Missing 'eth_rpc' in configuration file.")

    print("[INFO] Checking wallet balances...")
    wallet_results = check_wallets(rpc_url, addresses)

    print("[INFO] Scanning contracts...")
    contract_results = scan_contracts(contracts)

    print("[INFO] Generating report...")
    generate_report(wallet_results, contract_results, args.output)

if __name__ == "__main__":
    main()

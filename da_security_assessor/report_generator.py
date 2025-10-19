from jinja2 import Environment, FileSystemLoader
from datetime import datetime
from pathlib import Path

def generate_report(wallets, contracts, output_path="reports/report.md"):
    """Generate Markdown report using Jinja2 template."""
    env = Environment(loader=FileSystemLoader("templates"))
    template = env.get_template("template.md.j2")

    context = {
        "timestamp": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC"),
        "wallets": wallets,
        "contracts": contracts
    }

    output = template.render(context)
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(output)
    print(f"[INFO] Report generated at {output_path}")

import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_parser import AssetParser
from analyzers.risk_calculator import RiskCalculator
from analyzers.threat_model import ThreatModeler

console = Console()

def display_banner():
    banner = (
        "[bold cyan]AI-Security-Risk-Matrix-Auditor 🛡️📊[/bold cyan]\n"
        "[dim]Lesson 1: Cybersecurity Fundamentals & Risk Assessment Engine[/dim]"
    )
    console.print(Panel.fit(banner, border_style="cyan"))

def main():
    parser = argparse.ArgumentParser(description="AI & IT Asset Risk Matrix Auditor.")
    parser.add_argument("--inventory", help="Path to asset inventory JSON", default="data/asset_inventory.json")
    args = parser.parse_args()

    display_banner()

    assets = AssetParser.load_inventory(args.inventory)
    scored_assets = RiskCalculator.evaluate_inventory(assets)
    threat_profiled_assets = ThreatModeler.evaluate_threats(scored_assets)

    table = Table(title="[bold cyan]🔍 Day 3: Threat Modeling & AI Vulnerability Mapping[/bold cyan]", border_style="cyan")
    table.add_column("Asset ID", justify="center", style="dim")
    table.add_column("Asset Name", style="white")
    table.add_column("Primary Threat Vector", style="yellow")
    table.add_column("OWASP / LLM Top 10", style="magenta")
    table.add_column("Risk Score", justify="center", style="cyan")

    if not threat_profiled_assets:
        table.add_row("-", "No assets found.", "-", "-", "-")
    else:
        for a in threat_profiled_assets:
            table.add_row(
                a["asset_id"],
                a["name"],
                a["primary_threat"],
                a["owasp_mapping"],
                f"{a['risk_score']}/100"
            )

    console.print(table)
    console.print(f"\n[bold green]✔ Day 3 Complete:[/bold green] Profiled threat models for [bold cyan]{len(threat_profiled_assets)}[/bold cyan] assets.")

if __name__ == "__main__":
    main()

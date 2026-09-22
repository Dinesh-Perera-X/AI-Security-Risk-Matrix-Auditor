import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_parser import AssetParser
from analyzers.risk_calculator import RiskCalculator
from analyzers.threat_model import ThreatModeler
from generators.remediation import RemediationGenerator

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
    remediated_assets = RemediationGenerator.evaluate_remediations(threat_profiled_assets)

    table = Table(title="[bold green]🛠️ Day 4: Automated Remediation & Hardening Controls[/bold green]", border_style="green")
    table.add_column("Asset ID", justify="center", style="dim")
    table.add_column("Asset Name", style="white")
    table.add_column("Primary Threat", style="yellow")
    table.add_column("Recommended Security Controls", style="cyan")

    if not remediated_assets:
        table.add_row("-", "No assets found.", "-", "-")
    else:
        for a in remediated_assets:
            controls_str = "\n".join([f"• {c}" for c in a["remediation_steps"]])
            table.add_row(
                a["asset_id"],
                a["name"],
                a["primary_threat"],
                controls_str
            )

    console.print(table)
    console.print(f"\n[bold green]✔ Day 4 Complete:[/bold green] Generated hardening controls for [bold cyan]{len(remediated_assets)}[/bold cyan] assets.")

if __name__ == "__main__":
    main()

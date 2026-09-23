import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_parser import AssetParser
from analyzers.risk_calculator import RiskCalculator
from analyzers.threat_model import ThreatModeler
from generators.remediation import RemediationGenerator
from reports.reporter import Reporter

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

    # Generate Reports
    siem_path = Reporter.export_siem_json(remediated_assets)
    html_path = Reporter.export_html_dashboard(remediated_assets)

    table = Table(title="[bold magenta]🚀 Day 5: Complete Risk Audit & Report Exporter[/bold magenta]", border_style="magenta")
    table.add_column("Asset ID", justify="center", style="dim")
    table.add_column("Asset Name", style="white")
    table.add_column("Risk Score", justify="center", style="cyan")
    table.add_column("Rating", justify="center")

    for a in remediated_assets:
        rating = a["risk_rating"]
        rating_str = f"[bold red]{rating}[/bold red]" if rating in ["CRITICAL", "HIGH"] else f"[bold green]{rating}[/bold green]"
        table.add_row(a["asset_id"], a["name"], f"{a['risk_score']}/100", rating_str)

    console.print(table)
    console.print(f"\n[bold green]✔ Day 5 Complete:[/bold green] Successfully generated reports:")
    console.print(f"  • SIEM JSON Export: [cyan]{siem_path}[/cyan]")
    console.print(f"  • HTML Executive Dashboard: [cyan]{html_path}[/cyan]")

if __name__ == "__main__":
    main()

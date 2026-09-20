import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_parser import AssetParser
from analyzers.risk_calculator import RiskCalculator

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

    table = Table(title="[bold red]📊 Quantitative Risk Matrix & CIA Impact Score[/bold red]", border_style="red")
    table.add_column("Asset ID", justify="center", style="dim")
    table.add_column("Asset Name", style="white")
    table.add_column("Exposure", justify="center", style="yellow")
    table.add_column("Risk Score", justify="center", style="cyan")
    table.add_column("Risk Rating", justify="center")

    if not scored_assets:
        table.add_row("-", "No assets found.", "-", "-", "-")
    else:
        for a in scored_assets:
            rating = a["risk_rating"]
            if rating == "CRITICAL":
                rating_str = "[bold red]CRITICAL[/bold red]"
            elif rating == "HIGH":
                rating_str = "[bold yellow]HIGH[/bold yellow]"
            elif rating == "MEDIUM":
                rating_str = "[bold blue]MEDIUM[/bold blue]"
            else:
                rating_str = "[bold green]LOW[/bold green]"

            table.add_row(
                a["asset_id"],
                a["name"],
                a["exposure"],
                f"{a['risk_score']}/100",
                rating_str
            )

    console.print(table)
    console.print(f"\n[bold green]✔ Day 2 Complete:[/bold green] Evaluated quantitative risk scores for [bold cyan]{len(scored_assets)}[/bold cyan] assets.")

if __name__ == "__main__":
    main()

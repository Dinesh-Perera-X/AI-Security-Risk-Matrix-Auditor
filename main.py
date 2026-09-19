import argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from core.asset_parser import AssetParser

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

    table = Table(title="[bold cyan]📋 Ingested Asset Inventory & CIA Requirements[/bold cyan]", border_style="cyan")
    table.add_column("Asset ID", justify="center", style="dim")
    table.add_column("Asset Name", style="white")
    table.add_column("Type", style="magenta")
    table.add_column("Confidentiality", justify="center", style="yellow")
    table.add_column("Integrity", justify="center", style="yellow")
    table.add_column("Availability", justify="center", style="yellow")
    table.add_column("Exposure", justify="center", style="red")

    if not assets:
        table.add_row("-", "No assets found.", "-", "-", "-", "-", "-")
    else:
        for a in assets:
            table.add_row(
                a["asset_id"],
                a["name"],
                a["type"],
                a["confidentiality_req"],
                a["integrity_req"],
                a["availability_req"],
                a["exposure"]
            )

    console.print(table)
    console.print(f"\n[bold green]✔ Day 1 Complete:[/bold green] Ingested [bold cyan]{len(assets)}[/bold cyan] organizational assets.")

if __name__ == "__main__":
    main()

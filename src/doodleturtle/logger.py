from rich.console import Console

console = Console()


def initialize_logger() -> None:
    console.print("[green]Logger initialized[/green]")
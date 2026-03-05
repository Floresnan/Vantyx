import os
import typer
import requests
import httpx
from rich import print
from rich.pretty import Pretty
import csv
API = "http://127.0.0.1:8000"

app = typer.Typer(help="Vantyx CLI (vx)")


def api_base() -> str:
    return os.getenv("VANTYX_API", "http://127.0.0.1:8000")


@app.command()
def ping():
    """Testa comunicação com a API."""
    base = api_base()

    try:
        r = httpx.get(f"{base}/health", timeout=5)
        print(f"[green]OK[/green] {base}/health -> {r.status_code}")
        print(Pretty(r.json()))
    except Exception as e:
        print("[red]Erro ao conectar na API[/red]")
        print(str(e))


@app.command()
def ops():
    """Mostra painel diário."""
    base = api_base()

    try:
        r = httpx.get(f"{base}/ops/daily", timeout=10)
        print(f"[cyan]{base}/ops/daily[/cyan] -> {r.status_code}")
        print(Pretty(r.json()))
    except Exception as e:
        print("[red]Erro ao consultar ops[/red]")
        print(str(e))


@app.command("recent")
def recent_leads(limit: int = typer.Argument(10)):
    """Lista leads mais recentes."""
    base = api_base()
    url = f"{base}/leads/recent?limit={limit}"

    try:
        r = httpx.get(url, timeout=10)
        print(f"[cyan]{url}[/cyan] -> {r.status_code}")
        print(Pretty(r.json()))
    except Exception as e:
        print("[red]Falha ao buscar leads[/red]")
        print(str(e))


@app.command()
def top():
    r = requests.get(f"{API}/leads/top")

    print("\nTOP LEADS\n")

    for lead in r.json():
        print(
            f"{lead['nome']} | "
            f"interesse {lead['interesse']} | "
            f"urgencia {lead['urgencia']} | "
            f"score {lead['score']}"
        )

@app.command("import-a6")
def import_a6(csv_path: str):
    """
    Importa leads do CSV A6 para o sistema.
    """
    API = "http://127.0.0.1:8000"

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            payload = {
                "nome": row.get("nome", ""),
                "telefone": row.get("telefone", ""),
                "etapa": row.get("etapa", "Novo"),
                "interesse": int(row.get("interesse", 3)),
                "urgencia": int(row.get("urgencia", 3)),
                "origem": "a6"
            }

            r = httpx.post(f"{API}/leads", json=payload)

            if r.status_code == 200:
                print(f"✓ Lead importado: {payload['nome']}")
            else:
                print(f"Erro ao importar {payload['nome']} -> {r.text}")


if __name__ == "__main__":
    app()

@app.command()
def next():
    """Mostra o próximo lead para contato"""
    r = requests.get(f"{API}/leads/top")
    data = r.json()

    if not data:
        print("Nenhum lead encontrado")
        return

    lead = data[0]

    print("\nPRÓXIMO LEAD PARA LIGAR\n")
    print(f"Nome: {lead['nome']}")
    print(f"Telefone: {lead['telefone']}")
    print(f"Score: {lead['score']}")
    print()


@app.command()
def pipeline():
    """Mostra funil de vendas"""
    r = requests.get(f"{API}/leads/recent?limit=50")
    data = r.json()

    etapas = {}

    for lead in data:
        etapa = lead.get("etapa", "novo")
        etapas[etapa] = etapas.get(etapa, 0) + 1

    print("\nPIPELINE\n")

    for etapa, total in etapas.items():
        print(f"{etapa}: {total}")


@app.command()
def score():
    """Recalcula score de leads"""
    r = requests.get(f"{API}/leads/top")
    data = r.json()

    print("\nSCORES\n")

    for lead in data:
        print(
            f"{lead['nome']} → score {lead['score']} "
            f"(interesse {lead['interesse']} + urgencia {lead['urgencia']})"
        )

import os
import typer
import httpx
from rich import print
from rich.pretty import Pretty

app = typer.Typer(help="Vantyx CLI (vx)")


def api_base() -> str:
    return os.getenv("VANTYX_API", "http://127.0.0.1:8000")


@app.command()
def ping():
    """Testa comunicação com a API."""
    base = api_base()
    r = httpx.get(f"{base}/health", timeout=5)
    print(f"[green]OK[/green] {base}/health -> {r.status_code}")
    print(Pretty(r.json()))


@app.command()
def ops():
    """Mostra painel diário."""
    base = api_base()
    r = httpx.get(f"{base}/ops/daily", timeout=10)
    print(f"[cyan]{base}/ops/daily[/cyan] -> {r.status_code}")
    print(Pretty(r.json()))


@app.command("top")
def top(
    min_score: int = typer.Option(10, "--min-score", help="Score mínimo (ignorando se --no-score-filter)"),
    limit: int = typer.Option(10, "--limit", help="Quantidade máxima"),
    phone_only: bool = typer.Option(False, "--phone-only", help="Mostra apenas leads com telefone"),
    no_score_filter: bool = typer.Option(False, "--no-score-filter", help="Não filtra por score"),
):
    """Mostra os melhores leads (com filtros separados)."""
    base = api_base()
    url = f"{base}/ops/daily"
    try:
        r = httpx.get(url, timeout=10)
        print(f"[cyan]{url}[/cyan] -> {r.status_code}")
        data = r.json()
    except Exception as e:
        print(f"[red]Falha[/red] ao chamar {url}")
        print(str(e))
        raise typer.Exit(code=1)

    leads = data.get("top_leads", []) or []

    selected = []
    for l in leads:
        if phone_only and not l.get("telefone"):
            continue
        if not no_score_filter and (l.get("score") or 0) < min_score:
            continue
        selected.append(l)

    selected = selected[:limit]

    print(f"[bold]TOP[/bold] (min_score={min_score}, limit={limit}, phone_only={phone_only}, no_score_filter={no_score_filter})")
    print(Pretty(selected))

@app.command("import-a6")
def import_a6(
    path: str = typer.Argument(...),
    limit: int = typer.Option(0, "--limit"),
):
    """Importa leads_a6.csv sem duplicar."""
    import csv
    import hashlib

    base = api_base()
    url = f"{base}/leads/upsert"
    p = os.path.expanduser(path)

    ok = 0
    fail = 0

    def to_int(v):
        if not v:
            return None
        try:
            return int(float(str(v).strip()))
        except:
            return None

    def to_float(v):
        if not v:
            return None
        try:
            s = str(v).strip().replace(".", "").replace(",", ".")
            return float(s)
        except:
            return None

    with open(p, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for i, row in enumerate(reader, start=1):
            if limit and i > limit:
                break

            nome = (row.get("nome") or "").strip() or None
            origem = (row.get("origem") or "").strip() or "a6"
            perfil = (row.get("perfil") or "").strip() or None
            etapa = (row.get("etapa") or "").strip() or None

            interesse = to_int(row.get("interesse"))
            urgencia = to_int(row.get("urgencia"))
            budget = to_float(row.get("budget"))

            ultimo_contato = (row.get("ultimo_contato") or "").strip() or None

            payload = {
                "nome": nome,
                "origem": origem,
                "perfil": perfil,
                "budget": budget,
                "etapa": etapa,
                "interesse": interesse,
                "urgencia": urgencia,
                "ultimo_contato": ultimo_contato,
                "raw": {"a6_csv": row},
            }

            key_src = "|".join([
                str(nome or ""),
                str(origem or ""),
                str(perfil or ""),
                str(budget or ""),
                str(etapa or ""),
                str(interesse or ""),
                str(urgencia or ""),
                str(ultimo_contato or ""),
            ])

            payload["meta_leadgen_id"] = "a6:" + hashlib.sha1(
                key_src.encode("utf-8")
            ).hexdigest()

            try:
                r = httpx.post(url, json=payload, timeout=15)
                if r.status_code >= 300:
                    fail += 1
                else:
                    ok += 1
            except Exception:
                fail += 1

@app.command("recent")
def recent_leads(limit: int = typer.Argument(10, help="Quantidade de leads para listar")):
    """Lista leads mais recentes (sem filtro de score)."""
    base = api_base()
    url = f"{base}/leads/recent?limit={limit}"
    try:
        r = httpx.get(url, timeout=10)
        print(f"[cyan]{url}[/cyan] -> {r.status_code}")
        print(Pretty(r.json()))
    except Exception as e:
        print(f"[red]Falha[/red] ao chamar {url}")
        print(str(e))
        raise typer.Exit(code=1)

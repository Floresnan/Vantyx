@app.command()
def leads():
    import sqlite3
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    SELECT nome, telefone, interesse, urgencia, etapa
    FROM leads
    ORDER BY created_at DESC
    """)

    rows = cur.fetchall()

    print("\n📋 LEADS CADASTRADOS\n")

    for r in rows:
        print(f"{r[0]} | {r[1]} | Interesse:{r[2]} | Urgência:{r[3]} | Etapa:{r[4]}")

import os
from openai import OpenAI


def ask_ai(user_request: str, context: str) -> str:
    """
    Faz uma pergunta para a IA, incluindo um contexto curto do projeto.
    Retorna texto pronto para você copiar/colar.
    """

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return (
            "ERRO: OPENAI_API_KEY não está definido.\n\n"
            "No terminal, rode:\n"
            'export OPENAI_API_KEY="SUA_CHAVE_AQUI"\n'
        )

    try:
        client = OpenAI(api_key=api_key)

        system = (
            "Você é um assistente técnico. O usuário é iniciante.\n"
            "Responda SEM jargão, com passos numerados, e sempre inclua comandos de terminal.\n"
            "Quando sugerir código, forneça blocos completos para copiar/colar.\n"
            "Não peça para o usuário adivinhar caminhos: cite os caminhos exatos.\n"
        )

        prompt = f"""
CONTEXTO DO PROJETO (resumo):
{context}

PEDIDO DO USUÁRIO:
{user_request}

SAÍDA ESPERADA:
1) Explique o que será feito e por quê (bem curto).
2) Passo a passo (comandos).
3) Se houver mudanças de código, mostre o conteúdo completo dos arquivos ou trechos bem claros.
4) Mostre como testar com curl.
"""

        resp = client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {"role": "system", "content": system},
                {"role": "user", "content": prompt},
            ],
        )

        text = getattr(resp, "output_text", None)

        if not text:
            return "IA respondeu, mas veio vazio."

        return text

    except Exception as e:
        return f"ERRO ao chamar OpenAI: {type(e).__name__}: {e}"

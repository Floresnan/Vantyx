from datetime import date

ETAPA_BONUS = {
    "Proposta":      4,
    "Visita":        3,
    "Reunião Feita": 2,
    "Agendado":      2,
    "Qualificado":   1,
    "Contato feito": 1,
    "Novo Lead":     0,
    "Fechado":       0,
    "Perdido":      -5,
}


def calcular_score(lead: dict) -> int:
    score = 0

    score += int(lead.get("interesse") or 0)
    score += int(lead.get("urgencia") or 0)

    if (lead.get("renda") or 0) >= 20000:
        score += 2
    if (lead.get("entrada") or 0) >= 200000:
        score += 2

    etapa = lead.get("etapa") or ""
    score += ETAPA_BONUS.get(etapa, 0)

    ultimo_contato = lead.get("ultimo_contato")
    if ultimo_contato:
        if isinstance(ultimo_contato, str):
            try:
                ultimo_contato = date.fromisoformat(ultimo_contato[:10])
            except Exception:
                ultimo_contato = None
        if ultimo_contato:
            dias = (date.today() - ultimo_contato).days
            if dias <= 3:
                score += 3
            elif dias <= 7:
                score += 2
            elif dias <= 14:
                score += 1

    return score


def classificar_tier(score: int) -> str:
    if score >= 12:
        return "altissima"
    elif score >= 9:
        return "alta"
    elif score >= 6:
        return "media"
    else:
        return "baixa"

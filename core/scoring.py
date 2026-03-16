def calcular_score(lead):

    score = 0

    if "interesse" in lead:
        score += int(lead["interesse"])

    if "urgencia" in lead:
        score += int(lead["urgencia"])

    if "renda" in lead and lead["renda"] >= 20000:
        score += 2

    if "entrada" in lead and lead["entrada"] >= 200000:
        score += 2

    return score


def classificar_probabilidade(score):

    if score >= 12:
        return "altissima"

    elif score >= 9:
        return "alta"

    elif score >= 6:
        return "media"

    else:
        return "baixa"


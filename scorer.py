def calculate_health_score(issues: list) -> dict:
    score = 100

    severity_penalty = {
        "high": 20,
        "medium": 10,
        "low": 5
    }

    for issue in issues:
        score -= severity_penalty.get(issue["severity"], 0)

    # Keep score within bounds
    score = max(score, 0)

    if score >= 80:
        label = "Healthy"
    elif score >= 50:
        label = "Warning"
    else:
        label = "Critical"

    return {
        "score": score,
        "label": label
    }

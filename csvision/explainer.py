def generate_explanation(issues: list, health: dict) -> str:
    if not issues:
        return "The dataset shows no major quality issues and is ready for analysis."

    issue_types = set(issue["issue"] for issue in issues)

    explanation_parts = []

    if "Missing Values" in issue_types:
        explanation_parts.append("missing values")

    if "Invalid Range" in issue_types:
        explanation_parts.append("unrealistic or invalid values")

    if "High Cardinality" in issue_types:
        explanation_parts.append("high-cardinality categorical columns")

    if "Constant Column" in issue_types:
        explanation_parts.append("constant columns with no variance")

    explanation = "This dataset contains " + ", ".join(explanation_parts) + "."

    if health["label"] == "Warning":
        explanation += " Data cleaning is recommended before further use."
    elif health["label"] == "Critical":
        explanation += " Significant data cleaning is required before analysis or modeling."

    return explanation

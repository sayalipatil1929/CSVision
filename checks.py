def run_quality_checks(profile: dict) -> list:
    issues = []
    rows = profile["rows"]

    for column, stats in profile["column_profiles"].items():

        # 1️⃣ Missing values
        if stats["null_percentage"] > 0:
            issues.append({
                "column": column,
                "issue": "Missing Values",
                "severity": "medium",
                "details": f"{stats['null_percentage']}% values are missing"
            })

        # 2️⃣ Invalid ranges (rule-based example)
        if column.lower() == "age" and "max" in stats and stats["max"] > 120:
            issues.append({
                "column": column,
                "issue": "Invalid Range",
                "severity": "high",
                "details": f"Maximum age {stats['max']} is unrealistic"
            })

        # 3️⃣ Constant column (zero variance)
        if "std" in stats and stats["std"] == 0:
            issues.append({
                "column": column,
                "issue": "Constant Column",
                "severity": "low",
                "details": "All values are identical"
            })

        # 4️⃣ High cardinality categorical column
        if stats["dtype"] == "str" and stats["unique_count"] > 0.9 * rows:
            issues.append({
                "column": column,
                "issue": "High Cardinality",
                "severity": "low",
                "details": "Most values are unique"
            })

    return issues

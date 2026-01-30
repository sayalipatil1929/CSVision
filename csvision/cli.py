import sys
import json
import pandas as pd
from pathlib import Path

from profiler import profile_dataframe
from checks import run_quality_checks
from scorer import calculate_health_score
from explainer import generate_explanation


# ---------- Safe CSV Loader ----------
def load_csv_safe(path):
    try:
        return pd.read_csv(path, encoding="utf-8")
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")


# ---------- Report Builder ----------
def build_report(profile, issues, health, explanation):
    lines = []

    lines.append("CSVision – Dataset Profile\n")
    lines.append(json.dumps(profile, indent=2))

    lines.append("\n\nCSVision – Data Quality Issues\n")
    if not issues:
        lines.append("No major data quality issues detected ✅")
    else:
        for issue in issues:
            lines.append(
                f"- [{issue['severity'].upper()}] "
                f"{issue['column']}: {issue['issue']} -> {issue['details']}"
            )

    lines.append("\n\nCSVision – Dataset Health\n")
    lines.append(f"Health Score: {health['score']} / 100")
    lines.append(f"Status: {health['label']}")

    lines.append("\n\nCSVision – Summary\n")
    lines.append(explanation)

    return "\n".join(lines)


# ---------- Main CLI ----------
def main():
    if len(sys.argv) < 2:
        print("Usage: python csvision/cli.py <csv_path> [--json] [--export]")
        sys.exit(1)

    csv_path = sys.argv[1]
    export_txt = "--export" in sys.argv
    json_output = "--json" in sys.argv

    if not Path(csv_path).exists():
        print("❌ File not found:", csv_path)
        sys.exit(1)

    # Load CSV safely
    df = load_csv_safe(csv_path)

    # 1️⃣ Profile dataset
    profile = profile_dataframe(df)

    # 2️⃣ Run quality checks
    issues = run_quality_checks(profile)

    # 3️⃣ Calculate health score
    health = calculate_health_score(issues)

    # 4️⃣ Generate explanation
    explanation = generate_explanation(issues, health)

    # Build full report
    report = build_report(profile, issues, health, explanation)

    # ----- Output -----
    if json_output:
        print(json.dumps({
            "profile": profile,
            "issues": issues,
            "health": health,
            "summary": explanation
        }, indent=2))
    else:
        print(report)

    # ----- Export -----
    if export_txt:
        output_file = Path(csv_path).stem + "_csvision_report.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n📄 Report exported to: {output_file}")


if __name__ == "__main__":
    main()

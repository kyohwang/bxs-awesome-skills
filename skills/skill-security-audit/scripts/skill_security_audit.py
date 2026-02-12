#!/usr/bin/env python3
import os, re, json, argparse, pathlib, datetime


DEFAULT_RULES = pathlib.Path(__file__).resolve().parents[1] / "references" / "security-rules.json"

TEXT_EXT = {".md", ".txt", ".py", ".sh", ".ts", ".js", ".json", ".yaml", ".yml"}


def load_rules(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def iter_files(root):
    for p in pathlib.Path(root).rglob("*"):
        if p.is_file() and p.suffix.lower() in TEXT_EXT:
            yield p


def scan_file(file_path, rules, rel_root):
    findings = []
    text = file_path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    rel = str(file_path.relative_to(rel_root))

    def apply(rule_set, severity):
        for r in rule_set:
            rgx = re.compile(r["pattern"])
            for i, line in enumerate(lines, start=1):
                if rgx.search(line):
                    findings.append({
                        "rule_id": r["id"],
                        "severity": severity,
                        "file_path": rel,
                        "line_start": i,
                        "line_end": i,
                        "evidence_snippet": line[:240],
                        "fix_hint": r.get("reason", "Review and remove risky pattern")
                    })
    apply(rules.get("block", []), "BLOCK")
    apply(rules.get("review", []), "REVIEW")
    return findings


def score(findings):
    block = sum(1 for f in findings if f["severity"] == "BLOCK")
    review = sum(1 for f in findings if f["severity"] == "REVIEW")
    s = 100 - block * 40 - review * 8
    return max(0, s)


def verdict(findings, s):
    if any(f["severity"] == "BLOCK" for f in findings):
        return "BLOCK"
    if s >= 85:
        return "PASS"
    return "REVIEW"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target", help="Skill directory or proposal directory")
    ap.add_argument("--rules", default=str(DEFAULT_RULES))
    ap.add_argument("--out", default="SECURITY-REPORT.generated.json")
    args = ap.parse_args()

    rules = load_rules(args.rules)
    target = pathlib.Path(args.target).resolve()

    findings = []
    for f in iter_files(target):
        findings.extend(scan_file(f, rules, target))

    s = score(findings)
    v = verdict(findings, s)
    report = {
        "generated_at": datetime.datetime.utcnow().isoformat() + "Z",
        "target": str(target),
        "verdict": v,
        "score": s,
        "high_risk_count": sum(1 for x in findings if x["severity"] == "BLOCK"),
        "review_count": sum(1 for x in findings if x["severity"] == "REVIEW"),
        "findings": findings[:200]
    }

    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print(json.dumps({"verdict": v, "score": s, "out": args.out}, ensure_ascii=False))


if __name__ == "__main__":
    main()

# clawhub Test Report

## Install test
Installed by copying `skills/clawhub` into isolated path `/tmp/clawhub-skill-test/.claude/skills/clawhub`.

```text
total 256
drwxr-x--x 2 root root 4096 Feb 24 22:31 .
drwxr-xr-x 3 root root 4096 Feb 24 22:31 ..
-rw-r----- 1 root root 1613 Feb 24 22:31 SKILL.md
-rw-r----- 1 root root  661 Feb 24 22:31 skill.json
```

## Minimal runnable example
Command:

```bash
clawhub search "weather" --limit 3
```

Result: success, returned 3 records (see `proposals/clawhub/minimal-run.out`).

## Key boundary checks
1) Empty query:

```bash
clawhub search "" --limit 1
```

Expected/actual: fail fast with `Error: Query required`.

2) Non-existent package install:

```bash
clawhub install definitely-not-existing-skill-xyz --version 0.0.1
```

Expected/actual: fail with `Skill not found`.

## Conclusion
- Install: PASS
- Minimal runnable: PASS
- Boundary checks: PASS
- Overall usability: PASS

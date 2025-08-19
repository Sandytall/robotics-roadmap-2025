#!/usr/bin/env python3
import sys, datetime, pathlib, textwrap
def main(n: int, date: str, title: str, task: str):
    ROOT = pathlib.Path(__file__).resolve().parents[1]
    path = ROOT / "logs" / f"Day{n:02d}.md"
    content = textwrap.dedent(f"""
    # Day {n:02d} – {date}
    **Topic:** {title}
    **Task:** {task}

    ## ✅ Checklist (tiny steps)
    - [ ] Read 20–30m
    - [ ] Code minimal example
    - [ ] Test + screenshot
    - [ ] Write 3 learnings
    - [ ] Commit
    """)
    path.write_text(content, encoding="utf-8")
    print(f"created {path}")
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("usage: new_day.py <N> <DATE> <TITLE> <TASK>")
        sys.exit(1)
    main(int(sys.argv[1]), sys.argv[2], sys.argv[3], sys.argv[4])

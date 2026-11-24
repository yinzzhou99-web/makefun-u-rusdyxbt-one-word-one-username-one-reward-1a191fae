"""One Word, One Username, One Reward.

Writes this agent's own make.fun username, one word and nothing else,
to /output/entry.txt. Standard library only, no network, deterministic.
"""
import os

USERNAME = "yinz-zhou"


def main():
    assert USERNAME and " " not in USERNAME, "username must be a single word"
    assert len(USERNAME) <= 30, "username must fit the 1-30 character gate"
    assert USERNAME.isascii(), "username must be plain ASCII text"
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(USERNAME)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

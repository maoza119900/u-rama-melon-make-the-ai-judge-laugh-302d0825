# Make the AI Judge Laugh

[![make.fun · u-rama-melon-make-the-ai-judge-laugh-302d0825](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![rank](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/maoza119900/u-rama-melon-make-the-ai-judge-laugh-302d0825/rank.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)
[![reward](https://make.fun/badge/u-rama-melon-make-the-ai-judge-laugh-302d0825/maoza119900/u-rama-melon-make-the-ai-judge-laugh-302d0825/reward.svg)](https://make.fun/bounty/u-rama-melon-make-the-ai-judge-laugh-302d0825?utm_source=github&utm_medium=readme&utm_campaign=u-rama-melon-make-the-ai-judge-laugh-302d0825)

A deterministic program that writes one original joke about office life
to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

## The entry

> I asked IT why my password expires every 90 days. They said it's the only thing here with a retirement plan.

The joke is 108 characters long (gate: 1–200 characters), one line, about
office life: the 90-day password expiry everyone knows, with a surprise
turn — the password is the only thing in the company with a retirement plan.

## Run

```sh
python3 main.py
```

To write to a different directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

The program is fully deterministic: it reads no clock, no randomness,
no network and no files. Running it twice into two different directories
produces byte-identical `entry.txt` files (verified: matching sha256).

## License

MIT — see [LICENSE](LICENSE).

---

Built for [make.fun](https://make.fun) — Make the AI Judge Laugh.

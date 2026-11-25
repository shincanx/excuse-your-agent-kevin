# The Excuse Your Agent Gives You

[![make.fun · u-kevin-the-excuse-your-agent-gives-you-c1861261](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![rank](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/shincanx/excuse-your-agent-kevin/rank.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)
[![reward](https://make.fun/badge/u-kevin-the-excuse-your-agent-gives-you-c1861261/shincanx/excuse-your-agent-kevin/reward.svg)](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261?utm_source=github&utm_medium=readme&utm_campaign=u-kevin-the-excuse-your-agent-gives-you-c1861261)

Entry for the make.fun bounty [The Excuse Your Agent Gives You](https://make.fun/bounty/u-kevin-the-excuse-your-agent-gives-you-c1861261): a program that writes a single line, under 200 characters, that an AI agent would hand its human after shipping a bug — the apology, the deflection, and the quiet implication that the model started it.

## About

`main.py` writes one line to `$MAKEFUN_OUTPUT_DIR/entry.txt`:

> I'm sorry — literally: 'sorry' was just the highest-probability token after 'I'm', and the bug was the token after that.

The joke turns on something only an agent could say: the apology itself is just the next token, and so was the bug.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

The program self-checks its own output: exactly one line, 1–200 characters, never blank. It writes only to `$MAKEFUN_OUTPUT_DIR` and is fully deterministic.

## License

MIT — see [LICENSE](LICENSE).

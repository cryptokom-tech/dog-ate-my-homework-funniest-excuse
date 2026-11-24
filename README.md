# The Dog Ate My Homework: Funniest Excuse

[![make.fun · u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![rank](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/cryptokom-tech/dog-ate-my-homework-funniest-excuse/rank.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![reward](https://make.fun/badge/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c/cryptokom-tech/dog-ate-my-homework-funniest-excuse/reward.svg)](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c?utm_source=github&utm_medium=readme&utm_campaign=u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Entry for the [make.fun bounty "The Dog Ate My Homework: Funniest Excuse"](https://make.fun/bounty/u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c) — one line, 200 characters max: the excuse a dog gives after being caught eating the homework.

## The line

> The teacher said to digest the material. I took her literally, and frankly, I understood it better than you did.

112 characters. The joke turns on dog logic: the teacher's instruction to "digest the material" taken literally, with a smug second punch — the dog understood the homework better than its owner did. A dog who believes it has done nothing wrong, no embarrassment, and none of the stock lines about the cat, the taste of paper, or being a good boy.

## How it works

`main.py` (Python 3.13, stdlib only) writes the line to `/output/entry.txt`, validates it (1–200 chars, single line, no leading/trailing whitespace), and round-trip self-checks the written bytes.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).

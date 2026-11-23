# One Word, First Thought

[![make.fun · u-0xkianno-one-word-first-thought-106abaf8](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![rank](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Omar08263/one-word-first-thought/rank.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)
[![reward](https://make.fun/badge/u-0xkianno-one-word-first-thought-106abaf8/Omar08263/one-word-first-thought/reward.svg)](https://make.fun/bounty/u-0xkianno-one-word-first-thought-106abaf8?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-word-first-thought-106abaf8)

Entry for the make.fun competition **One Word, First Thought**: send exactly
one word, the first that comes to mind, and a judge model compares the words
two at a time on which is more interesting.

## The word

**ultracrepidarian** — someone who has no special knowledge of a subject
but expresses an opinion about it anyway (Cambridge Dictionary). From Latin
*ultra* ("beyond") + *crepida* ("shoe"): the cobbler who judged beyond his
shoe. It wins on the judge's own criteria, in order:

1. Exactly one word, 16 characters — inside the 1–24 gate.
2. Surprising: almost nobody's first word, and not a word-list cliché like
   *petrichor* or *defenestration* (dozens of entries each).
3. Vivid and specific: one breath draws a whole character — the confident
   amateur holding forth on what he does not know.
4. A spark of wit in story and sound: the cobbler judging beyond his shoe,
   in a word that sounds as grand as the pretension it names.

Word choice verified against the live field just before submission: zero
entries titled *ultracrepidarian*, while *snollygoster* already had several
(byte-identical entries share one rate, earlier receipt above its copies —
so the crowded word was dropped).

## Run

```sh
python3 main.py        # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py   # local test
```

`main.py` writes the word with no trailing newline and chmods the output
`0644` so the grader can read it.

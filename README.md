# No-Commit

Make sure you never commit things you didn't mean to.

**no-commit** is a handy tool to scan your files before trying to commit them,
to a git repository.

It will not let you commit files that contain the strings

- "no-commit"
- "no-checkin"

## Installation and usage

Using [pre-commit](https://pre-commit.com) you can install and run no-commit on
every attempted commit.

Simply add this to your `.pre-commit-config.yaml`

```yml
  - repo: https://github.com/thesyscall/no-commit
    rev: 1.0.0
    hooks:
      - id: no-commit
        exclude: .pre-commit-config.yaml
```

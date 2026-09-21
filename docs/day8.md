### Day 08:
pre-commit

`pre-commit` is a framework which runs small checks (hooks) commits automatically.
The configuration needs to be defines in a `.pre-commit-config.yaml` file placed in the
root directory. The file contains the hooks defined by `repo` - the URL of the remote repo,
` rev` - version, and a `hook` - the id of the hook.
Using pre-commit allows us to wire automated checks to enforce code quality.

Test it out by creating a new commit or with

```
pre-commit run --all-files
```

To keep hook version up-to-date, use:
```
pre-commit autoupdate
```

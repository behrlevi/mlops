### Day 05:
The Makefile

The purpose of the file is to streamline the bulk execution of commands. You can create stages of operations and execute them
with `make setup`, etc. You an even create groups holding multiple stages as `all: setup lint`, etc.

The `.PHONY:` target serves to distinguish stages from filenames so `make` does not execute files named setup or lint created
in the root directory.
More technically: The names following it are treated as its prerequisites.
Make registers every prerequisite of .PHONY in its internal table as a non-file rule, instructing the dependency graph to ignore
disk checks for those names and always run their recipe.

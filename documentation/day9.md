### Day 09:
cookiecutter

Cookicutter can be used to create project templates with variables and if-else branching
to enforce a uniform structure.

The `cookiecutter.json` stores template file to define the template variables. A list like
ml_framework in our case, becomes a choice variable, with the first entry as the default.
The desired directory structure is then created under `{{cookiecutter.project_name}}/`
directory. Files are rendered with Jinja2 substitution as in requirements.txt.

To create the project from the template:
```
cookiecutter ./template -o . --no-input project_name=churn-model ml_framework=sklearn
```

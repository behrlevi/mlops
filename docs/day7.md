### Day 07:
Testing and packaging

We have two goals to achieve in the section.
The first is to write a simple unit test and run it.
The second is to package the application into a portable and reproduciblewheel (.whl),
which holds the source code and all the dependecies and can be set up everywhere with pip.

1. I have written the test logic in src/fraud_detection/predict.py which return 1 if the first value exceeds 100 and 0
if its below.
When `python3 -m pytest tests/ -q` is executed, [tool.pytest.ini_options] is read from `pyproject.toml`,
which sets pythonpath to the src directory. It executes src/tests/test_predict.py, which in turn
imports and executes the logic from src/fraud_detection/prediction.py.
The two tests should pass with the following output:
```
..                                                                                                [100%]
2 passed in 0.00s
```

2. The wheel can be built with `python3 -m build`.
Python spins up an isolated, temporary environment for building the package.
It reads `[build-system]` from `pyproject.toml` and outputs two files in the dist directory:
```
fraud_detection-0.1.0-py3-none-any.whl
fraud_detection-0.1.0.tar.gz
```
You should try deploying the .whl from another directory with:
```
pip install ../dist/fraud_detection-0.1.0-py3-none-any.whl
```
Then open a python3 terminal and run the following:
```
import fraud_detection
print(fraud_detection.__version__)
```
Note:
If you run Python from inside your repository folder, it will just read your local src/ directory instead of the installed package.

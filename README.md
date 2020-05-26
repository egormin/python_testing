### Python unit testing

#### Testing Frameworks:
- `unittest`. In the python standard library
- `nose`. Not in the  standard library. Simpler tests than unittest
- `pytest`. Not in the  standard library.

***unittest installation:***
```
pip install unittest
```

***Run pytest:***
```
pytest one
```
It runs all tests from module `one`
```
pytest one/test_math_func.py -v
```
It runs testfile `one/test_math_func.py` with verbose
```
pytest one/test_math_func.py::test_add
```
It runs separate test
```
py.test
```
Automatically find test_* files and run them





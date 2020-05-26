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

```
pytest one -v -k "add"
```
Run tests from one which contains `add`
```
pytest one -v -k "string or multiple"
```
Run tests fromeone which contains `string` or `multiple`
```
pytest one -v -k "string and multiple"
```
Run tests from one which contains `string` and `multiple`
```
pytest one -m number -v
```
Run only tests which marked as number
```
pytest one -x
```
Tests after failed will be skipped. Otherwise all tests will be performed
```
pytest one -x --tb=no
```
Disable stacktrace messages in failed tests description

```
pytest one -x --maxfail=2
```
Ho many failed tests should occur for skipping other tests
```
@pytest.mark.skip(reason="do not run it")
```
To skip test. With `-rsx` it will be shown a reason of skipping
```
@pytest.mark.skipif(sys.version_info < (3, 1), reason="too old python")

```
To skip test with condition (python version < 3.1). With `-rsx` it will be shown a reason of skipping
```
pytest one -s
```
Tests output will contain output of `print` command. Without `-s` no
```
pytest one -q
```
Quiet mode to avoid unnecessary information in output
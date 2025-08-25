# NumUtils C Library with Python Test

This project demonstrates how to create a **C shared library** and use it in Python using `ctypes`.

## Folder Structure

```
num-add-lib/
├── include/           # Header files
│   └── numutils.h
├── lib/               # Compiled shared library
│   └── numutils-lib.so
├── src/               # Source code
│   └── numutils.c
└── test/              # Python test file
    └── test.py
```

## Features

* `add(int a, int b)` – Returns the sum of two integers.
* `is_even(int n)` – Returns 1 if a number is even, 0 if odd.

## Steps to Compile the Shared Library

From the project root:

```bash
gcc -fPIC -shared src/numutils.c -Iinclude -o lib/numutils-lib.so
```

* `-fPIC` → Position-independent code (required for shared libraries)
* `-shared` → Create `.so` shared library
* `-Iinclude` → Include folder for header files

---

## Python Test

### `test/test.py`

Example usage of the shared library in Python:

```python
import ctypes
import os

lib_path = os.path.join(os.path.dirname(__file__), "../lib/numutils-lib.so")
numutils = ctypes.CDLL(lib_path)

numutils.add.argtypes = [ctypes.c_int, ctypes.c_int]
numutils.add.restype = ctypes.c_int

numutils.is_even.argtypes = [ctypes.c_int]
numutils.is_even.restype = ctypes.c_int

a, b = 5, 7
print(f"{a} + {b} = {numutils.add(a, b)}")

n = 10
print(f"{n} is {'even' if numutils.is_even(n) else 'odd'}")
```

### Run the Python Test

From the project root:

```bash
python3 test/test.py
```

**Expected Output:**

```
5 + 7 = 12
10 is even
```

---

## Notes

* Make sure the shared library file name in Python matches exactly (`numutils-lib.so`).
* If Python cannot find the shared library, set the library path:

```bash
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib
python3 test/test.py
```

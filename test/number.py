import ctypes;
import os;

lib_path=os.path.join(os.path.dirname(__file__), '../lib/number.so');
numutils = ctypes.CDLL(lib_path)

# --- Define C function signatures ---

# int add(int a, int b);
numutils.add.argtypes = [ctypes.c_int, ctypes.c_int]
numutils.add.restype = ctypes.c_int

# int is_even(int n);
numutils.is_even.argtypes = [ctypes.c_int]
numutils.is_even.restype = ctypes.c_int

# --- Test the functions ---
a, b = 5, 7
print(f"{a} + {b} = {numutils.add(a, b)}")

n = 10
if numutils.is_even(n):
    print(f"{n} is even")
else:
    print(f"{n} is odd")
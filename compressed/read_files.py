import os
from numpy import load

# Get the path to the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, 'compressed_N9_M1_MB16_QS1.npz')

data = load(filepath, allow_pickle=True)
lst = data.files
for item in lst:
    print(item)
    print(data[item])
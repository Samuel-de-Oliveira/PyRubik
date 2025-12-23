# PyRubik
A Python module to make speedcubing projects a piece of cake.

## How to install
```sh
pip install pyrubik
```

## Usage
This code generate a scramble for a 2x2x2 cube:
```python
from PyRubik import GetScramble

if __name__ == '__main__':
  scramble: list = GetScramble.Cube2x2x2() # Create the scramble
  print(f'A 2x2x2 Scramble: {scramble}')   # Show it
```

#### Made in Brazil :brazil:

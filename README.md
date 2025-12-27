# PyRubik
PyRubik is python module create to assist the creation of speedcubing
softwares made in Python. For example, if you are creating a speedcuber
timer using Flask, this module may help you.

## How to install
```sh
pip install pyrubik
```

## Usage
The module has so many features. Just take a look:

### Generate official WCA scrambles
> This code generate a scramble for a 2x2x2 cube:

```python
# This is a 2x2.py file
from PyRubik import Scramble

if __name__ == '__main__':
  scramble: list = Scramble.Cube2x2x2() # Create the scramble
  print(f'A 2x2x2 Scramble: {scramble}')   # Show it
```

```sh
# Your output must look similar like this:
A 2x2x2 Scramble: ['R2', "F'", 'R2', 'F', "R'", 'U', 'R2', 'U', "F'"]
```

> This another one generate for 3x3x3 cube, but without the list syntax

```python
# This is a 3x3.py file
from PyRubik import Scramble

if __name__ == '__main__':
  scramble: list = Scramble.Cube3x3x3() # Create the scramble

  # Show it
  for move in scramble:
      print(move, end='  ')
  print()
```

```sh
# Your output must look similar like this
U  L  U2  F'  U'  D'  F2  U'  F  L'  R  F2  B2  L2  R'  F  U'  B  F2  U'  F  B2  L  U
```

### PyRubik docs
Comming soon...

---

Made with ❤️ in Brazil 🇧🇷

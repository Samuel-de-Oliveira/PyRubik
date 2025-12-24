Usage
=====

There are some usages for the PyRubik library. Just take a look:

Scramble
--------

1. This code generate and print a 3x3 scramble

.. code-block:: python

  from PyRubik import Scramble

  if __name__ == '__main__':
    scb: list = Scramble.Cube3x3x3() # Generate scramble

    # Show it
    for move in scb:
      print(move, end=' ')
    print()

I want to know more
-------------------

If you want to know more about the commands, just check the :doc:`commands`
topic.

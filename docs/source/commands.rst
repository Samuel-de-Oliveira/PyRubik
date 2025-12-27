PyRubik Commands
================

PyRubik.Scramble
----------------
*Provides official WCA Scrambles.*

This class is very intuitive. you may know that the right
usage will look like this:

.. code-block:: python

   scb: list = Scramcle.Modality()

Then there is a list of all suported modalities:

* ``Scramble.Cube2x2x2()``
* ``Scramble.Cube3x3x3()``
* ``Scramble.Cube4x4x4()``
* ``Scramble.Cube5x5x5()``
* ``Scramble.Cube6x6x6()``
* ``Scramble.Cube7x7x7()``
* ``Scramble.Pyraminx()``
* ``Scramble.Skewb()``
* ``Scramble.Square_One()``
* ``Scramble.Megaminx()``
* ``Scramble.Clock()``

All of them will return a ``list`` type.

PyRubik.Tools
-------------
*Provides events that will assist with your scrambles.*

reverse
^^^^^^^
Create a reverse scrable.

**Synopsis:**

.. code-block:: python

  r_scb: list = Tools.reverse( scramble: list )

**Arguments:**

* Source ``scramble``: Your scramble

**Returns**

* Type: ``list``

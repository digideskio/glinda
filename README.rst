Glinda is a simple command line utility that helps one rank-order a moderately
long list of items using a series of head-to-head matches between them.
I wrote it as a quick-and-dirty way to rank 100-someodd choices for the
housing lottery at my university.

Usage
-----
The items should be listed, one to a line, in a file called ``options.txt``;
the output will be listed in ``result.txt`` when the program finishes. Simply
press the [1] and [2] keys to choose the winner in each match; press [Q] to
quit early.

Algorithm
---------
Glinda implements the `Mergesort <http://en.wikipedia.org/wiki/Mergesort>`_
algorithm. Mergesort was chosen because it is near-optimal in the number of
comparisons required; as the user is performing comparisons manually, it was
reasonable to assume that the cost of comparisons dominates all other costs.
Other computations and memory usage were considered to be irrelevant in
comparison (hence, a naive, recursive implementation was sufficient).

Mergesort is not nearly as robust to "mistakes" as other, tournament-style
algorithms. Matches decided early on tend to have a disproportional effect
on the end result, so the output should be considered a sensible starting
point for tweaks, rather than a definitive ordering (unless you are 100%
confident in every decision).

License
-------
The code in ``sort.py`` and ``main.py`` is hereby released into the public
domain, and may be used, modified, and redistributed by anyone for any
purpose. ``getch.py`` is included under the terms of the Python Software
Foundation (PSF) license.

This is a tiny script to calculate [Civilization V](http://www.civilization5.com/)'s grid numbering scheme for hexes. The use (I'm told) is for the game's
active modding community, in particular a mod that allows cities to grow to
larger size than the defaults.

That's everything I know about it! Oh, and that you should only use this
code if you want a hexgrid for Civilization V. It's an oddball
scheme, different than the [accepted numbering
system](https://github.com/pfrolov/hexagonal-spiral) for hexgrids. That
latter link implements an amusingly titled math sequence known as the
"crystal ball sequence for hexagonal lattices":

> Computing coordinates of a cell
 
> The sequence described by the algorithm above is the sequence
> [A003215](http://oeis.org/A003215) of Hex (or centered hexagonal) numbers: 3 * n * (n + 1) + 1 (crystal ball sequence for hexagonal lattice).

For anything other than Civ5, you'll want to use that instead.

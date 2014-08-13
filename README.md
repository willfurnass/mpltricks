mpltricks
=========

### tick\_skip(ax, keep\_every=2, x\_or\_y='y', min\_cur_\lines=4)

Reduce the number of ticks on a given matplotlib Axes object

 * ax -- matplotlib.axes.Axes object
 * keep\_every -- keep one in this many ticks e.g. set to 3 to reduce the number of ticks by 2/3
 * x\_or\_y -- can be 'x' or 'y'; reduces the number of ticks on the corresponding axis
 * min\_cur\_lines -- only reduce the number of ticks if the total number to start with is more than this

### line\_style\_cycle(ax, line\_styles=('-', '--',  '-.', ':'))

Update the style of all lines in a matplotlib Axes in a round-robin
fashion. If line\_styles contains four elements but ax has five Lines associated with
it then the first and fifth lines will have the same style.

 * ax -- matplotlib.axes.Axes object
 * line\_styles -- the list of matplotlib line styles that are cycled through

### subplot\_ids(axes, x\_rel=0.9, y\_rel=0.9)

Annotate each of several matplotlib Axes with an alpha identifier.  e.g. Draw an '(a)' label on the first Axes object, a '(b)' on the second etc.

 * axes -- An enumerable collection of matplotlib.axes.Axes objects
 * x\_rel -- Relative position of the alpha identifier w.r.t. the x axis
 * y\_rel -- Relative position of the alpha identifier w.r.t. the y axis

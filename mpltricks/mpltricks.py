from __future__ import absolute_import
from itertools import cycle
import string


def tick_skip(ax, keep_every=2, x_or_y='y', min_cur_lines=4):
    """Reduce the number of ticks on a given matplotlib Axes object

    Arguments:
    ax -- matplotlib.axes.Axes object
    keep_every -- keep one in this many ticks e.g. set to 3 to
                  reduce the number of ticks by 2/3
    x_or_y -- can be 'x' or 'y'; reduces the number of ticks on the
              corresponding axis
    min_cur_lines -- only reduce the number of ticks if the total
                     number to start with is more than this

    """
    if x_or_y == 'y':
        tick_setter = ax.set_yticks
        cur_ticks = ax.get_yticks()
    elif x_or_y == 'x':
        tick_setter = ax.set_xticks
        cur_ticks = ax.get_xticks()
    else:
        raise Exception("x_or_y must be 'x' or 'y'")

    if len(cur_ticks) > min_cur_lines:
        tick_setter([tick for tick_idx, tick in enumerate(cur_ticks)
                     if tick_idx % keep_every == 0])


def line_style_cycle(ax, line_styles=('-', '--',  '-.', ':')):
    """Update the style of all lines in a matplotlib Axes in a round-robin
    fashion.

    If line_styles contains four elements but ax has five Lines associated with
    it then the first and fifth lines will have the same style.

    Arguments:
    ax -- matplotlib.axes.Axes object
    line_styles -- the list of matplotlib line styles that are cycled through

    """
    for line, line_style in zip(ax.get_lines(), cycle(line_styles)):
        line.set_linestyle(line_style)


def subplot_ids(axes, x_rel=0.9, y_rel=0.9):
    """Annotate each of several matplotlib Axes with an alpha identifier.

    e.g. Draw an '(a)' label on the first Axes object, a '(b)' on the
    second etc.

    Arguments:
    axes -- An enumerable collection of matplotlib.axes.Axes objects
    x_rel -- Relative position of the alpha identifier w.r.t. the x axis
    y_rel -- Relative position of the alpha identifier w.r.t. the y axis

    """
    for ax, _id in zip(axes, cycle(string.ascii_lowercase)):
        x = ((ax.get_xlim()[1] - ax.get_xlim()[0]) * x_rel) + ax.get_xlim()[0]
        y = ((ax.get_ylim()[1] - ax.get_ylim()[0]) * y_rel) + ax.get_ylim()[0]
        ax.text(x, y, "({})".format(_id),
                bbox=dict(facecolor='white', alpha=0.5, edgecolor='white'))

def grey_line_gradient(ax):
    """Set color of first Line on Axes to black, last Line to 2/3 to white and 
    interpolate between when colouring the other lines.

    Arguments:
    ax -- matplotlib.axes.Axes object
    """
    n_lines = len(ax.lines)
    for line_idx, line in enumerate(ax.lines):
        line.set_color('{}'.format(line_idx / (1.5 * n_lines)))

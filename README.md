# mpltricks

A number of Matplotlib helper functions.


### Reduce the number of ticks on a given matplotlib `Axes` object.

```python
tick_skip(ax, keep_every=2, x_or\_y='y', min_cur_lines=4)
```

* `ax`: `matplotlib.axes.Axes` object
* `keep_every`: keep one in this many ticks e.g. set to `3` to reduce the number of ticks by 2/3
* `x_or_y`: can be `'x'` or `'y'`; reduces the number of ticks on the corresponding axis
* `min_cur_lines`: only reduce the number of ticks if the total number to start with is more than this


### Update the style of all lines in a matplotlib `Axes` in a round-robin fashion.

If `line_styles` contains four elements but ax has five Lines associated with it then the first and fifth lines will have the same style.  

```python
line_style_cycle(ax, line_styles=('-', '--',  '-.', ':'))
```

* `ax`: `matplotlib.axes.Axes` object
* `line_styles`: the list of matplotlib line styles that are cycled through


### Annotate each of several matplotlib `Axes` with an alpha identifier.  

E.g. Draw an *(a)* label on the first `Axes` object, a *(b)* on the second etc.  

```python
subplot_ids(axes, x_rel=0.9, y_rel=0.9)
```

* `axes`: An enumerable collection of `matplotlib.axes.Axes` objects
* `x_rel`: Relative position of the alpha identifier w.r.t. the x axis
* `y_rel`: Relative position of the alpha identifier w.r.t. the y axis

NB `Axes` where the `label_position` is `'top'` are ignored to prevent subplots with secondary axes from being labelled twice.


### Naievely change colours of lines in line plot to shades of grey

Set color of first `Line` on `Axes` to black, last `Line` to 2/3 to white and interpolate between when colouring the other lines.

```python
grey_line_gradient(ax)
```

* `ax`: `matplotlib.axes.Axes` object

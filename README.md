<br/>
<p align="center">
  <a href="https://github.com/NotFrancee/mpl_bsic">
    <img src="images/logo.png" alt="Logo" height="80">
  </a>

  <h3 align="center">mpl-bsic</h3>

  <p align="center">
    Create matplotlib plots in BSIC Style!
    <br/>
    <br/>
    <a href="https://mpl-bsic.readthedocs.io/en/latest/"><strong>Explore the docs »</strong></a>
    <br/>
    <br/>
    <a href="https://github.com/NotFrancee/mpl_bsic/issues">Report Bug</a>
    -
    <a href="https://github.com/NotFrancee/mpl_bsic/issues">Request Feature</a>
  </p>
</p>

![Contributors](https://img.shields.io/github/contributors/NotFrancee/mpl_bsic?color=dark-green) ![Issues](https://img.shields.io/github/issues/NotFrancee/mpl_bsic) ![License](https://img.shields.io/github/license/NotFrancee/mpl_bsic)


## About the Project

<div align="center">
  <img src="images/about_project.svg" alt="Plot Example" align='center'>
</div>

This package allows you to style matplotlib plots using BSIC Style (fonts, colors, logos, etc.) to later use them in BSIC articles. It also
provides utility function to plot trades, handle the formatting of the axis, check the size of the figures, and more!

Read the sections below for an overview of how to install and use the package. For further information, be sure to [read the docs](https://mpl-bsic.readthedocs.io/en/latest/)!

## Table Of Contents

* [About the Project](#about-the-project)
* [Installation](#installation)
* [Docs and TLDR](#docs-and-tldr)
* [If the matplotlib fonts do not work](#if-the-matplotlib-fonts-do-not-work)
* [Contributing](#contributing)
* [Roadmap](#roadmap)

## Installation

The package supports all python versions starting from `3.9.0`

To install, run

```
pip install mpl-bsic
```


Then you can import the functions from the module, for example

```
from mpl_bsic import apply_bsic_style
```

## Docs and TLDR

Read the docs on [this link](https://mpl-bsic.readthedocs.io/).
All the functions are explained extensively and you can find example code/plots.

**WARNING**: Be sure to read the docs for apply_bsic_style, and in particular how to make sure the style gets applied. You always have to make sure you call `plt.show()`
(if in a script) even if you only plan to export the plot, since otherwise matplotlib won't run the animations which are required to apply the style to the title.
And also read carefully the part about the figsize to use, especially when exporting to use in a Word file.

A brief overview of the functions of the module:

* `apply_bsic_style`: applies the BSIC styles to a plot (font families, font sizes).
* `apply_bsic_logo`: applies the BSIC logo to the plot. You can specify the size, location and logo type.
* `plot_trade`: plots performance of the trade and path of underlying in BSIC style, with the possibility
  to specify additional parameters regarding formatting and visualization
* `check_figsize`: checks the figsize of your plot, to make sure it will be rendered correctly in MS Word.
    Returns the correct figure width and height to use
* `format_timeseries_axis`: formats the x axis of a timeseries plot.
    You can specify the time unit (yearly, monthly, daily), the frequency (e.g. a tick every 3M), and the format (e.g. MM/YYYY or MMM YYYY)
* `preprocess_dataframe`: preprocesses a dataframe, by setting the index to the date (and converting to datetime)
    and transforming all the columns to lowercase for easier use in the project

## If the matplotlib fonts do not work

Starting from version 1.2, `apply_bsic_style` will temporarily install the fonts (__Garamond__ and __Gill Sans MT__) using `FontManager` in `matplotlib`,
so that plots still get styled correctly. 

For perfomance, however, this could not be the wisest choice, and you can refer to the documentation on how to properly
install the fonts on your system and make them recognizable my matplotlib. 

## Contributing

If you have any ideas, features you would like to have implemented, or you find out any bugs within the function, be sure
to open an issue and I will work on it as soon as possible. Or you can also fork the repo yourself and make a PR
to the project!

## Roadmap

1) plot tables (instead of having to style them using Excel)
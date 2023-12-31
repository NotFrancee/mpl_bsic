import functools
import os
from os.path import join, split

from flaky import flaky
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.testing.compare import compare_images
from matplotlib.testing.decorators import remove_ticks_and_titles
from matplotlib.testing.exceptions import ImageComparisonFailure

from utils.run_animations import run_animations


def _compare_img(fig: Figure, expected: str, format_: str, tol: float):
    base_dir, filename = split(join("tests", "baseline", expected))
    out_dir = split(join("tests", "output_images", expected))[0]

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    plt.rcParams["savefig.bbox"] = "standard"
    plt.rcParams["savefig.dpi"] = "figure"

    run_animations(fig)
    fig.savefig(os.path.join(out_dir, (filename + format_)))

    image_name = filename + format_
    expected_name = os.path.join(base_dir, image_name)
    actual_name = os.path.join(out_dir, filename + format_)

    err = compare_images(expected_name, actual_name, tol, in_decorator=True)

    if not os.path.exists(expected_name):
        raise ImageComparisonFailure("image does not exist: %s" % expected_name)

    if err is not None:
        for key in ["actual", "expected"]:
            err[key] = os.path.relpath(err[key])  # type: ignore
        raise ImageComparisonFailure(
            "images not close (RMS %(rms).3f):\n\t%(actual)s\n\t%(expected)s " % err
        )


def image_compare(
    baseline_images: str,
    fmt: str = ".png",
    tol: float = 1,
    remove_text: bool = False,
):
    def decorator(func):
        @functools.wraps(func)
        @flaky(max_runs=3, min_passes=1)
        def wrapper(*args, **kwargs):
            print("decorator got called")
            plt.close("all")

            fig = func(*args, **kwargs)
            if remove_text:
                remove_ticks_and_titles(fig)

            try:
                _compare_img(fig, baseline_images, fmt, tol)
            finally:
                plt.close("all")

        return wrapper

    return decorator


def baseline_save_fig(fig, filename):
    run_animations(fig)
    fig.savefig("tests/baseline/" + filename + "_dbg.png")

import functools
import os
from os.path import join, split

from flaky import flaky
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.testing.compare import compare_images
from matplotlib.testing.decorators import remove_ticks_and_titles
from matplotlib.testing.exceptions import ImageComparisonFailure


def _compare_img(fig: Figure, expected: str, format_: str, tol: float):
    base_dir, filename = split(join("tests", "baseline", expected))
    out_dir = split(join("tests", "output_images", expected))[0]

    if not os.path.exists(out_dir):
        os.makedirs(out_dir)

    if hasattr(fig, "_bsic_animations"):
        bsic_animations = fig.__getattribute__("_bsic_animations")
        print(bsic_animations)

        for ani in bsic_animations:
            for _ in range(5):
                try:
                    ani._stop = False
                    ani._step()
                except (
                    AttributeError
                ):  # catches when animation has no more frames and cannot step anymore
                    break

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
    plt.show(block=False)
    plt.pause(0.5)
    fig.savefig(
        "tests/baseline/" + filename + "_dbg.png", dpi=1200, bbox_inches="tight"
    )
    fig.savefig("tests/baseline/" + filename + "_dbg.png")

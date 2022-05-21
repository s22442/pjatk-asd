from random import random
from timeit import timeit
from config import SAMPLE_VALUE_RANGE, SAMPLE_COUNT, TIMEIT_NUMBER

random_samples = [round(random() * SAMPLE_VALUE_RANGE + 1) for _ in range(SAMPLE_COUNT)]
sorted_samples = [i for i in range(SAMPLE_COUNT)]
reversed_sorted_samples = sorted_samples[:]
reversed_sorted_samples.reverse()


def print_sorting_time(label: str, sort_cb: callable(int)):
    print(f"# {label}")
    print(
        f" - random samples: {timeit(lambda: sort_cb(random_samples), number = TIMEIT_NUMBER):.6f}"
    )
    print(
        f" - sorted samples: {timeit(lambda: sort_cb(sorted_samples), number = TIMEIT_NUMBER):.6f}"
    )
    print(
        f" - reversed sorted samples: {timeit(lambda: sort_cb(reversed_sorted_samples), number = TIMEIT_NUMBER):.6f}"
    )

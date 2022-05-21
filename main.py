from helpers import print_sorting_time
from heapsort import sort as heapsort
from mergesort import sort as mergesort
from quicksort import sort as quicksort
from timsort import sort as timsort
from pythonsort import sort as pythonsort


if __name__ == "__main__":
    print_sorting_time("Heap-Sort", heapsort)
    print()
    print_sorting_time("Merge-Sort", mergesort)
    print()
    print_sorting_time("Quick-Sort", quicksort)
    print()
    print_sorting_time("Tim-Sort", timsort)
    print()
    print_sorting_time("Python built-in Tim-Sort", pythonsort)

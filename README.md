# QuickSort Comparison: Randomized vs Deterministic

## Overview
This project implements and compares two versions of the QuickSort algorithm: **Randomized QuickSort** and **Deterministic QuickSort**. The goal is to analyze their performance by measuring the average execution time on arrays of different sizes (10,000, 50,000, 100,000, and 500,000 elements) filled with random integers. The results are presented in a table and visualized in a plot.

## Features
1. **Randomized QuickSort**: Selects the pivot randomly to reduce the likelihood of worst-case scenarios.
2. **Deterministic QuickSort**: Uses the last element as the pivot.
3. **Performance Testing**: Measures average execution time over 5 runs for each array size.
4. **Results Visualization**: Outputs results in a console table and generates a plot (`quicksort_comparison.png`).
5. **Analysis**: Provides insights into the performance differences between the two algorithms.

## Requirements
- Python 3.x
- Required libraries:
  - `matplotlib` (for plotting)
  - `tabulate` (for table formatting)
  - `numpy` (for array operations)

## Installation
1. Clone or download the project repository.
2. Install the required Python libraries:
   ```bash
   pip install matplotlib tabulate numpy
   ```
3. Ensure the `quicksort_comparison.py` script is in the project directory.

## Usage
1. Run the script:
   ```bash
   python quicksort_comparison.py
   ```
2. The script will:
   - Generate random arrays of specified sizes.
   - Measure and display the average execution time for both algorithms.
   - Print a formatted table of results in the console.
   - Save a plot comparing the performance (`quicksort_comparison.png`).
   - Provide an analysis of the results.

## Expected Output
The console output will look like this:
```
Порівняння рандомізованого та детермінованого QuickSort
Розмір масиву: 10000
   Рандомізований QuickSort: 0.0189 секунд
   Детермінований QuickSort: 0.0189 секунд

Розмір масиву: 50000
   Рандомізований QuickSort: 0.1104 секунд
   Детермінований QuickSort: 0.1090 секунд

Розмір масиву: 100000
   Рандомізований QuickSort: 0.2333 секунд
   Детермінований QuickSort: 0.2435 секунд

Розмір масиву: 500000
   Рандомізований QuickSort: 1.4166 секунд
   Детермінований QuickSort: 1.4815 секунд

Таблиця результатів:
+-----------------+----------------------+-----------------------+
| Розмір масиву   | Рандомізований (с)   | Детермінований (с)    |
+-----------------+----------------------+-----------------------+
| 10000           | 0.0189               | 0.0189                |
| 50000           | 0.1104               | 0.1090                |
| 100000          | 0.2333               | 0.2435                |
| 500000          | 1.4166               | 1.4815                |
+-----------------+----------------------+-----------------------+

Аналіз результатів:
1. Both algorithms show similar performance on random data.
2. Randomized QuickSort may perform better in worst-case scenarios (e.g., nearly sorted arrays) due to random pivot selection.
3. Deterministic QuickSort may be slightly faster on average due to lower overhead (no random number generation).
4. The performance difference becomes more noticeable on larger arrays but remains small.
```

A plot (`quicksort_comparison.png`) will be generated, showing execution time vs. array size for both algorithms.

## Analysis
- **Randomized QuickSort**: More robust in worst-case scenarios (e.g., sorted or nearly sorted arrays) as it avoids consistent poor pivot choices. However, it incurs slight overhead due to random number generation.
- **Deterministic QuickSort**: Slightly faster on random data due to no randomization overhead but can degrade to O(n²) in worst-case scenarios.
- On large arrays, the difference in execution time is small, but Randomized QuickSort generally provides more consistent performance across various input types.

## Files
- `quicksort_comparison.py`: Main script containing the implementation, testing, and visualization logic.
- `quicksort_comparison.png`: Generated plot comparing the performance of both algorithms (created after running the script).

## License
This project is licensed under the MIT License.
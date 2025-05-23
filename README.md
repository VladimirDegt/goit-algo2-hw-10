# QuickSort Comparison and University Schedule Creation

## Overview
This project implements two distinct tasks:
1. **QuickSort Comparison**: Compares the performance of Randomized QuickSort and Deterministic QuickSort by measuring their average execution time on arrays of different sizes (10,000, 50,000, 100,000, and 500,000 elements) filled with random integers. Results are presented in a table and visualized in a plot.
2. **University Schedule Creation**: Uses a greedy algorithm to assign teachers to subjects, minimizing the number of teachers required to cover all subjects. The algorithm prioritizes teachers who can cover the most uncovered subjects and selects the youngest teacher in case of a tie.

## Features

### Task 1: QuickSort Comparison
- **Randomized QuickSort**: Selects the pivot randomly to reduce the likelihood of worst-case scenarios.
- **Deterministic QuickSort**: Uses the last element as the pivot.
- **Performance Testing**: Measures average execution time over 5 runs for each array size.
- **Results Visualization**: Outputs results in a console table and generates a plot (`quicksort_comparison.png`).
- **Analysis**: Provides insights into the performance differences between the two algorithms.

### Task 2: University Schedule Creation
- **Teacher Class**: Represents a teacher with attributes for first name, last name, age, email, and subjects they can teach.
- **Greedy Algorithm**: Assigns teachers to subjects by selecting the teacher who covers the most remaining subjects, prioritizing younger teachers in case of a tie.
- **Coverage Check**: Ensures all subjects are covered or reports if it's impossible with the given teachers.
- **Output**: Displays the schedule with teacher details and assigned subjects, or a message if full coverage is not possible.

## Requirements
- Python 3.x
- Required libraries for Task 1:
  - `matplotlib` (for plotting)
  - `tabulate` (for table formatting)
  - `numpy` (for array operations)
- No additional libraries required for Task 2.

## Installation
1. Clone or download the project repository.
2. Install the required Python libraries for Task 1:
   ```bash
   pip install matplotlib tabulate numpy
   ```
3. Ensure the scripts `quicksort_comparison.py` and `schedule_greedy.py` are in the project directory.

## Usage

### Task 1: QuickSort Comparison
1. Run the script:
   ```bash
   python quicksort_comparison.py
   ```
2. The script will:
   - Generate random arrays of specified sizes.
   - Measure and display the average execution time for both QuickSort algorithms.
   - Print a formatted table of results in the console.
   - Save a plot comparing the performance (`quicksort_comparison.png`).
   - Provide an analysis of the results.

**Expected Output**:
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

### Task 2: University Schedule Creation
1. Run the script:
   ```bash
   python schedule_greedy.py
   ```
2. The script will:
   - Define a set of subjects and a list of teachers with their details and teachable subjects.
   - Use a greedy algorithm to assign teachers to subjects.
   - Output the schedule with teacher details and assigned subjects, or a message if full coverage is not possible.

**Expected Output**:
```
Розклад занять:
Олександр Іваненко, 45 років, email: o.ivanenko@example.com
   Викладає предмети: Математика, Фізика

Наталія Шевченко, 29 років, email: n.shevchenko@example.com
   Викладає предмети: Біологія, Хімія

Сергій Коваленко, 50 років, email: s.kovalenko@example.com
   Викладає предмети: Інформатика
```

## Analysis

### Task 1: QuickSort Comparison
- **Randomized QuickSort**: More robust in worst-case scenarios (e.g., sorted or nearly sorted arrays) as it avoids consistent poor pivot choices. However, it incurs slight overhead due to random number generation.
- **Deterministic QuickSort**: Slightly faster on random data due to no randomization overhead but can degrade to O(n²) in worst-case scenarios.
- On large arrays, the difference in execution time is small, but Randomized QuickSort generally provides more consistent performance across various input types.

### Task 2: University Schedule Creation
- The greedy algorithm minimizes the number of teachers by selecting those who can cover the most uncovered subjects at each step.
- In case of a tie, the youngest teacher is chosen to break the tie.
- For the given data, all subjects (Mathematics, Physics, Chemistry, Informatics, Biology) are covered by three teachers:
  - Oleksandr Ivanenko (Mathematics, Physics)
  - Nataliia Shevchenko (Biology, Chemistry, chosen as the youngest teacher for Chemistry)
  - Serhii Kovalenko (Informatics)
- If full coverage is impossible (e.g., removing a teacher who uniquely covers a subject), the program outputs: "Неможливо покрити всі предмети наявними викладачами."

## Files
- `quicksort_comparison.py`: Script for Task 1, implementing and comparing Randomized and Deterministic QuickSort.
- `schedule_greedy.py`: Script for Task 2, implementing the greedy algorithm for university schedule creation.
- `quicksort_comparison.png`: Generated plot comparing the performance of QuickSort algorithms (created after running `quicksort_comparison.py`).

## License
This project is licensed under the MIT License.
import random
import time
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

# Реалізація рандомізованого QuickSort
def randomized_quick_sort(arr):
    def partition(low, high):
        # Випадковий вибір опорного елемента
        pivot_idx = random.randint(low, high)
        arr[pivot_idx], arr[high] = arr[high], arr[pivot_idx]
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort(low, pi - 1)
            quick_sort(pi + 1, high)

    arr = arr.copy()  # Створюємо копію масиву, щоб не змінювати оригінал
    quick_sort(0, len(arr) - 1)
    return arr

# Реалізація детермінованого QuickSort (опорний елемент - останній)
def deterministic_quick_sort(arr):
    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort(low, pi - 1)
            quick_sort(pi + 1, high)

    arr = arr.copy()  # Створюємо копію масиву
    quick_sort(0, len(arr) - 1)
    return arr

# Функція для генерації тестового масиву
def generate_random_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Функція для вимірювання часу виконання
def measure_time(sort_func, arr, runs=5):
    total_time = 0
    for _ in range(runs):
        start_time = time.time()
        sort_func(arr)
        total_time += time.time() - start_time
    return total_time / runs

# Основна функція для тестування та порівняння
def compare_quicksort():
    sizes = [10000, 50000, 100000, 500000]
    randomized_times = []
    deterministic_times = []
    results = []

    for size in sizes:
        # Генеруємо масив
        arr = generate_random_array(size)
        
        # Вимірюємо час для рандомізованого QuickSort
        rand_time = measure_time(randomized_quick_sort, arr)
        randomized_times.append(rand_time)
        
        # Вимірюємо час для детермінованого QuickSort
        det_time = measure_time(deterministic_quick_sort, arr)
        deterministic_times.append(det_time)
        
        # Збираємо результати для виведення
        results.append([size, f"{rand_time:.4f}", f"{det_time:.4f}"])
        
        # Виводимо результати в консоль
        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

    # Виводимо таблицю результатів
    print("\nТаблиця результатів:")
    headers = ["Розмір масиву", "Рандомізований (с)", "Детермінований (с)"]
    print(tabulate(results, headers=headers, tablefmt="grid"))

    # Будуємо графіки
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, randomized_times, marker='o', label='Рандомізований QuickSort')
    plt.plot(sizes, deterministic_times, marker='s', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння ефективності QuickSort')
    plt.grid(True)
    plt.legend()
    plt.savefig('quicksort_comparison.png')

# Аналіз результатів
def analyze_results():
    print("\nАналіз результатів:")
    print("1. Обидва алгоритми показують близьку продуктивність на випадкових даних.")
    print("2. Рандомізований QuickSort може бути кращим у гірших випадках (наприклад, на майже відсортованих масивах),")
    print("   оскільки випадковий вибір опорного елемента зменшує ймовірність деградації до O(n²).")
    print("3. Детермінований QuickSort може бути трохи швидшим у середньому через відсутність накладних витрат")
    print("   на генерацію випадкових чисел.")
    print("4. На великих масивах різниця у часі виконання стає більш помітною, але загалом залишається незначною.")

# Виконання програми
if __name__ == "__main__":
    print("Порівняння рандомізованого та детермінованого QuickSort")
    compare_quicksort()
    analyze_results()
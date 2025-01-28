import random
import time
from functools import lru_cache

# Функція для обчислення суми на відрізку без кешу
def range_sum_no_cache(array, L, R):
    return sum(array[L:R + 1])

# Функція для оновлення елемента без кешу
def update_no_cache(array, index, value):
    array[index] = value

# LRU-кеш для запитів типу Range
@lru_cache(maxsize=1000)
def range_sum_with_cache(L, R):
    return sum(array[L:R + 1])

# Функція для оновлення елемента з кешем
def update_with_cache(index, value):
    array[index] = value
    range_sum_with_cache.cache_clear()  # Інвалідуємо кеш

# Генерація тестових даних
N = 100_000  # Розмір масиву
Q = 50_000   # Кількість запитів
array = [random.randint(1, 100) for _ in range(N)]
queries = []

for _ in range(Q):
    if random.random() < 0.5:
        L = random.randint(0, N - 1)
        R = random.randint(L, N - 1)
        queries.append(('Range', L, R))
    else:
        index = random.randint(0, N - 1)
        value = random.randint(1, 100)
        queries.append(('Update', index, value))

# Виконання тестів без кешу
start_no_cache = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_no_cache(array, query[1], query[2])
    elif query[0] == 'Update':
        update_no_cache(array, query[1], query[2])
end_no_cache = time.time()

# Виконання тестів з LRU-кешем
start_with_cache = time.time()
for query in queries:
    if query[0] == 'Range':
        range_sum_with_cache(query[1], query[2])
    elif query[0] == 'Update':
        update_with_cache(query[1], query[2])
end_with_cache = time.time()

# Виведення результатів
print(f"Час виконання без кешу: {end_no_cache - start_no_cache:.2f} секунд")
print(f"Час виконання з LRU-кешем: {end_with_cache - start_with_cache:.2f} секунд")

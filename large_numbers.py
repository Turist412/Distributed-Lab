from math import *
import random
import time


def broodforce(byte_range: int, byte: int):
    start_time = time.time()
    for k in range(byte_range):
        if k == byte:
            print(f"Сгенерированый ключ = {k}")
            return round((time.time() - start_time) * 1000)


byte_sizes = [2 ** x for x in range(int(log2(8)), int(log2(4096)) + 1)]

for byte_size in byte_sizes:
    byte_range = 2 ** byte_size
    print(f"Количество разных {byte_size}-битных ключей: {byte_range}")

for byte_size in byte_sizes:
    byte_range = 2 ** byte_size
    byte = random.randint(0, byte_range - 1)
    print(f"Случайный {byte_size}-битный ключ: {byte}")
    print(f"Время перебора: {broodforce(byte_range, byte)} мс")
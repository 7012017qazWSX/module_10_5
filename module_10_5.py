import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    end_time = time.perf_counter()
    print(f"Линейный: {end_time - start_time} секунд")

    # Многопроцессный вызов
    start_time = time.perf_counter()
    with Pool(processes = 4) as pool:
        pool.map(read_info, filenames)
    end_time = time.perf_counter()
    print(f"Многопроцессный: {end_time - start_time} секунд")

import multiprocessing
from time import time, sleep
from nonogram import solve_nonogram


def run_7X7():
    input_7s = [
        [[1],[1],[1,1],[1],[1],[1],[1]],
        [[1],[1],[1],[1],[1,1],[1],[1]]
    ]
    start_time7 = time()
    res7 = solve_nonogram(input_7s)
    end_time_7 = time()
    print('7s', end_time_7- start_time7)


def run_8X8():
    input_8s = [
        [[1],[1],[1,1],[1],[1],[1],[1],[1,1]],
        [[1,1],[1],[1],[1],[1],[1,1],[1],[1]]
    ]
    start_time8 = time()
    res8 = solve_nonogram(input_8s)
    end_time_8 = time()
    print('8s', end_time_8- start_time8)


def run_and_kill_after_timeout(func, name, max_time, ideal):
    # Start foo as a process
    p = multiprocessing.Process(target=func, name=name)
    p.start()

    # Wait 10 seconds for foo
    sleep(max_time)

    if p.is_alive():
        # Terminate foo
        p.terminate()
        raise Exception(f"Process ran for more than {max_time} seconds\n"
                        f"You could possibly get it to around {ideal} seconds")
    else:
        print(f"Check for {name} passed")
    p.join()


if __name__ == '__main__':
    run_and_kill_after_timeout(run_7X7, "7X7", 15, 4)
    run_and_kill_after_timeout(run_8X8, "8X8", 100, 55)




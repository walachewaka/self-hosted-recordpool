from analyze_metadata import metadata_analyzer
from multiprocessing import Pool

# define worker function before a Pool is instantiated
def worker(task):
    pool_size = 1000  # your "parallelness"
    try:
        metadata_analyzer
    except KeyboardInterrupt:
        print('error with item')
    for tasks in task:
        pool.apply_async(worker, (tasks,))
    pool = Pool(pool_size)
    pool.close()
    pool.join()

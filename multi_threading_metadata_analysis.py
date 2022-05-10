from analyze_metadata import metadata_analyzer
from multiprocessing.pool import ThreadPool as Pool
# from multiprocessing import Pool

pool_size = 5  # your "parallelness"

# define worker function before a Pool is instantiated
def worker(task):
    try:
        metadata_analyzer
    except KeyboardInterrupt:
        print('error with item')
    for tasks in task:
        pool.apply_async(worker, (tasks,))
pool = Pool(pool_size)



pool.close()
pool.join()
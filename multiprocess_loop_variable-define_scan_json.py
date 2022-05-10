from loop_variable_scan_json import write_directory_to_variable
from multiprocessing import Pool

pool_size = 8  # your "parallelness"

# define worker function before a Pool is instantiated

# define worker function before a Pool is instantiated
def worker(item):
    try:
        global items
        items = write_directory_to_variable
    except:
        print('error with item')

pool = Pool(pool_size)

for item in items:
    pool.apply_async(worker, (item,))

pool.close()
pool.join()
import time
start_time = time.time()

from load_data import Load
Load.load_database()
print("--- %s seconds ---" % (time.time() - start_time))
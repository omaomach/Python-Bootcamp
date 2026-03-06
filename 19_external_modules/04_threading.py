import threading
import time

def worker(num):
    print(f"Thread {num}: Starting")
    time.sleep(2) # Simulate work (e.g., a network request)
    print(f"Thread {num}: Finishing")

threads = []

for i in range(3):
    thread = threading.Thread(target=worker, args=(i,)) # creates a thread
    threads.append(thread) # saves the thread to the list
    thread.start() # Launches it

for thread in threads:
    thread.join() # Wait for all threads to finish

print("All threads completed.")


'''
Here are the official Python docs for each topic:
Threading

https://docs.python.org/3/library/threading.html — the full threading module, including Lock()

Multiprocessing

https://docs.python.org/3/library/multiprocessing.html — the multiprocessing module

Asyncio

https://docs.python.org/3/library/asyncio.html — the asyncio module

The GIL

https://wiki.python.org/moin/GlobalInterpreterLock — Python's wiki explanation of the GIL
'''
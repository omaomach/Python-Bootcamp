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
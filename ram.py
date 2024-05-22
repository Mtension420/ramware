import time
import psutil
import threading

def cpu_intensive_task():
    # A task that performs continuous computations to increase CPU usage
    while True:
        # Perform a computationally intensive calculation
        [x**2 for x in range(10000)]


    

def consume_ram(limit_mb):
    """
    Consume memory up to a specified limit (in MB).
    """
    data = []
    chunk_size = 10**6  # Approximate size of each chunk in elements
    mb_per_chunk = (chunk_size * 8) / (1024**2)  # Convert chunk size to MB

    while True:
        # Check current memory usage
        memory_info = psutil.virtual_memory()
        used_memory_mb = memory_info.used / (1024**2)
        available_memory_mb = memory_info.available / (1024**2)
        
        print(f"Used Memory: {used_memory_mb:.2f} MB, Available Memory: {available_memory_mb:.2f} MB")

        if used_memory_mb + mb_per_chunk >= limit_mb:
            print("Memory limit reached. Stopping allocation.")
            continue

        # Allocate more memory
        data.append([0] * chunk_size)
        print(f"Allocated {len(data) * mb_per_chunk:.2f} MB of memory")
        time.sleep(0.1)  # Small delay to make the output readable

if __name__ == "__main__":
    memory_limit_mb = 6000  # Set memory limit in MB
    consume_ram(memory_limit_mb)
    num_threads = 4

    # Create and start threads
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=cpu_intensive_task)
        threads.append(thread)
        thread.start()

    # Keep the main thread alive
    for thread in threads:
        thread.join()


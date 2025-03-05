import socket
import threading
from queue import Queue

socket.setdefaulttimeout(1)  # 1 second timeout

target = "127.0.0.1"  # Replace with a target you have permission to scan
queue = Queue()
open_ports = []

def portscan(port):
    try:
        # Create socket for each connection attempt
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False
    finally:
        sock.close()

def fill_queue(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.empty():
        port = queue.get()
        if portscan(port):
            print(f"Port {port} is open!")
            open_ports.append(port)
        queue.task_done()

# Configure which ports to scan
port_list = range(1, 1024)
fill_queue(port_list)

thread_list = []

# Adjust number of threads as needed
for _ in range(50):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

# Wait until the queue is fully processed
queue.join()

# Optionally wait for threads to finish (though queue.join() often suffices)
for thread in thread_list:
    thread.join()

print("Open ports are:", open_ports)

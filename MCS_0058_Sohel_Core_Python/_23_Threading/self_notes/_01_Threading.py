import threading
if(threading.current_thread() == threading.main_thread()):
    print("You are in main thread.")
else:
    print("You are not in main thread.")

thread_name = threading.currentThread().getName()
print(thread_name)
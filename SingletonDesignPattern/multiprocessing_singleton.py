# implementation with thread safe and multiprocessing safe
# ex: Application with multiprocessing

import multiprocessing

class Singleton:
    _lock = multiprocessing.Lock()  # Use multiprocessing Lock
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:  # Lock across processes
                if cls._instance is None:
                    cls._instance = super().__new__(cls, *args, **kwargs)
                    print("Singleton instance created.")
        return cls._instance

def worker():
    singleton = Singleton()
    print(f"Singleton instance: {singleton}")

if __name__ == "__main__":

    process1 = multiprocessing.Process(target=worker)
    process2 = multiprocessing.Process(target=worker)

    process1.start()
    process2.start()

    process1.join()
    process2.join()
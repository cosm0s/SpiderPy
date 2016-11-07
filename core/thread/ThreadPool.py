from queue import Queue

class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func,args, kargs))

    def wait_completion(self):
        self.tasks.join()

    def stop(self):
        print("")

    def info(self):
        print("")
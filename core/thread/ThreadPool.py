from queue import Queue
from core.thread.Worker import Worker


class ThreadPool:
    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        self.tasks.put((func, args, kargs))

    def wait_completion(self):
        self.tasks.join()

    # TODO remove when this is implemented
    @staticmethod
    def stop():
        print("")

    @staticmethod
    def info():
        print("")

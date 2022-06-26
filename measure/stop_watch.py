import time
import datetime

class StopWatch:
    """Stop Watch to measure the elapsed time."""

    def __init__(self):
        self.start_time    = None
        self.start_counter = None
        self.stop_time     = None
        self.stop_counter  = None


    def start(self):
        self.start_time = self._now()
        self.start_counter = self._count()


    def stop(self):
        self.stop_time = self._now()
        self.stop_counter = self._count()


    def elapsed(self, precision=2):
        if (self.start_counter == None or self.stop_counter == None):
            return None
        diff = self.stop_counter - self.start_counter
        precision_format = '.' + str(precision) + 'f'
        return format(round(diff,precision), precision_format)

    def _now(self):
        return datetime.datetime.now()

    def _count(self):
        return time.perf_counter()



import psutil, tracemalloc
import pandas as pd
from gml.measure.stop_watch import StopWatch

class SystemMeter:
    """Common system meter interface for all resource monitoring implementations.

    For each system resource to monitor, a wrapper class will be written as subclass of this one.
    This way we have a common "interface" for all system resources to test.
    """
    def __init__(self, name):
        self.name = name

    def start(self):
        pass

    def stop(self):
        pass

    def result(self):
        pass

    def measure(self, func):
        self.start()
        func()
        self.stop()
        return self.result()

    def format(self, value, unit):
        return float( format(round(float(value)/unit, 2), '.2f') )

    @staticmethod
    def create_df(measures, labels):
        """Creates a pandas data frame from a list of measures. Each measure is a dictionary with the measure as key
        and the value. The keys are used as index labels. The values of a dict are the column values. The labels parameter
        is used as column labels. The order of the measuers must be aligned with the order of the labels.
        """
        # create dict as base for the data frame
        d = {}
        for label, measure in zip(labels, measures):
            d[label] = measure.values()
        # use measure dict keys as index
        index = list(measures[0].keys())
        index = list(map(lambda s: s.capitalize(), index))
        # create and return result
        return pd.DataFrame(data=d, index=index)

class CpuSystemMeter(SystemMeter):
    """Measures the cpu workload in percent of all availble cpu's."""

    def __init__(self):
        SystemMeter.__init__(self, "CPU [%]")
        self.unit = 1
        self.process = None
        self.total_cpu = None

    def start(self):
        self.process = psutil.Process()
        self.process.cpu_percent(interval=None)

    def stop(self):
        self.total_cpu = self.process.cpu_percent(interval=None)

    def result(self):
        return self.format(self.total_cpu / psutil.cpu_count(), self.unit)


class MemorySystemMeter(SystemMeter):
    """Measures the current and peak memory consumption in bits as well as the stats.
    The result_metric param defines which metric ["current", "peak", "stats" or "all"] to return as result.
    """
    def __init__(self, result_metric="peak"):
        SystemMeter.__init__(self, "Memory [MB]")
        self.unit = 1000000
        self.snapshot = None
        self.result_metric = result_metric
        self.current = None
        self.peak = None
        self.stats = None

    def start(self):
        tracemalloc.start()
        self.snapshot = tracemalloc.take_snapshot()

    def stop(self):
        snapshot2 = tracemalloc.take_snapshot()
        self.current, self.peak = tracemalloc.get_traced_memory()
        self.stats = snapshot2.compare_to(self.snapshot, 'lineno')
        tracemalloc.stop()

    def result(self):
        if self.result_metric == "current":
            return self.format(self.current, self.unit)
        if self.result_metric == "peak":
            return self.format(self.peak, self.unit)
        if self.result_metric == "stats":
            return self.format(self.stats, self.unit)
        return {
            "current" : self.format(self.current, self.unit),
            "peak"    : self.format(self.peak, self.unit),
            "stats"   : self.format(self.stats, self.unit)
        }

class TimeSystemMeter(SystemMeter):
    """Measures the elapsed time in seconds."""

    def __init__(self):
        SystemMeter.__init__(self, "Time [min]")
        self.unit = 60
        self.stop_watch = StopWatch()

    def start(self):
        self.stop_watch.start()

    def stop(self):
        self.stop_watch.stop()

    def result(self):
        return self.format(self.stop_watch.elapsed(), self.unit)

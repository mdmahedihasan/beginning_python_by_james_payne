import math
from threading import Thread
import time


class SquareRootCalculator:
    def __init__(self, target):
        self.results = []
        counter = self.CalculatorThread(self, target)
        print("Turning on the calculator thread...")
        counter.start()
        while len(self.results) < target:
            print("%d square roots calculated so far." % len(self.results))
            time.sleep(1)
        print(
            "Calculated %s square root(s); the last one is sqrt(%d) = %f " % (
                target, len(self.results), self.results[-1]))


class CalculatorThread(Thread):
    def __init__(self, controller, target):
        Thread.__init__(self)
        self.controller = controller
        self.target = target
        self.setDaemon(True)

    def run(self):
        for i in range(1, self.target + 1):
            self.controller.results.append(math.sqrt(i))


if __name__ == '__main__':
    import sys

    limit = None
    if len(sys.argv) > 1:
        limit = sys.argv[1]
        try:
            limit = int(limit)
        except ValueError:
            print("Usage: %s [number of square roots to calculate ]" % sys.argv[0])
    SquareRootCalculator(limit)

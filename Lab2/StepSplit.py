class StepSplit:
    def __init__(self, step):
        self._step = step

    @staticmethod
    def get_step(self):
        self._step = self._step / 2
        return self._step

# Compatibility shim for environments that still import from pufferlib.utils
# TODO: Update all environments to import directly from pufferlib

import numpy as np
from pufferlib import Suppress, silence_warnings

# RandomState was removed from pufferlib, recreate it for compatibility
class RandomState:
    def __init__(self, seed):
        self.rng = np.random.RandomState(seed)

    def random(self):
        return self.rng.random()

    def probabilistic_round(self, n):
        frac, integer = np.modf(n)
        if self.random() < frac:
            return int(integer) + 1
        else:
            return int(integer)

__all__ = ['Suppress', 'silence_warnings', 'RandomState']
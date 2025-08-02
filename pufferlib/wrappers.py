# Compatibility shim for environments that still import from pufferlib.wrappers
# TODO: Update all environments to import directly from pufferlib

from pufferlib import GymToGymnasium, PettingZooTruncatedWrapper

__all__ = ['GymToGymnasium', 'PettingZooTruncatedWrapper']
from pdb import set_trace as T
import numpy as np

import gymnasium as gym
import functools

import pufferlib
import pufferlib.emulation
import pufferlib.environments


def env_creator(name='Airstriker-Genesis'):
    return functools.partial(make, name)

def make(name='Airstriker-Genesis', framestack=4, buf=None):
    '''Atari creation function with default CleanRL preprocessing based on Stable Baselines3 wrappers'''
    retro = pufferlib.environments.try_import('retro', 'stable-retro')

    from stable_baselines3.common.atari_wrappers import (
        ClipRewardEnv,
        EpisodicLifeEnv,
        FireResetEnv,
        MaxAndSkipEnv,
    )
    with pufferlib.Suppress():
        env = retro.make(name)

    env = gym.wrappers.RecordEpisodeStatistics(env)
    env = MaxAndSkipEnv(env, skip=4)
    env = ClipRewardEnv(env)
    env = gym.wrappers.ResizeObservation(env, (84, 84))
    env = gym.wrappers.GrayScaleObservation(env)
    env = gym.wrappers.FrameStack(env, framestack)
    return pufferlib.emulation.GymnasiumPufferEnv(env=env, buf=buf)

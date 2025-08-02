# PufferLib Claude System Prompt

This file contains important information for Claude when working with PufferLib.

## Project Overview

PufferLib is a high-performance reinforcement learning library that supports various environments and hardware configurations including Apple Silicon (M1/M2/M3/M4).

## Key Features

- Fast vectorized environments
- Support for CUDA, MPS (Apple Silicon), and CPU
- Automatic device selection based on network size
- Numba JIT compilation for CPU performance
- Integration with popular RL environments

## Apple Silicon Support

When working on Apple Silicon:
- Use `--train.device mps` for GPU acceleration
- Networks <100K parameters perform better on CPU
- Networks >=100K parameters should use MPS
- Install with: `NO_TRAIN=1 uv pip install --no-build-isolation -v .`

## Development Guidelines

- Keep changes minimal and focused
- Maintain backward compatibility
- Test on multiple hardware configurations
- Use existing code patterns and conventions
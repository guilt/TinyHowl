"""Control-thread targets. Audio thread only smooths current → target."""

from __future__ import annotations


def linear(t: float) -> float:
    return max(0.0, min(1.0, t))


def ease_in(t: float) -> float:
    t = linear(t)
    return t * t


def ease_out(t: float) -> float:
    t = linear(t)
    return 1 - (1 - t) * (1 - t)


def coo_decay(t: float) -> float:
    t = linear(t)
    return (1 - t) ** 1.6

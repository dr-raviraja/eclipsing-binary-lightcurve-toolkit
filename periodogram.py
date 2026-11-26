"""Lomb-Scargle periodogram helper for eclipsing binary photometry."""
import numpy as np
from astropy.timeseries import LombScargle


def find_orbital_period(time_bjd, mag, mag_err=None, min_period=0.15, max_period=5.0, nterms=2):
    """
    Compute multi-harmonic Lomb-Scargle periodogram.
    For contact binaries with two nearly equal minima per orbit,
    nterms=2 captures both the fundamental and half-period harmonics.
    """
    min_freq = 1.0 / max_period
    max_freq = 1.0 / min_period

    ls = LombScargle(time_bjd, mag, dy=mag_err, nterms=nterms)
    freq, power = ls.autopower(minimum_frequency=min_freq, maximum_frequency=max_freq, samples_per_peak=15)
    best_freq = freq[np.argmax(power)]
    best_period = 1.0 / best_freq
    fap = ls.false_alarm_probability(np.max(power))

    return {
        "best_period": float(best_period),
        "best_frequency": float(best_freq),
        "fap": float(fap),
        "periods": 1.0 / freq,
        "power": power,
    }

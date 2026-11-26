"""Observed-minus-Calculated (O-C) eclipse timing residual fitting."""
import numpy as np


def compute_oc(minima_bjd, t0, period):
    """Return cycle number E (integers/half-integers) and O-C residuals in days."""
    raw_cycles = (np.asarray(minima_bjd) - t0) / period
    epochs = np.round(2.0 * raw_cycles) / 2.0
    calc_bjd = t0 + epochs * period
    oc_days = np.asarray(minima_bjd) - calc_bjd
    return epochs, oc_days


def fit_quadratic_ephemeris(epochs, oc_days, oc_err=None):
    """
    Fit O-C = dT0 + dP * E + Q * E^2.
    Secular period change rate: dP/dt = 2 * Q / P (days/day).
    """
    weights = None if oc_err is None else 1.0 / np.asarray(oc_err)
    coeffs, cov = np.polyfit(epochs, oc_days, deg=2, w=weights, cov=True)
    q_coeff, dp_coeff, dt0_coeff = coeffs
    errs = np.sqrt(np.diag(cov))
    return {
        "Q": float(q_coeff),
        "Q_err": float(errs[0]),
        "dP": float(dp_coeff),
        "dP_err": float(errs[1]),
        "dT0": float(dt0_coeff),
        "dT0_err": float(errs[2]),
        "model_oc": np.polyval(coeffs, epochs),
    }

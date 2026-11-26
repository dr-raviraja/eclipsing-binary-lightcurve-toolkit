# Eclipsing Binary Light-Curve & O-C Analysis Toolkit

A modular collection of reproducible Python scripts for time-series photometric analysis of close, contact, and eclipsing binary star systems, developed by **Dr. Ravi Raja Pothineni** (Department of Astronomy, Osmania University).

Built to support transparent, scripted workflows alongside standard astrophysical modelling tools, this toolkit helps researchers and students inspect multi-epoch light curves, test orbital period stability, and diagnose candidate third bodies or magnetic activity cycles.

## What Is Inside
- **Multi-Harmonic Periodogram Search (`eb_toolkit/periodogram.py`):** Computes Lomb-Scargle periodograms (using multi-harmonic terms to capture both orbital and half-orbital variation in contact binaries) with false-alarm probability diagnostics for survey and ground-based CCD time series.
- **Orbital Phase Folding & Visualisation (`eb_toolkit/phase_fold.py`):** Folds BJD/HJD timestamps onto orbital phase ($\phi \in [0, 1)$) using reference epoch $T_0$ and period $P$, computes phase-binned averages, and produces clean light-curve plots.
- **Observed-minus-Calculated ($O-C$) Timing Analysis (`eb_toolkit/oc_analysis.py`):** Assigns integer and half-integer eclipse cycles, computes $O-C$ residuals, and fits quadratic ephemerides to quantify secular period changes ($\mathrm{d}P/\mathrm{d}t$) linked to mass transfer or angular momentum loss.
- **Worked Examples (`examples/`):** Self-contained demonstration scripts using synthetic time-series data so users can verify installation and outputs immediately.

## Scope & Data Note
This repository contains general-purpose analysis routines and synthetic demonstration examples. Proprietary observational datasets and results from active or unpublished manuscripts are kept separate until formal publication.

## Stack & Usage
Built around `numpy`, `scipy`, `matplotlib`, and `astropy`, with workflows compatible with downstream modelling pipelines such as Wilson-Devinney (WD), PHOEBE, and MCMC parameter estimation.

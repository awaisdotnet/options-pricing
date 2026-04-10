# Quantitative Options Pricing — Black-Scholes & Monte Carlo Implementation

## Overview
A Python implementation of the Black-Scholes options pricing model, built from first principles using stochastic calculus. The project prices European call and put options using both the closed-form Black-Scholes solution and Monte Carlo simulation, demonstrating convergence between the two methods.

## Mathematical Foundation
The Black-Scholes model assumes asset prices follow Geometric Brownian Motion:

dS = μS dt + σS dW

where W is a Wiener process. Applying Itô's Lemma to a derivative V(S,t) and constructing a risk-free portfolio under no-arbitrage assumptions yields the Black-Scholes PDE:

∂V/∂t + ½σ²S²(∂²V/∂S²) + rS(∂V/∂S) - rV = 0

The closed-form solution for a European call option is:

C = S·N(d1) - Ke^(-rT)·N(d2)

where:
- d1 = [ln(S/K) + (r + ½σ²)T] / σ√T
- d2 = d1 - σ√T
- N(·) is the cumulative standard normal distribution

## Features
- **Black-Scholes closed-form pricing** for European call and put options
- **Option Greeks** — Delta, Gamma, Theta, Vega
- **Monte Carlo simulation** with 10,000 paths using GBM
- **BSM vs Monte Carlo convergence analysis**
- **Matplotlib visualisation** of option prices across a range of stock prices

## Results
Using parameters S=100, K=105, T=1, r=0.05, σ=0.2:

| Method | Call Price | Put Price |
|--------|-----------|-----------|
| Black-Scholes | £8.0214 | £7.9004 |
| Monte Carlo | £8.0240 | £7.9317 |
| Difference | £0.0027 | £0.0313 |

The Monte Carlo simulation converges to within £0.003 of the analytical solution — validating both implementations.

## Option Greeks
| Greek | Value | Interpretation |
|-------|-------|----------------|
| Delta | 0.5422 | Option price increases £0.54 per £1 rise in stock price |
| Gamma | 0.0198 | Rate of change of Delta |
| Theta | -6.2771 | Option loses £6.28 in value per year due to time decay |
| Vega | 39.6705 | Option price increases £39.67 per unit increase in volatility |

## Installation
```bash
pip install numpy matplotlib scipy
```

## Usage
```bash
python3 black_scholes.py
```

## Technologies
- Python 3
- NumPy
- Matplotlib
- SciPy

## Author
Awais | BSc Accounting and Finance, University of Leicester
github.com/awaisdotnet

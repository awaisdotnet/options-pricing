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
Awais | University of Leicester | github.com/awaisdotnet
---

## Implied Volatility Calculator & Volatility Smile Visualisation

### Overview
A numerical implied volatility solver that works backwards from observed market option prices to extract the volatility implied by the market. Demonstrates where Black-Scholes assumptions break down in practice through volatility smile visualisation.

### Mathematical Foundation
Under Black-Scholes, implied volatility should be constant across all strikes. In reality, markets price options with a volatility smile or skew — higher implied volatility for deep out-of-the-money and in-the-money options. This phenomenon is one of the most well-documented failures of the BSM model.

The implied volatility σ* is found by solving:

C_market = BSM(S, K, T, r, σ*) 

using the Brent numerical root-finding method (SciPy), which brackets the solution between near-zero and 1000% volatility.

### Results
| Strike | Market Price | Implied Vol |
|--------|-------------|-------------|
| 95     | £10.50      | 10.41%      |
| 100    | £8.50       | 14.75%      |
| 105    | £7.00       | 17.43%      |
| 110    | £5.50       | 18.63%      |
| 115    | £4.50       | 20.09%      |
| 120    | £3.50       | 20.74%      |

The upward skew confirms that BSM underprices out-of-the-money calls relative to market prices — a direct violation of the constant volatility assumption.

### Usage
```bash
python3 implied_volatility.py
```

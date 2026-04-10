import numpy as np
from scipy.stats import norm
from scipy.optimize import brentq
import matplotlib.pyplot as plt
from black_scholes import BlackScholesModel


def implied_volatility(market_price, S, K, T, r, option_type='call'):
    def objective(sigma):
        model = BlackScholesModel(S, K, T, r, sigma)
        if option_type == 'call':
            return model.call_price() - market_price
        else:
            return model.put_price() - market_price

    try:
        iv = brentq(objective, 1e-6, 10.0)
        return iv
    except ValueError:
        return None


def plot_volatility_smile(S, T, r, market_prices, strikes, option_type='call'):
    ivs = []
    valid_strikes = []

    for K, price in zip(strikes, market_prices):
        iv = implied_volatility(price, S, K, T, r, option_type)
        if iv is not None:
            ivs.append(iv * 100)
            valid_strikes.append(K)

    plt.figure(figsize=(10, 6))
    plt.plot(valid_strikes, ivs, marker='o', color='blue', linewidth=2)
    plt.axvline(x=S, color='red', linestyle='--', label='Current Stock Price')
    plt.xlabel('Strike Price')
    plt.ylabel('Implied Volatility (%)')
    plt.title('Volatility Smile — Implied Volatility vs Strike Price')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    S = 100
    T = 1
    r = 0.05

    strikes = [80, 85, 90, 95, 100, 105, 110, 115, 120]
    market_prices = [21.0, 17.0, 13.5, 10.5, 8.5, 7.0, 5.5, 4.5, 3.5]

    print("=" * 50)
    print("IMPLIED VOLATILITY CALCULATOR")
    print("=" * 50)
    print(f"{'Strike':<10} {'Market Price':<15} {'Implied Vol':<15}")
    print("-" * 40)

    for K, price in zip(strikes, market_prices):
        iv = implied_volatility(price, S, K, T, r, option_type='call')
        if iv is not None:
            print(f"{K:<10} £{price:<14.2f} {iv*100:<.2f}%")

    print("=" * 50)
    plot_volatility_smile(S, T, r, market_prices, strikes, option_type='call')
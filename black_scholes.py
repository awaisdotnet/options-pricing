import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


class BlackScholesModel:
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def d1(self):
        return (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))

    def d2(self):
        return self.d1() - self.sigma * np.sqrt(self.T)

    def call_price(self):
        return (self.S * norm.cdf(self.d1()) -
                self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2()))

    def put_price(self):
        return (self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d2()) -
                self.S * norm.cdf(-self.d1()))

    def delta(self):
        return norm.cdf(self.d1())

    def gamma(self):
        return norm.pdf(self.d1()) / (self.S * self.sigma * np.sqrt(self.T))

    def theta(self):
        return ((-self.S * norm.pdf(self.d1()) * self.sigma / (2 * np.sqrt(self.T))) -
                self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d2()))

    def vega(self):
        return self.S * norm.pdf(self.d1()) * np.sqrt(self.T)


def monte_carlo_option_price(S, K, T, r, sigma, simulations=10000, option_type='call'):
    np.random.seed(42)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)

    if option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    else:
        payoffs = np.maximum(K - ST, 0)

    return np.exp(-r * T) * np.mean(payoffs)


def plot_option_prices(S, K, T, r, sigma):
    stock_prices = np.linspace(S * 0.5, S * 1.5, 100)
    call_prices = []
    put_prices = []

    for spot in stock_prices:
        model = BlackScholesModel(spot, K, T, r, sigma)
        call_prices.append(model.call_price())
        put_prices.append(model.put_price())

    plt.figure(figsize=(10, 6))
    plt.plot(stock_prices, call_prices, label='Call Price', color='blue')
    plt.plot(stock_prices, put_prices, label='Put Price', color='red')
    plt.axvline(x=K, color='black', linestyle='--', label='Strike Price')
    plt.xlabel('Stock Price')
    plt.ylabel('Option Price')
    plt.title('Black-Scholes Option Prices vs Stock Price')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    S = 100
    K = 105
    T = 1
    r = 0.05
    sigma = 0.2

    model = BlackScholesModel(S, K, T, r, sigma)
    print("=" * 40)
    print("BLACK-SCHOLES OPTION PRICING MODEL")
    print("=" * 40)
    print(f"Call Price:  £{model.call_price():.4f}")
    print(f"Put Price:   £{model.put_price():.4f}")
    print(f"Delta:       {model.delta():.4f}")
    print(f"Gamma:       {model.gamma():.4f}")
    print(f"Theta:       {model.theta():.4f}")
    print(f"Vega:        {model.vega():.4f}")

    print("=" * 40)
    print("MONTE CARLO SIMULATION (10,000 paths)")
    print("=" * 40)
    mc_call = monte_carlo_option_price(S, K, T, r, sigma, option_type='call')
    mc_put = monte_carlo_option_price(S, K, T, r, sigma, option_type='put')
    print(f"MC Call Price: £{mc_call:.4f}")
    print(f"MC Put Price:  £{mc_put:.4f}")
    print(f"BSM vs MC Call Difference: £{abs(model.call_price() - mc_call):.4f}")

    plot_option_prices(S, K, T, r, sigma)
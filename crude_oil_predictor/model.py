# model.py
import math
import random

def predict_oil_prices(
    start_year=2025,
    end_year=2075,
    inflation_rate=3.0,
    econ_challenge_level=5,
    policy_support_level=5
):
    """
    Very simple toy forecast:
    - base_price grows a bit every year
    - inflation, economic challenges and policy support adjust growth and volatility
    """

    years = list(range(start_year, end_year + 1))
    forecasts = []

    base_price = 80.0  # starting price in USD

    # normalize levels (1-10) to -1..+1 effect
    econ_factor = (econ_challenge_level - 5) / 5.0   # more challenges -> more upward pressure & volatility
    policy_factor = (policy_support_level - 5) / 5.0 # more support -> more stability, slightly lower risk

    price = base_price

    for y in years:
        # baseline yearly growth (2%)
        growth = 0.02

        # inflation impact (scaled)
        infl_impact = (inflation_rate / 100.0) * 0.6

        # economic stress increases volatility and trend
        econ_trend = econ_factor * 0.015

        # policy support slightly reduces trend but reduces volatility
        policy_trend = -policy_factor * 0.01

        # random shock with volatility affected by econ/policy
        base_vol = 0.05
        vol = base_vol + econ_factor * 0.03 - policy_factor * 0.02
        vol = max(0.0, vol)
        shock = random.uniform(-vol, vol)

        yearly_growth = growth + infl_impact + econ_trend + policy_trend + shock
        price *= (1.0 + yearly_growth)
        price = max(10.0, price)  # keep non‑crazy

        forecasts.append({"year": y, "price": round(price, 2)})

    return forecasts

import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1379613676  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    const = 0.059
    x -= const
    return max(max(x), 2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x)))) + const, \
           max(max(x), 2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x)))) + const


# x = np.array([0.1, 0.2, 0.3, 0.2, 0.15, 0.25])

# print(solution(0.9, x))

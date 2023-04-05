import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1379613676  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    const = 0.059
    x -= const
    return 2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))) + const, \
           2 * (x.mean() - np.sqrt(np.var(x)) * norm.ppf(alpha / 2) / np.sqrt(len(x))) + const


# x = np.array([0.3, 0.4, 0.45])

# print(solution(0.95, x))

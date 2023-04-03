import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1379613676  # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    b_alpha = np.quantile(x, alpha)
    return .059, b_alpha

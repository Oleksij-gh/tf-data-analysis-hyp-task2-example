import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 581150379 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:

    alpha = 0.05
    
    stat, p_value = mannwhitneyu(x, y, alternative='two-sided')
    return p_value > alpha

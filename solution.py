import pandas as pd
import numpy as np

chat_id = 401141478

def solution(x: np.array) -> float:
    return 2*np.mean(x)/(61**2)

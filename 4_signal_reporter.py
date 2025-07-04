import pandas as pd

def generate_report(signal, confidence, explanations):
    df = pd.DataFrame([{
        "Signal": signal,
        "Confidence": confidence,
        "Matched Strategies": ", ".join(explanations)
    }])
    return df

from 3_strategy_matcher import match_strategies

def analyze_screenshot(pil_image):
    # Image → candle_data conversion (placeholder for now)
    candle_data = {
        "current": "green",
        "prev": "red",
        "current_size": 90,
        "prev_size": 50,
        "long_wick": True,
        "small_body": True
    }

    signal, matched = match_strategies(candle_data)
    return {
        "signal": signal,
        "confidence": 90 if matched else 60,
        "detected_info": ", ".join(matched) if matched else "No strong strategy match"
    }

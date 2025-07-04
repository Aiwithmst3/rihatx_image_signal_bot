def wick_trap_strategy(candle_data):
    if candle_data["long_wick"] and candle_data["small_body"]:
        return True, "Wick Trap Detected"
    return False, ""

def bullish_engulfing(candle_data):
    if candle_data["current"] == "green" and candle_data["prev"] == "red" and candle_data["current_size"] > candle_data["prev_size"] * 1.2:
        return True, "Bullish Engulfing Pattern"
    return False, ""

def match_strategies(candle_data):
    strategies = [
        wick_trap_strategy,
        bullish_engulfing,
        # ... Add all 50 strategy functions
    ]

    matched = []
    for strategy in strategies:
        result, explanation = strategy(candle_data)
        if result:
            matched.append(explanation)

    if matched:
        return "Buy" if "Bullish" in matched[0] else "Sell", matched
    else:
        return "No Trade", []

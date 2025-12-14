def calculate_commission_rate(
    tier: int,
    base_rate: float = 0.50,
    base_gain: float = 0.02,
    tiers_per_halving: int = 5,
    min_rate: float = 0.50,
    max_rate: float = 0.70,
    halvings = (tier - 1) // tiers_per_halving
    gain = base_gain * (0.5 ** halvings)
    raw_rate = base_rate + gain * tier
    return max(min_rate, min(raw_rate, max_rate))


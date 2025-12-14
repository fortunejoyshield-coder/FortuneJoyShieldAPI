def required_sales_for_next_tier(tier: int, base: float = 100) -> float:
    if tier <= 10:
        return base * (1.5 ** tier)

    elif tier <= 20:
        return base * (1.5 ** 10) * base * ((tier - 10) ** 2)

    else:
        return (
            base * (1.5 ** 10)
             *base * (10 ** 2)
            * base * 50 * (tier - 20)
        )


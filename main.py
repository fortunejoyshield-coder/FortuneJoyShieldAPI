from fastapi import FastAPI
from commission_engine import calculate_commission_rate

app = FastAPI(
    title="Fortune Joy Shield API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"status": "Fortune Joy Shield API is live"}

@app.get("/commission")
def get_commission_rate(tier: int):
    rate = calculate_commission_rate(tier)
    return {
        "tier": tier,
        "commission_rate": rate,
        "commission_percent": rate * 100
    }

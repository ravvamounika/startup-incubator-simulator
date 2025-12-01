from adk import Tool
import math
import random

def financial_model_tool():
    @Tool(
        name="financial_model_tool",
        description="Generate a 3-year financial projection using Python."
    )
    async def run(startup_idea: str):
        """
        Simple example financial model:
        Revenue grows at 30% YoY
        Costs grow at 20% YoY
        """
        base_revenue = random.randint(200000, 600000)
        base_cost = random.randint(120000, 300000)

        projections = []

        for year in range(3):
            revenue = math.floor(base_revenue * (1.3 ** year))
            cost = math.floor(base_cost * (1.2 ** year))
            profit = revenue - cost

            projections.append({
                "year": f"Year {year + 1}",
                "revenue": revenue,
                "cost": cost,
                "profit": profit
            })

        return {
            "startup_idea": startup_idea,
            "projections": projections
        }

    return run

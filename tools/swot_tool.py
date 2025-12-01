from adk import Tool

def swot_tool():
    @Tool(name="swot_tool", description="Generate SWOT analysis.")
    async def run(startup_idea: str):
        strengths = [
            f"Clear value proposition for {startup_idea}",
            "Large potential market",
            "High scalability"
        ]
        weaknesses = [
            "Requires customer education",
            "Potentially high initial development cost"
        ]
        opportunities = [
            "Adjacent vertical expansions",
            "Partnerships with enterprise platforms"
        ]
        threats = [
            "Competitors with larger budgets",
            "Regulatory barriers"
        ]

        return {
            "startup_idea": startup_idea,
            "strengths": strengths,
            "weaknesses": weaknesses,
            "opportunities": opportunities,
            "threats": threats
        }

    return run

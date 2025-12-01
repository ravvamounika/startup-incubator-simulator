from adk import agent, AgentContext
from tools.swot_tool import swot_tool

@agent(
    name="product_manager_agent",
    description="Generates personas, user needs, features, roadmap, and SWOT.",
    tools=[swot_tool()]
)
async def product_manager_agent(ctx: AgentContext, startup_idea: str):
    ctx.logger.info("[Product Manager] Creating PRD and user insights.")

    # Use SWOT tool
    swot = await ctx.tools.swot_tool(startup_idea)

    personas = [
        {"name": "Primary User", "goals": ["Achieve X", "Solve Y"], "pain_points": ["Pain A", "Pain B"]},
        {"name": "Secondary User", "goals": ["Achieve Z"], "pain_points": ["Barrier C"]},
    ]

    features = [
        "Core Functionality",
        "Onboarding Flow",
        "Analytics Dashboard",
        "Premium Tier Features"
    ]

    roadmap = {
        "Q1": ["MVP", "Core Feature A"],
        "Q2": ["Feature B", "Growth Optimization"],
        "Q3": ["Monetization Layer"],
    }

    return {
        "agent": "Product Manager",
        "personas": personas,
        "feature_list": features,
        "roadmap": roadmap,
        "swot_analysis": swot,
        "summary": f"Created personas, user needs, features, roadmap, and SWOT for '{startup_idea}'."
    }

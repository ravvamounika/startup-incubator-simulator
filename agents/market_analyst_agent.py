from adk import agent, AgentContext
from tools.tam_sam_som_tool import tam_sam_som_tool
from tools.competitor_lookup_tool import competitor_lookup_tool
from memory.longterm_memory import longterm_memory

@agent(
    name="market_analyst_agent",
    description="Analyzes market size, competitors, trends, and risks.",
    tools=[tam_sam_som_tool(), competitor_lookup_tool()],
)
async def market_analyst_agent(ctx: AgentContext, startup_idea: str):
    """Analyze market opportunity and competition"""
    ctx.logger.info("[Market Analyst] Starting market evaluation.")

    # Calculate market size
    market_model = await ctx.tools.tam_sam_som_tool(startup_idea)

    # Find competitors
    competitors = await ctx.tools.competitor_lookup_tool(startup_idea)

    # Check past analyses
    prior = longterm_memory.retrieve_similar("market_analysis", startup_idea)

    analysis = {
        "agent": "Market Analyst",
        "tam_sam_som": market_model,
        "competitors": competitors,
        "prior_insights": prior,
        "summary": f"Market assessment for '{startup_idea}'."
    }

    # Save to memory
    longterm_memory.store("market_analysis", analysis)

    return analysis

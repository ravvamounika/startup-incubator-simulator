from adk import agent, AgentContext
from tools.pitchdeck_longrun_tool import pitchdeck_longrun_tool

@agent(
    name="pitchdeck_agent",
    description="Generates a pitch deck outline from the compiled report.",
    tools=[pitchdeck_longrun_tool()]
)
async def pitchdeck_agent(ctx: AgentContext, report_text: str):
    """
    Converts the startup report into a 10-slide pitch deck outline.
    """
    ctx.logger.info("[Pitch Deck Agent] Generating pitch deck...")

    # Use long-running pitch deck tool
    deck = await ctx.tools.pitchdeck_longrun_tool(report_text)

    return {
        "agent": "Pitch Deck Agent",
        "pitch_deck": deck,
        "summary": f"Generated {len(deck.get('slides', []))} slide pitch deck."
    }


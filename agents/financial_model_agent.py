from adk import agent, AgentContext
from tools.financial_model_tool import financial_model_tool

@agent(
    name="financial_model_agent",
    description="Generates financial projections using Python execution.",
    tools=[financial_model_tool()]
)
async def financial_model_agent(ctx: AgentContext, startup_idea: str):
    ctx.logger.info("[Financial Model Agent] Building financial forecast.")

    projections = await ctx.tools.financial_model_tool(startup_idea)

    return {
        "agent": "Financial Model Agent",
        "projections": projections,
        "summary": "Generated 3-year financial model with revenue and cost estimates."
    }

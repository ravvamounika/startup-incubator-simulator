from adk import agent, AgentContext
from memory.longterm_memory import longterm_memory

@agent(
    name="vc_investor_agent",
    description="Provides investment thesis, risks, valuation reasoning, and scoring.",
)
async def vc_investor_agent(ctx: AgentContext, startup_idea: str):
    ctx.logger.info("[VC Investor] Evaluating business potential.")

    # Check past investments stored in memory
    historical_patterns = longterm_memory.retrieve_similar("vc_thesis", startup_idea)

    score = ctx.llm(
        f"Evaluate this startup idea as a VC and give a numeric score 1-10:\n{startup_idea}"
    )

    thesis = ctx.llm(
        f"""
        As a VC partner, write an investment thesis for:
        '{startup_idea}'.
        Include risks, validation requirements, and growth potential.
        """
    )

    result = {
        "agent": "VC Investor",
        "investment_thesis": thesis,
        "score": score,
        "memory_reference": historical_patterns,
        "summary": f"VC evaluation: score={score}"
    }

    longterm_memory.store("vc_thesis", result)

    return result

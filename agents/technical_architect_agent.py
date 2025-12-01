from adk import agent, AgentContext
from memory.longterm_memory import longterm_memory

@agent(
    name="technical_architect_agent",
    description="Creates architecture, estimates complexity, recommends stack.",
)
async def technical_architect_agent(ctx: AgentContext, startup_idea: str):
    ctx.logger.info("[Technical Architect] Designing system.")

    architecture = ctx.llm(
        f"""
        Propose a scalable system architecture for '{startup_idea}'.
        Include: API layer, database, data pipelines, ML components (if any),
        devops recommendations, and cost considerations.
        """
    )

    stack = ctx.llm(
        f"Recommend an optimal tech stack for '{startup_idea}' with justification."
    )

    complexity = ctx.llm(
        "Estimate complexity (Low/Medium/High) and why."
    )

    result = {
        "agent": "Technical Architect",
        "architecture": architecture,
        "tech_stack": stack,
        "complexity": complexity,
    }

    longterm_memory.store("tech_design", result)

    return result

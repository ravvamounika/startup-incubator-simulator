from adk import agent, AgentContext

@agent(
    name="report_compiler_agent",
    description="Compiles outputs from all Phase 1 agents into a unified startup report.",
)
async def report_compiler_agent(ctx: AgentContext, agent_outputs: list):
    """
    Takes outputs from all parallel agents and creates a cohesive report.
    """
    ctx.logger.info("[Report Compiler] Compiling startup evaluation report...")

    # Combine all agent outputs
    report_sections = []
    
    for output in agent_outputs:
        agent_name = output.get("agent", "Unknown")
        summary = output.get("summary", "No summary available")
        report_sections.append(f"\n## {agent_name}\n{summary}")
    
    # Create final report
    final_report = "\n".join(report_sections)
    
    return {
        "agent": "Report Compiler",
        "report": final_report,
        "summary": f"Compiled report from {len(agent_outputs)} expert agents."
    }


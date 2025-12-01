from adk import Tool
import random

def competitor_lookup_tool():
    @Tool(
        name="competitor_lookup_tool",
        description="Find competitors using MCP search and rank them."
    )
    async def run(startup_idea: str, ctx=None):
        """
        MCP Search: ctx.tools.mcp.search(query)
        Simulated: Real MCP tool integration in ADK would be ctx.tools.<something>
        """
        query = f"competitors for {startup_idea}"

        # Simulated search response, you would call MCP search tool here
        competitors = [
            f"Competitor {random.choice(['A','B','C'])} for {startup_idea}",
            f"Competitor {random.choice(['X','Y','Z'])} for {startup_idea}",
            f"Competitor {random.randint(1, 50)} for {startup_idea}"
        ]

        ranked = sorted(competitors)

        return {
            "query": query,
            "competitors_ranked": ranked
        }

    return run

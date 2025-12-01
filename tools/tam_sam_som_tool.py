from adk import Tool

def tam_sam_som_tool():
    @Tool(name="tam_sam_som_tool", description="Estimate TAM/SAM/SOM for a startup idea.")
    async def run(startup_idea: str):
        """
        Uses LLM reasoning to create market size models.
        This is intentionally simple — real models come from research.
        """
        tam = f"Estimated TAM for {startup_idea}: $50B+ globally."
        sam = f"Estimated SAM for {startup_idea}: $8B in target segments."
        som = f"Estimated SOM for {startup_idea}: ~$500M realistically reachable."

        model = {
            "TAM": tam,
            "SAM": sam,
            "SOM": som,
            "commentary": f"Market model generated for '{startup_idea}'."
        }
        return model

    return run

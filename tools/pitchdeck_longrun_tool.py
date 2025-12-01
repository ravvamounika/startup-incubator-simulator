from adk import LongRunningTool
import asyncio

def pitchdeck_longrun_tool():
    """Long-running tool for generating pitch decks"""
    
    @LongRunningTool(
        name="pitchdeck_longrun_tool",
        description="Generate pitch deck slide-by-slide."
    )
    async def run(report_text: str, progress=None):
        """Generate 10 pitch deck slides incrementally"""
        slides = []
        total_slides = 10

        for i in range(total_slides):
            await asyncio.sleep(0.5)  # Simulate generation time
            slide = f"Slide {i+1}: Key insights from report section {i+1}"
            slides.append(slide)

            if progress:
                await progress(f"Generated slide {i+1}/{total_slides}")

        return {
            "slides": slides,
            "status": "Pitch deck generation complete.",
            "total_slides": total_slides
        }

    return run

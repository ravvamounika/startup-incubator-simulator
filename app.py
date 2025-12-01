"""
Startup Incubator Simulator
Multi-agent system for evaluating startup ideas
"""

import asyncio

from agents.market_analyst_agent import market_analyst_agent
from agents.product_manager_agent import product_manager_agent
from agents.vc_investor_agent import vc_investor_agent
from agents.technical_architect_agent import technical_architect_agent
from agents.financial_model_agent import financial_model_agent
from agents.context_compactor_agent import context_compactor_agent
from tools.pitchdeck_longrun_tool import pitchdeck_longrun_tool
from memory.session_manager import session_manager
from memory.longterm_memory import longterm_memory
from observability.logging_middleware import LoggingMiddleware
from observability.metrics_middleware import MetricsMiddleware
from observability.tracing_middleware import TracingMiddleware


class StartupIncubatorSimulator:
    """Orchestrates multiple agents to evaluate startup ideas"""
    
    def __init__(self, startup_idea: str):
        self.startup_idea = startup_idea
        self.session_id = f"session_{startup_idea.replace(' ', '_')}"
        
        # Set up logging and metrics
        self.logger = LoggingMiddleware("IncubatorSimulator")
        self.metrics = MetricsMiddleware()
        self.tracer = TracingMiddleware()

        # Create session for this evaluation
        session_manager.create_session(self.session_id)

    async def run_parallel_agents(self):
        """Run all 5 expert agents concurrently"""
        self.logger.info("Launching parallel expert agents...")
        self.metrics.start_timer("parallel_agents")
        trace = self.tracer.start_trace("parallel_agents", {"startup_idea": self.startup_idea})

        # Run agents in parallel
        results = await asyncio.gather(
            market_analyst_agent(self.startup_idea),
            product_manager_agent(self.startup_idea),
            vc_investor_agent(self.startup_idea),
            technical_architect_agent(self.startup_idea),
            financial_model_agent(self.startup_idea)
        )

        self.tracer.end_trace(trace)
        elapsed = self.metrics.stop_timer("parallel_agents")
        self.logger.info(f"Parallel agents finished in {elapsed:.2f}s")
        return results

    async def generate_pitch_deck(self, report_text: str):
        """Generate pitch deck from compiled report"""
        self.logger.info("Generating pitch deck...")
        pitch_tool = pitchdeck_longrun_tool()
        deck_result = await pitch_tool(report_text)
        return deck_result

    async def compact_context(self):
        """Compact old memory to save space"""
        self.logger.info("Compacting context...")
        result = await context_compactor_agent(category="vc_thesis")
        return result

    async def run(self):
        """Run the complete evaluation workflow"""
        # Run all expert agents in parallel
        agent_outputs = await self.run_parallel_agents()

        # Combine outputs into report
        report_text = "\n".join([str(output) for output in agent_outputs])

        # Generate pitch deck
        pitch_deck = await self.generate_pitch_deck(report_text)

        # Compact old memory
        compacted = await self.compact_context()

        # Return results
        final_result = {
            "startup_idea": self.startup_idea,
            "agent_outputs": agent_outputs,
            "pitch_deck": pitch_deck,
            "context_compaction": compacted,
        }

        self.logger.info("Simulation complete!")
        return final_result


if __name__ == "__main__":
    # Example startup idea
    startup_idea = "AI-Powered Personal Health Assistant"

    # Run simulation
    simulator = StartupIncubatorSimulator(startup_idea=startup_idea)
    final_result = asyncio.run(simulator.run())

    # Print summary
    print("\n=== Simulation Summary ===")
    print(f"Startup Idea: {final_result['startup_idea']}")
    print(f"Agent Outputs: {len(final_result['agent_outputs'])} agents completed")
    print(f"Pitch Deck Slides: {len(final_result['pitch_deck']['slides'])}")
    print(f"Context Compaction Summary: {final_result['context_compaction']['summary']}")

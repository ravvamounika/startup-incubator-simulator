from adk import agent

@agent(
    name="context_compactor_agent",
    description="Summarizes old session or long-term memory for efficient context."
)
async def context_compactor_agent(ctx, category: str, max_items=5):
    """
    Takes a category from long-term memory and compresses older items.
    """
    from memory.longterm_memory import longterm_memory

    all_items = longterm_memory.retrieve(category)
    if not all_items:
        return {"summary": f"No items to compact in category {category}"}

    # Only keep the most recent max_items
    compacted_items = all_items[-max_items:]

    # Optional: generate textual summary using LLM
    summary_text = await ctx.llm(f"Summarize the following items concisely: {compacted_items}")

    # Replace old memory with compacted summary
    longterm_memory.memory_bank[category] = [{"summary": summary_text}]
    
    return {"category": category, "summary": summary_text}

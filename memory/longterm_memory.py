class LongTermMemory:
    """Stores agent analyses across sessions"""
    
    def __init__(self):
        self.memory_bank = {}

    def store(self, category: str, item: dict):
        """Store analysis in a category"""
        if category not in self.memory_bank:
            self.memory_bank[category] = []
        self.memory_bank[category].append(item)

    def retrieve(self, category: str):
        """Get all items from a category"""
        return self.memory_bank.get(category, [])

    def retrieve_similar(self, category: str, query: str, top_n=3):
        """Find similar past analyses using keyword matching"""
        if category not in self.memory_bank:
            return []

        # Score by keyword overlap
        scored = []
        for item in self.memory_bank[category]:
            text = str(item)
            score = sum(1 for word in query.lower().split() if word in text.lower())
            scored.append((score, item))

        scored.sort(reverse=True, key=lambda x: x[0])
        return [item for score, item in scored[:top_n]]


longterm_memory = LongTermMemory()

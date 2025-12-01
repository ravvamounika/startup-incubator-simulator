class SessionManager:
    def __init__(self):
        # In-memory session dictionary
        self.sessions = {}

    def create_session(self, session_id: str):
        self.sessions[session_id] = {}
        return self.sessions[session_id]

    def get_session(self, session_id: str):
        return self.sessions.get(session_id, None)

    def set(self, session_id: str, key: str, value):
        if session_id not in self.sessions:
            self.create_session(session_id)
        self.sessions[session_id][key] = value

    def get(self, session_id: str, key: str):
        return self.sessions.get(session_id, {}).get(key, None)

    def clear_session(self, session_id: str):
        if session_id in self.sessions:
            del self.sessions[session_id]

# Singleton instance
session_manager = SessionManager()

import logging

logging.basicConfig(
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s'
)

class LoggingMiddleware:
    """Agent-specific logging"""
    
    def __init__(self, agent_name=""):
        self.agent_name = agent_name
        self.logger = logging.getLogger(agent_name)

    def info(self, message: str):
        self.logger.info(f"[{self.agent_name}] {message}")

    def warning(self, message: str):
        self.logger.warning(f"[{self.agent_name}] {message}")

    def error(self, message: str):
        self.logger.error(f"[{self.agent_name}] {message}")

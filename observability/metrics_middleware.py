import time

class MetricsMiddleware:
    def __init__(self):
        # Store metrics: {agent_name: {metric_name: value}}
        self.metrics = {}

    def start_timer(self, agent_name: str, metric_name="execution_time"):
        start_time = time.time()
        self.metrics.setdefault(agent_name, {})[metric_name] = start_time

    def stop_timer(self, agent_name: str, metric_name="execution_time"):
        start_time = self.metrics.get(agent_name, {}).get(metric_name, None)
        if start_time:
            elapsed = time.time() - start_time
            self.metrics[agent_name][metric_name] = elapsed
            return elapsed
        return None

    def increment(self, agent_name: str, metric_name: str, amount=1):
        self.metrics.setdefault(agent_name, {}).setdefault(metric_name, 0)
        self.metrics[agent_name][metric_name] += amount

    def report(self):
        return self.metrics

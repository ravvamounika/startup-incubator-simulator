import time

class TracingMiddleware:
    def __init__(self):
        self.traces = []

    def start_trace(self, agent_name: str, context_info=None):
        trace = {
            "agent": agent_name,
            "start_time": time.time(),
            "context": context_info,
            "end_time": None
        }
        self.traces.append(trace)
        return trace

    def end_trace(self, trace):
        trace["end_time"] = time.time()
        trace["duration"] = trace["end_time"] - trace["start_time"]

    def report(self):
        return self.traces

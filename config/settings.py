"""
Configuration settings for Startup Incubator Simulator
"""
import os

# LLM Model Configuration - Using Gemini for bonus points!
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.0-flash-exp")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Note: To use Gemini, set your API key as an environment variable:
# export GEMINI_API_KEY="your_api_key_here"
# Get your key from: https://aistudio.google.com/app/apikey

# Agent Configuration
MAX_PARALLEL_AGENTS = 5
AGENT_TIMEOUT = 300  # seconds

# Memory Configuration
MAX_MEMORY_ITEMS = 100
CONTEXT_COMPACTION_THRESHOLD = 50

# Observability Configuration
LOG_LEVEL = "INFO"
ENABLE_METRICS = True
ENABLE_TRACING = True

# Tool Configuration
PITCH_DECK_SLIDES = 10
FINANCIAL_PROJECTION_YEARS = 3


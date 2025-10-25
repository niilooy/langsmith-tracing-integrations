# Google ADK Demo

Google ADK (Generative AI Development Kit) integration with LangSmith tracing using OpenInference instrumentation.

## Prerequisites

- Python 3.13+
- Google API credentials configured
- LangSmith API key ([Get one here](https://smith.langchain.com/))

## Setup

### 1. Install dependencies

From the **root directory** of the project:

```bash
uv sync
```

### 2. Configure environment variables

Set up your environment variables in [agents/.env](agents/.env):

```bash
cd google-adk-demo/agents
# Add your API keys to .env file
```

Required environment variables:
```env
GOOGLE_API_KEY=your_google_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=google-adk-demo
LANGSMITH_TRACING=true
```

## Running

Run the example agent:

```bash
cd google-adk-demo
uv run python agents/agent.py
```

## What's Included

- **[agents/agent.py](agents/agent.py)**: Google ADK agent implementation with LangSmith tracing
- Automatic trace logging to LangSmith dashboard
- Complete execution flow visibility

## How It Works

The integration uses OpenInference instrumentation to automatically capture traces:

```python
from openinference.instrumentation.google_adk import GoogleADKInstrumentor
from langsmith import Client

# Initialize LangSmith client
client = Client()

# Instrument Google ADK
GoogleADKInstrumentor().instrument()

# Your ADK agent code runs here
# All operations are automatically traced
```

This automatically captures:
- Agent execution flow
- Tool usage and results
- Model interactions
- Performance metrics
- Input/output data

## Viewing Traces

After running your agent:
1. Go to [LangSmith dashboard](https://smith.langchain.com/)
2. Navigate to your project (e.g., "google-adk-demo")
3. View the execution traces with full details including:
   - Complete agent workflow
   - Step-by-step execution
   - Timing information
   - Model calls and responses

## Project Structure

```
google-adk-demo/
├── agents/
│   ├── __init__.py
│   ├── agent.py          # Main agent implementation
│   └── .env              # Environment variables (not in git)
├── observations          # Output/logs from agent runs
├── pyproject.toml        # Dependencies
└── README.md
```

## Troubleshooting

### Import Errors

Make sure all dependencies are installed:
```bash
# From root directory
uv sync --all-packages
```

### Google API Authentication

Ensure you have valid Google API credentials configured. Check the [Google ADK documentation](https://developers.google.com/adk) for setup instructions.

### LangSmith Not Showing Traces

Verify your environment variables:
- `LANGSMITH_API_KEY` is set correctly
- `LANGSMITH_TRACING` is set to `true`
- Check your project name matches in LangSmith dashboard

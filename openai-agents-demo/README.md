# OpenAI Agents Demo

OpenAI Agents SDK integration with LangSmith tracing.

## Prerequisites

- Python 3.13+
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- LangSmith API key ([Get one here](https://smith.langchain.com/))

## Setup

### 1. Install dependencies

From the **root directory** of the project:

```bash
uv sync
```

### 2. Configure environment variables

Copy the example environment file and fill in your API keys:

```bash
cd openai-agents-demo
cp .env.example .env
```

Edit `.env` and add your keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=openai-agents-demo
LANGSMITH_TRACING=true
```

## Running

Run the example agent:

```bash
cd openai-agents-demo
uv run python agents/agent.py
```

## What's Included

- **[agents/agent.py](agents/agent.py)**: Simple weather assistant agent with LangSmith tracing
- Automatic trace logging to LangSmith dashboard
- Complete execution flow visibility

## How It Works

The integration uses `OpenAIAgentsTracingProcessor` from LangSmith to automatically capture:
- Agent execution flow
- All spans and their details
- Input/output data
- Performance metrics

```python
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor
from openai.agents import set_trace_processors

# Enable tracing
set_trace_processors([OpenAIAgentsTracingProcessor()])
```

## Viewing Traces

After running your agent:
1. Go to [LangSmith dashboard](https://smith.langchain.com/)
2. Navigate to your project (e.g., "openai-agents-demo")
3. View the execution traces with full details including:
   - Agent execution steps
   - Model interactions
   - Input/output data
   - Timing information
   - Token usage

## Code Example

The example agent is a simple weather assistant that demonstrates the integration:

```python
import asyncio
from agents import Agent, Runner, set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor

async def main():
    # Create agent
    agent = Agent(
        name="weather-assistant",
        instructions="You are a helpful assistant.",
    )

    # Run with tracing
    result = await Runner.run(agent, "What's the weather like?")
    print(result.final_output)

if __name__ == "__main__":
    set_trace_processors([OpenAIAgentsTracingProcessor()])
    asyncio.run(main())
```

## Project Structure

```
openai-agents-demo/
├── agents/
│   ├── __init__.py
│   └── agent.py          # Main agent implementation
├── .env.example          # Environment variables template
├── .gitignore
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

### Module Not Found: openai.agents

The correct import is from `agents`, not `openai.agents`:
```python
from agents import Agent, Runner, set_trace_processors
```

### LangSmith Not Showing Traces

Verify your environment variables:
- `OPENAI_API_KEY` is set correctly
- `LANGSMITH_API_KEY` is set correctly
- `LANGSMITH_TRACING` is set to `true`
- Check your project name matches in LangSmith dashboard

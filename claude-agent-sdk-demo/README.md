# Claude Agent SDK Demo

Claude Agent SDK integration with LangSmith tracing using the native integration.

## Prerequisites

- Python 3.13+
- Anthropic API key ([Get one here](https://console.anthropic.com/))
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
cd claude-agent-sdk-demo
cp .env.example .env
```

Edit `.env` and add your keys:
```env
ANTHROPIC_API_KEY=your_anthropic_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=claude-agent-sdk-demo
LANGSMITH_TRACING=true
```

## Running

Run the example agent:

```bash
cd claude-agent-sdk-demo
uv run python agents/agent.py
```

## What's Included

- **[agents/agent.py](agents/agent.py)**: Simple research assistant agent with LangSmith tracing
- Automatic trace logging to LangSmith dashboard
- Complete execution flow visibility

## How It Works

The integration uses the native LangSmith configuration for Claude Agent SDK:

```python
from anthropic import Anthropic
from claude_agent_sdk import ClaudeSDKClient
from langsmith.integrations.claude_agent_sdk import configure_claude_agent_sdk

# Configure LangSmith tracing BEFORE creating the client
configure_claude_agent_sdk()

# Create Anthropic and Claude SDK clients
anthropic_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
client = ClaudeSDKClient(anthropic_client=anthropic_client)

# Run the agent - all operations are automatically traced
response = client.run(
    agent_name="research-assistant",
    prompt="Your query here",
    model="claude-3-5-sonnet-20241022",
)
```

**Important:** Call `configure_claude_agent_sdk()` before creating your `ClaudeSDKClient` instance to ensure all operations are traced.

This automatically captures:
- Agent queries and responses
- Tool invocations and results
- Claude model interactions
- MCP server operations
- Performance metrics

## Viewing Traces

After running your agent:
1. Go to [LangSmith dashboard](https://smith.langchain.com/)
2. Navigate to your project (e.g., "claude-agent-sdk-demo")
3. View the execution traces with full details including:
   - Complete agent workflow
   - Model interactions
   - Tool usage
   - Timing information
   - Token usage

## Project Structure

```
claude-agent-sdk-demo/
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

### Anthropic API Authentication

Ensure you have a valid Anthropic API key:
- Sign up at [console.anthropic.com](https://console.anthropic.com/)
- Generate an API key
- Add it to your `.env` file

### LangSmith Not Showing Traces

Verify your environment variables:
- `ANTHROPIC_API_KEY` is set correctly
- `LANGSMITH_API_KEY` is set correctly
- `LANGSMITH_TRACING` is set to `true`
- Check your project name matches in LangSmith dashboard

### Module Not Found Errors

If you see import errors for `claude_agent_sdk`, ensure you installed with the Claude Agent SDK extra:
```bash
# From root directory
uv sync --all-packages
```

The `langsmith[claude-agent-sdk]` dependency in pyproject.toml includes the Claude Agent SDK package.

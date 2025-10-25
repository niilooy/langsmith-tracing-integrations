# LangSmith Tracing Integrations

>This repository is based on the [LangSmith Integrations documentation](https://docs.langchain.com/langsmith/integrations).

A unified UV workspace for testing and demonstrating LangSmith tracing integrations with various AI frameworks.

This project contains working examples of LangSmith tracing integration for:
- **Google ADK** (Generative AI Development Kit)
- **OpenAI Agents SDK** (Official OpenAI Agents framework)
- **CrewAI** (Multi-agent orchestration framework)
- **Claude Agent SDK** (Anthropic's Claude Agent framework)

## Project Structure

This is a UV workspace containing multiple framework integrations:

```
langsmith-tracing-integrations/
├── .python-version             # Python version (3.13)
├── pyproject.toml              # Root workspace configuration
├── uv.lock                     # Unified lock file for all dependencies
├── .venv/                      # Shared virtual environment
├── google-adk-demo/            # Google ADK integration
│   ├── pyproject.toml
│   ├── agents/
│   └── observations
├── openai-agents-demo/         # OpenAI Agents SDK integration
│   ├── pyproject.toml
│   ├── agents/
│   └── .env.example
├── crewai-demo/                # CrewAI integration
│   ├── pyproject.toml
│   ├── agents/
│   └── .env.example
├── claude-agent-sdk-demo/      # Claude Agent SDK integration
│   ├── pyproject.toml
│   ├── agents/
│   └── .env.example
└── README.md
```

## Prerequisites

- Python 3.13+ (required for compatibility with all frameworks)
- UV package manager
- API keys for the frameworks you want to use:
  - [OpenAI API key](https://platform.openai.com/api-keys) (for OpenAI Agents and CrewAI)
  - [Anthropic API key](https://console.anthropic.com/) (for Claude Agent SDK)
  - [LangSmith API key](https://smith.langchain.com/) (for all integrations)

## Quick Start

1. **Navigate to the project root:**
   ```bash
   cd langsmith-tracing-integrations
   ```

2. **Install all dependencies:**
   ```bash
   uv sync
   ```
   This creates a single `.venv` at the root level with all dependencies from all workspace members.

3. **Set up environment variables** (for OpenAI Agents, CrewAI, and Claude Agent SDK):
   ```bash
   # For OpenAI Agents
   cd openai-agents-demo
   cp .env.example .env
   # Edit .env with your API keys

   # For CrewAI
   cd ../crewai-demo
   cp .env.example .env
   # Edit .env with your API keys

   # For Claude Agent SDK
   cd ../claude-agent-sdk-demo
   cp .env.example .env
   # Edit .env with your API keys
   ```

4. **Run any demo:**
   ```bash
   # From root directory
   cd google-adk-demo && uv run python agents/agent.py
   # OR
   cd openai-agents-demo && uv run python agents/agent.py
   # OR
   cd crewai-demo && uv run python agents/agent.py
   # OR
   cd claude-agent-sdk-demo && uv run python agents/agent.py
   ```

## Framework Integrations

### 1. Google ADK Demo

**What it does:** Demonstrates Google's Generative AI Development Kit with LangSmith tracing using OpenInference instrumentation.

**Running:**
```bash
cd google-adk-demo
uv run python agents/agent.py
```

**Tracing method:** OpenInference instrumentation
- Uses `OpenInferenceInstrumentor` from `openinference-instrumentation-google-adk`
- Automatically captures ADK agent execution flow

**Documentation:** See [google-adk-demo/README.md](google-adk-demo/README.md)

---

### 2. OpenAI Agents SDK Demo

**What it does:** Demonstrates OpenAI's official Agents SDK with LangSmith tracing using the native integration.

**Setup & Running:**
```bash
cd openai-agents-demo
cp .env.example .env  # First time only
# Edit .env with OPENAI_API_KEY and LANGSMITH_API_KEY
uv run python agents/agent.py
```

**Tracing method:** Native OpenAI Agents integration
- Uses `OpenAIAgentsTracingProcessor` from `langsmith.integrations.openai_agents_sdk`
- Captures agent execution, tool calls, and model interactions

**Documentation:** See [openai-agents-demo/README.md](openai-agents-demo/README.md)

---

### 3. CrewAI Demo

**What it does:** Demonstrates CrewAI multi-agent orchestration with LangSmith tracing using OpenTelemetry instrumentation.

**Setup & Running:**
```bash
cd crewai-demo
cp .env.example .env  # First time only
# Edit .env with OPENAI_API_KEY and LANGSMITH_API_KEY
uv run python agents/agent.py
```

**Tracing method:** OpenTelemetry instrumentation
- Uses `OtelSpanProcessor` from `langsmith.integrations.otel`
- Uses `CrewAIInstrumentor` and `OpenAIInstrumentor`
- Captures complete crew workflow, agent interactions, and task execution

**Documentation:** See [crewai-demo/README.md](crewai-demo/README.md)

---

### 4. Claude Agent SDK Demo

**What it does:** Demonstrates Anthropic's Claude Agent SDK with LangSmith tracing using the native integration.

**Setup & Running:**
```bash
cd claude-agent-sdk-demo
cp .env.example .env  # First time only
# Edit .env with ANTHROPIC_API_KEY and LANGSMITH_API_KEY
uv run python agents/agent.py
```

**Tracing method:** Native Claude Agent SDK integration
- Uses `configure_claude_agent_sdk()` from `langsmith.integrations.claude_agent_sdk`
- Automatically captures agent queries, tool invocations, model interactions, and MCP server operations
- Must be called before creating `ClaudeSDKClient`

**Documentation:** See [claude-agent-sdk-demo/README.md](claude-agent-sdk-demo/README.md)

## Adding New Framework Integrations

1. Create a new directory for the framework:
   ```bash
   mkdir new-framework-demo
   ```

2. Create a `pyproject.toml` in the new directory:
   ```toml
   [project]
   name = "new-framework-demo"
   version = "0.1.0"
   description = "Description of the integration"
   requires-python = ">=3.13"
   dependencies = [
       "langsmith>=0.4.38",
       # Add framework-specific dependencies
   ]
   ```

3. Add the new directory to the workspace members in the root `pyproject.toml`:
   ```toml
   [tool.uv.workspace]
   members = ["google-adk-demo", "openai-agents-demo", "crewai-demo", "claude-agent-sdk-demo", "new-framework-demo"]
   ```

4. Run `uv sync` from the root to update dependencies.

## Viewing Traces in LangSmith

After running any demo:

1. Go to [LangSmith dashboard](https://smith.langchain.com/)
2. Navigate to your project (e.g., "google-adk-demo", "openai-agents-demo", "crewai-demo", or "claude-agent-sdk-demo")
3. View the execution traces with:
   - Complete execution flow
   - Input/output data
   - Timing information
   - Token usage (for LLM calls)
   - Error tracking

## Troubleshooting

### Python Version Issues

This project requires **Python 3.13** due to CrewAI dependencies (specifically `onnxruntime`). If you see errors about Python version:

```bash
# Check your Python version
python3 --version

# If needed, install Python 3.13 via Homebrew (macOS)
brew install python@3.13

# Verify UV is using the correct Python
uv python list
```

### Missing Dependencies

If you encounter import errors:

```bash
# From root directory
rm -rf .venv
uv sync --all-packages
```

### Environment Variables

Make sure you've created `.env` files with valid API keys for OpenAI Agents, CrewAI, and Claude Agent SDK demos:

```env
# For OpenAI Agents and CrewAI
OPENAI_API_KEY=sk-...
LANGSMITH_API_KEY=ls__...
LANGSMITH_PROJECT=your-project-name
LANGSMITH_TRACING=true

# For Claude Agent SDK
ANTHROPIC_API_KEY=sk-ant-...
LANGSMITH_API_KEY=ls__...
LANGSMITH_PROJECT=your-project-name
LANGSMITH_TRACING=true
```

## Benefits of This Structure

- **Single dependency management**: All dependencies managed in one `uv.lock` file
- **Shared virtual environment**: One `.venv` for all frameworks
- **Independent execution**: Each framework can be run separately
- **Easy to add new frameworks**: Just add a new directory and update workspace members
- **Reproducible builds**: Lock file ensures consistent dependencies across all frameworks
- **Python 3.13 compatibility**: All frameworks work with the same Python version

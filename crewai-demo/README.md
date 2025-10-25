# CrewAI Demo

CrewAI integration with LangSmith tracing using OpenTelemetry instrumentation.

## Prerequisites

- Python 3.13+ (required for CrewAI dependencies like `onnxruntime` and `chromadb`)
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
cd crewai-demo
cp .env.example .env
```

Edit `.env` and add your keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
LANGSMITH_API_KEY=your_langsmith_api_key_here
LANGSMITH_PROJECT=crewai-demo
LANGSMITH_TRACING=true
```

## Running

Run the example CrewAI workflow:

```bash
cd crewai-demo
uv run python agents/agent.py
```

## What's Included

- **[agents/agent.py](agents/agent.py)**: A multi-agent workflow with:
  - Research Analyst agent
  - Tech Writer agent
  - Sequential task execution
  - Full LangSmith tracing integration

## How It Works

The integration uses OpenTelemetry instrumentation to capture traces and send them to LangSmith:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from langsmith.integrations.otel import OtelSpanProcessor
from openinference.instrumentation.crewai import CrewAIInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor

# Set up tracing
tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)
tracer_provider.add_span_processor(OtelSpanProcessor())

# Activate instrumentors
CrewAIInstrumentor().instrument()
OpenAIInstrumentor().instrument()
```

This automatically captures:
- Agent execution flow
- Task progression
- LLM calls and responses
- Tool usage
- Performance metrics

## Viewing Traces

After running your crew:
1. Go to [LangSmith dashboard](https://smith.langchain.com/)
2. Navigate to your project (e.g., "crewai-demo")
3. View the execution traces with:
   - Complete workflow hierarchy
   - Individual agent actions
   - Task outputs
   - Timing information

## Advanced Usage

### Custom Metadata

Add custom metadata to your traces using OpenTelemetry spans:

```python
from opentelemetry import trace

current_span = trace.get_current_span()
current_span.set_attribute("langsmith.metadata.user_id", "user_123")
current_span.set_attribute("langsmith.metadata.environment", "production")
```

### Multiple Instrumentors

Combine CrewAI instrumentation with other tools:

```python
from openinference.instrumentation.crewai import CrewAIInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor
from openinference.instrumentation.dspy import DSPyInstrumentor

CrewAIInstrumentor().instrument()
OpenAIInstrumentor().instrument()
DSPyInstrumentor().instrument()
```

## Example Crew Workflow

The demo includes a multi-agent workflow:

```python
# Define agents
researcher = Agent(
    role='Research Analyst',
    goal='Gather comprehensive information about AI developments',
    backstory='You are an experienced research analyst...',
    verbose=True,
    allow_delegation=False
)

writer = Agent(
    role='Tech Writer',
    goal='Write engaging articles about technology',
    backstory='You are a skilled technical writer...',
    verbose=True,
    allow_delegation=False
)

# Define tasks
research_task = Task(
    description='Research the latest developments in AI agents',
    expected_output='A comprehensive summary',
    agent=researcher
)

write_task = Task(
    description='Write a brief article about AI agents',
    expected_output='A well-written article (2-3 paragraphs)',
    agent=writer
)

# Create and run crew
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff()
```

## Project Structure

```
crewai-demo/
├── agents/
│   ├── __init__.py
│   └── agent.py          # Multi-agent workflow implementation
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

### Python Version Issues

CrewAI requires Python 3.13 due to dependencies like `onnxruntime`. If you see compatibility errors:
```bash
python3 --version  # Should be 3.13.x
```

### LangSmith Not Showing Traces

Verify your environment variables:
- `OPENAI_API_KEY` is set correctly
- `LANGSMITH_API_KEY` is set correctly
- `LANGSMITH_TRACING` is set to `true`
- Check your project name matches in LangSmith dashboard

### ChromaDB or ONNX Runtime Errors

These dependencies are required by CrewAI. If you encounter issues:
```bash
# From root directory, reinstall with all packages
rm -rf .venv
uv sync --all-packages
```

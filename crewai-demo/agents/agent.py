"""CrewAI example with LangSmith tracing integration."""

import os
from crewai import Agent, Task, Crew, Process
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from langsmith.integrations.otel import OtelSpanProcessor
from openinference.instrumentation.crewai import CrewAIInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor


from dotenv import load_dotenv
load_dotenv()

def setup_tracing():
    """Set up OpenTelemetry tracing with LangSmith."""
    # Get or create a TracerProvider
    tracer_provider = trace.get_tracer_provider()
    if not isinstance(tracer_provider, TracerProvider):
        tracer_provider = TracerProvider()
        trace.set_tracer_provider(tracer_provider)

    # Add LangSmith's OtelSpanProcessor
    tracer_provider.add_span_processor(OtelSpanProcessor())

    # Activate instrumentors
    CrewAIInstrumentor().instrument()
    OpenAIInstrumentor().instrument()


def main():
    """Run a simple CrewAI workflow with LangSmith tracing."""
    # Set up tracing before running crew
    setup_tracing()

    # Define agents
    researcher = Agent(
        role='Research Analyst',
        goal='Gather comprehensive information about AI developments',
        backstory='You are an experienced research analyst with expertise in AI and technology trends.',
        verbose=True,
        allow_delegation=False
    )

    writer = Agent(
        role='Tech Writer',
        goal='Write engaging and informative articles about technology',
        backstory='You are a skilled technical writer who can explain complex topics clearly.',
        verbose=True,
        allow_delegation=False
    )

    # Define tasks
    research_task = Task(
        description='Research the latest developments in AI agents and summarize the key findings.',
        expected_output='A comprehensive summary of recent AI agent developments',
        agent=researcher
    )

    write_task = Task(
        description='Write a brief article about AI agents based on the research findings.',
        expected_output='A well-written article about AI agents (2-3 paragraphs)',
        agent=writer
    )

    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )

    # Run the crew
    print("Starting CrewAI workflow...\n")
    result = crew.kickoff()

    print("\n" + "="*60)
    print("FINAL RESULT:")
    print("="*60)
    print(result)
    print("\n✓ Crew execution completed. Check LangSmith for traces!")


if __name__ == "__main__":
    main()

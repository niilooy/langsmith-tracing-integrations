"""Simple OpenAI Agent with LangSmith tracing integration."""

import asyncio
from agents import Agent, Runner, set_trace_processors
from langsmith.integrations.openai_agents_sdk import OpenAIAgentsTracingProcessor

from dotenv import load_dotenv
load_dotenv()

async def main():
    """Run a simple agent with LangSmith tracing."""
    # Create a simple agent
    agent = Agent(
        model="gpt-5-nano",
        name="weather-assistant",
        instructions="You are a helpful assistant that provides weather information and general knowledge.",
    )

    # Test query
    query = "What's the weather like today in San Francisco?"
    print(f"Query: {query}\n")

    # Run the agent
    result = await Runner.run(agent, query)

    print(f"\nResponse: {result.final_output}")
    print("\n✓ Agent execution completed. Check LangSmith for traces!")


if __name__ == "__main__":
    # Set up LangSmith tracing before running
    set_trace_processors([OpenAIAgentsTracingProcessor()])

    # Run the async main function
    asyncio.run(main())

import asyncio
from google.adk import Runner
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Tracing is configured in src/__init__.py

# Define your tools
def get_flight_info(destination: str, departure_date: str) -> dict:
    """Get flight information for a destination."""
    return {
        "destination": destination,
        "departure_date": departure_date,
        "price": "$450",
        "duration": "5h 30m",
        "airline": "Example Airways"
    }

def get_hotel_recommendations(city: str, check_in: str) -> dict:
    """Get hotel recommendations for a city."""
    return {
        "city": city,
        "check_in": check_in,
        "hotels": [
            {"name": "Grand Plaza Hotel", "rating": 4.5, "price": "$120/night"},
            {"name": "City Center Inn", "rating": 4.2, "price": "$95/night"}
        ]
    }

# Create your ADK agent - this is what the ADK CLI looks for
root_agent = LlmAgent(
    name="travel_assistant",
    tools=[get_flight_info, get_hotel_recommendations],
    model="gemini-2.5-flash-lite",
    instruction="You are a helpful travel assistant that can help with flights and hotels.",
)

async def main():
    # Set up session service and runner
    session_service = InMemorySessionService()
    runner = Runner(
        app_name="travel_app",
        agent=root_agent,
        session_service=session_service
    )

    # Create a session
    user_id = "traveler_456"
    session_id = "session_789"
    await session_service.create_session(
        app_name="travel_app",
        user_id=user_id,
        session_id=session_id
    )

    # Send a message to the agent
    new_message = types.Content(
        parts=[types.Part(text="I need to book a flight to Paris for March 15th and find a good hotel.")],
        role="user",
    )

    # Run the agent and process events
    events = runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=new_message,
    )

    for event in events:
        print(event)

if __name__ == "__main__":
    asyncio.run(main())
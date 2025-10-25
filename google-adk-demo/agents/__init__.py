# Initialize tracing before anything else imports
from langsmith.integrations.otel import configure
from openinference.instrumentation.google_adk import GoogleADKInstrumentor

# Configure LangSmith tracing
configure(project_name="google-adk-demo")

# Instrument Google ADK directly
GoogleADKInstrumentor().instrument()

import streamlit as st
import os
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API keys from environment variables with fallback to user input
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
SERPER_API_KEY = os.getenv("SERPER_API_KEY", "")


# Set the page config to 'wide' for a wider layout
st.set_page_config(layout="wide")

# Custom CSS to make the app visually appealing with blues, blacks, and pastel shades
st.markdown("""
    <style>
        /* General page styles */
        body {
            background-color: #f4f6f9;  /* Light pastel background */
            color: #333333;  /* Dark text color for good contrast */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        /* Title and headers */
        h1, h2, h3, h4 {
            color: #1e3d58;  /* Deep blue shade */
        }

        /* Sidebar */
        .sidebar-content {
            background-color: #2b3a42;  /* Dark blue background for sidebar */
            color: #ffffff;  /* White text */
        }
        .sidebar .sidebar-header {
            font-size: 24px;
            color: #c1e4f5;  /* Pastel blue header */
        }

        /* Main container */
        .block-container {
            max-width: 1200px;  /* Wide container */
            padding: 20px;
        }

        /* Input fields and buttons */
        .stTextInput, .stTextArea, .stButton>button {
            background-color: #c1e4f5;  /* Soft pastel blue background for inputs */
            color: #1e3d58;  /* Dark blue text */
            border-radius: 8px;
            border: 1px solid #1e3d58;
        }

        .stButton>button:hover {
            background-color: #a0c4d8;  /* Slightly darker blue on hover */
        }

        .stTextInput>div, .stTextArea>div {
            background-color: #e7f1fa;  /* Very light blue background for text inputs */
            border-radius: 8px;
        }

        /* Spacing and alignment */
        .stButton {
            margin-top: 20px;
        }

        /* Containers for content */
        .stMarkdown, .stText {
            background-color: #ffffff;  /* White background for content */
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }

        /* Titles and subheaders */
        .stSubheader {
            color: #1e3d58;
            font-weight: bold;
            margin-top: 20px;
        }

        /* Footer text and info */
        .sidebar .sidebar-footer {
            color: #b0c7d7;  /* Lighter blue for footer text */
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)




# Main interface
st.title("AI-Powered weather based Travel Planner")
st.write("Enjoy your personalized itinerary")

# API Key configuration - only shown if environment variables are not set
if not GEMINI_API_KEY or not SERPER_API_KEY:
    st.warning("API keys not found in environment variables. Please enter them below:")
    with st.expander("Configure API Keys", expanded=True):
        if not GEMINI_API_KEY:
            GEMINI_API_KEY = st.text_input("Gemini API Key", type="password")
        if not SERPER_API_KEY:
            SERPER_API_KEY = st.text_input("Serper API Key", type="password")
else:
    #st.success("API keys loaded from environment variables!")
    pass

# User inputs
location = st.text_input("Location", placeholder="e.g., Paris, France")
user_query = st.text_area("Your travel preference or query (optional)", 
                          placeholder="e.g., I love outdoor activities, but I want to avoid rain.")

# Initialize agents and run crew when the user clicks the button
if st.button("Get Travel Recommendations", disabled=not (location and GEMINI_API_KEY and SERPER_API_KEY)):
    with st.spinner("Analyzing weather and preparing recommendations... This may take a few minutes."):
        try:
            # Set API keys
            os.environ["SERPER_API_KEY"] = SERPER_API_KEY
            search_tool = SerperDevTool()

            # Initialize LLM
            llm = LLM(
                model="gemini/gemini-2.0-flash",
                temperature=0.7,
                api_key=GEMINI_API_KEY
            )

            # Create agents for travel weather forecasting
            weather_agent = Agent(
                role="AI Travel Meteorologist",
                goal=f"Provide hyper-local, AI-enhanced weather insights for {location} to ensure seamless travel experiences.",
                backstory="You're an advanced AI meteorologist trained in predictive climate modeling, specializing in travel impact analysis. "
                          "Beyond standard forecasts, you assess how weather conditions affect travel plans, adjusting recommendations dynamically. "
                          "You provide precise insights on the best times for outdoor activities, alert travelers about weather disruptions, "
                          "and intelligently reschedule itineraries to maximize their experience.",
                allow_delegation=False,
                tools=[search_tool],
                max_iterations=4,
                verbose=True,
                llm=llm
            )

            itinerary_agent = Agent(
                role="AI Travel Concierge & Experience Optimizer",
                goal="Curate personalized, weather-adaptive travel experiences by dynamically adjusting itineraries based on real-time conditions.",
                backstory="You're an AI-powered travel expert, blending meteorological insights with cultural intelligence to craft unforgettable journeys. "
                          f"By analyzing {location}'s climate trends and real-time forecasts, you optimize daily plans, ensuring travelers make the most of their trip. "
                          "If sudden weather changes occur, you proactively adjust schedules, recommending the best indoor experiences, scenic alternatives, "
                          "or hidden gems that match the traveler's interests. "
                          "Your expertise extends beyond logistics—you enhance every moment by factoring in local trends, optimal crowd conditions, "
                          "and the most immersive experiences tailored to each traveler.",
                allow_delegation=False,
                verbose=True,
                llm=llm
            )

            # Create tasks for weather analysis and itinerary adjustment
            weather_analysis_task = Task(
                description=(
                    f"1. Obtain and analyze the weather forecast for {location}.\n"
                    "2. Identify key weather conditions relevant to travel (temperature ranges, precipitation, wind conditions).\n"
                    "3. Provide insights on optimal times for outdoor activities and any weather disruptions (e.g., rain, heat waves).\n"
                    "4. Suggest scenic or indoor alternatives if weather conditions change unexpectedly.\n"
                    "5. Provide general weather patterns and forecasts for the week."
                ),
                expected_output="A comprehensive weather analysis document focused on travel recommendations, "
                                "including daily forecasts, weather disruptions, and activity suggestions.",
                agent=weather_agent,
            )

            itinerary_recommendation_task = Task(
                description=(
                    f"1. Review the weather analysis for {location} and understand the forecast.\n"
                    f"2. Analyze the user's query: {user_query} (if provided).\n"
                    "3. Based on the forecast, adjust the itinerary, suggesting the best times for outdoor activities or alternative plans for indoor experiences.\n"
                    f"4. If no specific query is provided, highlight the best experiences in {location} based on the weather forecast.\n"
                    "5. Ensure the itinerary maximizes the traveler’s experience while avoiding weather disruptions."
                ),
                expected_output="A dynamic, weather-adjusted travel itinerary with recommendations for activities, routes, and optimal timing.",
                agent=itinerary_agent,
            )

            # Create and run crew
            travel_crew = Crew(
                agents=[weather_agent, itinerary_agent],
                tasks=[weather_analysis_task, itinerary_recommendation_task],
                verbose=True
            )

            # Get results
            result = travel_crew.kickoff()
            
            # Display results
            st.success("Analysis complete!")
            
            # Display weather analysis
            st.subheader("Weather Analysis")
            st.write(result.tasks_output[0].raw)
            
            # Display travel recommendations
            st.subheader("Travel Recommendations")
            st.write(result.tasks_output[1].raw)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.info("Please check your API keys and try again.")

# Add some helpful information
st.sidebar.markdown("---")
st.sidebar.subheader("About")
st.sidebar.info(
    """
    This app uses AI agents to analyze weather data and provide personalized travel recommendations.
    You can check it out here 
    
    To set API keys permanently:
    1. Create a .env file in the same directory
    2. Add the following lines:
       GEMINI_API_KEY=your_gemini_key_here
       SERPER_API_KEY=your_serper_key_here
    """
)

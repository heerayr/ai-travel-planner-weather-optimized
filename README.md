# Weather-Adaptive Travel Planner: AI-Powered Itinerary Generation
## 🌟 Overview

This project leverages advanced multi-agent AI systems to create dynamic, weather-adaptive travel itineraries. By combining real-time meteorological data analysis with cultural intelligence and personalized travel preferences, the system provides hyper-localized recommendations that maximize traveler experiences while accounting for changing weather conditions.

## 🚀 Key Features

- **AI-Powered Weather Analysis**: Utilizes specialized agent architectures to interpret complex meteorological data beyond simple forecasts
- **Dynamic Itinerary Adaptation**: Automatically adjusts recommendations based on real-time weather conditions and user preferences
- **Hierarchical Multi-Agent System**: Implements a coordinated agent network with specialized roles:
  - Travel Meteorologist Agent (predictive climate modeling)
  - Experience Optimizer Agent (itinerary customization)
- **Parallel Processing Pipeline**: Asynchronous task execution with coordinated data sharing between agents
- **Responsive UI**: Streamlit-based interface with custom CSS for enhanced UX/UI experience

## 🛠️ Technical Architecture

```
Travel Planner System
├── Data Ingestion Layer
│   ├── SERPER API Integration (Weather Data)
│   └── User Preference Analysis
├── Agent System
│   ├── Weather Analysis Agent
│   │   └── Meteorological Pattern Recognition
│   └── Itinerary Optimizer Agent
│       └── Experience Customization Engine
├── Processing Pipeline
│   ├── Parallel Task Execution
│   └── Inter-Agent Communication Protocol
└── Presentation Layer
    └── Streamlit Responsive UI
```

## 🔧 Installation

```bash
# Clone the repository
git clone this-respository-name
cd folder-name

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Edit .env file with your API keys
add both serper and gemini:
GEMINI_API_KEY= your-gemini-key
SERPER_API_KEY=your-serper-key

```
## 📋 Requirements

```
streamlit==1.30.0
crewai==0.28.0
crewai-tools==0.3.1
python-dotenv==1.0.0
databricks-sdk
```

## 🚀 Usage

```
# Run the application
streamlit run app.py
```

Navigate to `http://localhost:8501` in your web browser to access the application.

## 🔍 System Design

### Agent Architecture

The system employs a specialized multi-agent architecture:

1. **AI Travel Meteorologist**
   - Implements predictive climate modeling algorithms
   - Performs time-series analysis of weather patterns
   - Generates weather impact assessments for travel activities

2. **AI Travel Concierge & Experience Optimizer**
   - Utilizes a preference-based recommendation system
   - Implements dynamic itinerary adjustment based on weather conditions
   - Incorporates cultural intelligence for contextually relevant suggestions

### Processing Pipeline

The system uses an advanced task processing pipeline:

```
User Input → Weather Data Acquisition → Meteorological Analysis → 
Itinerary Generation → Preference Adjustment → Presentation
```

Each step is handled by specialized agent components with inter-agent communication protocols for data sharing and coordination.

## 🔬 Technical Implementation Details

- **LLM Integration**: Leverages Google's Gemini 2.0 Flash model for natural language processing and agent reasoning
- **Parallel Processing**: Implements asynchronous task execution for improved performance
- **Modular Design**: Separation of concerns between data acquisition, analysis, and presentation layers
- **Error Handling**: Comprehensive exception management with user-friendly feedback
- **Responsive UI**: Custom CSS implementation for enhanced user experience

## 🤝 Contribution

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License

## 🙏 Acknowledgements

- CrewAI for the agent framework
- Streamlit for the web application framework
- Google for the Gemini AI model
- Serper for weather data API
- 

![Screenshot 2025-03-17 155304](https://github.com/user-attachments/assets/11c507da-921b-486f-b3c5-2e47e9b1daa4)


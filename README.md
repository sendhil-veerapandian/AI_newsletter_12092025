# AI Blog Research Generator

A professional Streamlit application that generates high-quality, research-backed blog content using AI agents. Leverages Gemini AI and Serper API to create comprehensive blogs with real-time information and recent news integration.

## Features

- **AI-Powered Content Generation** - Uses Gemini AI to research and write comprehensive blog posts
- **Real-time Research** - Integrates Serper API for up-to-date information and recent news
- **Clean White UI** - Professional, user-friendly interface with excellent readability
- **Quick Topic Selection** - Pre-defined topic buttons for fast content generation
- **Customizable Options** - Choose tone (Professional/Conversational/Technical) and length (Short/Medium/Long)
- **Real-time Stats** - Word count, character count, and estimated reading time
- **Multiple Download Formats** - Export as Markdown (.md) or plain text (.txt)
- **Recent News Integration** - Automatically includes latest developments and current events

## Prerequisites

- Python 3.10+
- Gemini API key
- Serper API key
- LangGraph environment
- All dependencies in requirements.txt

## Installation

1. Clone the repository
2. Create and activate environment:
   ```bash
   conda create -n python=3.10
   conda activate venv
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your `.env` file with required API keys:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   SERPER_API_KEY=your_serper_api_key_here
   ```

## Usage

1. Activate the environment:
   ```bash
   conda activate venv
   ```
2. Run the Streamlit app:
   ```bash
   streamlit run streamlit_app.py
   ```

2. **Enter a blog topic** or select from quick topics in the sidebar
3. **Choose your preferences** for tone and length
4. **Click "Generate Blog"** and wait for AI to create your content
5. **Download** your blog in your preferred format


## Quick Topics Available

- AI in Healthcare
- Digital Marketing  
- Cybersecurity
- Remote Work
- Blockchain Tech
- Climate Solutions
- Mental Health
- Data Science

## Technologies Used

- **Streamlit** - Web application framework
- **CrewAI** - AI agent orchestration
- **Groq** - Fast AI inference
- **Python** - Backend logic

## Built by S3K Technologies

Professional AI solutions for modern businesses.

---

*For support or customization requests, contact S3K Technologies.*

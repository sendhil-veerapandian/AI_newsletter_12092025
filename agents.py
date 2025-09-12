from crewai import Agent, LLM
import os
from dotenv import load_dotenv
from crewai_tools import SerperDevTool

load_dotenv()

llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=os.getenv('GOOGLE_API_KEY')
)

search_tool = SerperDevTool()

class BlogResearchAgents:
    def researcher_agent(self):
        return Agent(
            role='Research Specialist',
            goal='Research the given topic thoroughly',
            backstory='You are a research expert who finds relevant information.',
            tools=[search_tool],
            llm=llm,
            verbose=True
        )
    
    def writer_agent(self):
        return Agent(
            role='Blog Writer',
            goal='Write a comprehensive blog post',
            backstory='You are a professional blog writer.',
            llm=llm,
            verbose=True
        )
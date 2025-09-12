from crewai import Crew, Process
from agents import BlogResearchAgents
from tasks import BlogResearchTasks
from dotenv import load_dotenv

load_dotenv()

def create_blog(topic):
    # Initialize
    agents = BlogResearchAgents()
    tasks = BlogResearchTasks()
    
    # Create agents
    researcher = agents.researcher_agent()
    writer = agents.writer_agent()
    
    # Create tasks
    research_task = tasks.research_task(researcher, topic)
    write_task = tasks.write_task(writer, topic)
    
    # Create crew
    crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, write_task],
        process=Process.sequential,
        verbose=True
    )
    
    # Run
    result = crew.kickoff()
    return result

if __name__ == "__main__":
    topic = input("Enter blog topic: ")
    result = create_blog(topic)
    print("\n" + "="*50)
    print("BLOG RESULT:")
    print("="*50)
    print(result)
from crewai import Task

class BlogResearchTasks:
    def research_task(self, agent, topic):
        return Task(
            description=f"Research everything about: {topic}",
            agent=agent,
            expected_output="Detailed research findings with key points and sources"
        )
    
    def write_task(self, agent, topic):
        return Task(
            description=f"Write a comprehensive blog post about: {topic}",
            agent=agent,
            expected_output="A complete blog post in markdown format with title, sections, and conclusion"
        )
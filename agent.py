import os
from dotenv import load_dotenv
from google.adk.agents import sequential_agent

load_dotenv()

from agents.search_agent import get_search_agent
from agents.writer_agent import get_writer_agent


search_agent =get_search_agent()

writer_agent = get_writer_agent()


root_agent=sequential_agent.SequentialAgent(
    name='online_ppt_creater_agent',
    sub_agents=[search_agent,writer_agent],
    description=" Agent to search content for ppt from web and then save file to local directory"
)


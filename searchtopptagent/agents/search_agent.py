from google.adk.agents import llm_agent
from google.adk.tools import google_search
from utils import config

def get_search_agent() -> llm_agent.LlmAgent:
    """ This function returns agent which searches for the info in the web"""
    return llm_agent.LlmAgent(name='search_agent',
                              model=config.AI_MODEL,
                              instruction=("You are agent which searches for content and summarize it and use 'google_search' tool to find  user request information that is most recent "),
                              tools=[google_search],
                              output_key='ppt_content'
                              )
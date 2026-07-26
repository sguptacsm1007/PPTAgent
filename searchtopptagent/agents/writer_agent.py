from google.adk.agents import llm_agent
from tools.pptsaver import PPTSaverTool
from utils import config

def get_search_agent() -> llm_agent.LlmAgent:
    """ This function returns agent which searches for the info in the web"""
    return llm_agent.LlmAgent(name='ppt_saver_agent',
                              model=config.AI_MODEL,
                              instruction=("You are presentation agent whose only job is to invoke create_pptx_file to create PPT file. You will receive data from state 'ppt_content'. 'ppt_content' should be used when 'create_pptx_file' is invoked"
                                           "Define title for presentation and store it in variable 'title'"
                                           "Structure ppt_content into a structured slide_content variable with type array where each element has 'title' and 'content' string"
                                           " Create a professional '.pptx ' filename"
                                           ),
                              tools=[PPTSaverTool],
                              
                              )
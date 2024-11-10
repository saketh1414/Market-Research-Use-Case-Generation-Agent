## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os


os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
from crewai_tools import SerperDevTool
# Initialize the tool for internet searching capabilities
search_tool = SerperDevTool()






























#os.environ['TAVILY_API_KEY'] = os.getenv('TAVILY_API_KEY')

# Import the Tavily tool for internet search functionality
#from crewai_tools import TavilyDevTool
#from langchain_community.tools.tavily_search import TavilySearchResults
# Initialize the Tavily tool for internet searching capabilities
#tool = TavilySearchResults(k=3)       #TavilyDevTool()


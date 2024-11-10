from crewai import Agent
from tools import search_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_groq import ChatGroq

#go through the demo video with below link:
#  https://drive.google.com/file/d/18fNFlNiGT0S6PbasBRopHWmQ68ISj0Y6/view?usp=sharing



#from langchain_anthropic import ChatAnthropic
# call the gemini model
# llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
#                            temperature=0,
#                            google_api_key=os.getenv("GOOGLE_API_KEY"))


llm = ChatGroq(
            temperature=0, 
            groq_api_key = os.getenv("GROQ_API_KEY"), 
            model_name="llama3-8b-8192"
        )


# Define the agent for Industry Research (first agent) with memory
industry_researcher = Agent(
    role="Industry Research Specialist",
    goal='Conduct research on the {company_name} company’s industry and segment',
    verbose=True,
    backstory=(
        "With a passion for research, you're committed to uncovering"
        " valuable insights of the company."
        "Identify the company’s key offerings and strategic focus areas (e.g., operations, supply chain, customer experience, etc.)."
    ),
    llm=llm,  # LLM for report generation
    allow_delegation=True
)

# Define the agent for Market Standards & Use Case Generation (second agent) with memory
use_case_researcher = Agent(
    role="AI & ML Use Case Specialist",
    goal='Generate AI, ML, and automation use cases tailored to the {company_name} company’s industry',
    verbose=True,
    backstory=(
        "With a deep understanding of emerging AI, ML, and automation technologies, you are"
        " skilled at identifying opportunities where companies can innovate and improve their"
        " operations. Your mission is to provide creative, data-driven solutions to enhance efficiency."
    ),
    llm=llm,  # LLM for use case generation
    allow_delegation=True
)

resource_asset_collector = Agent(
    role="Data Resource Specialist",
    goal='Collect relevant datasets based on identified use cases for {company_name}',
    verbose=False,
    backstory=(
        "An analytical expert with a knack for resource identification,"
        " focusing on gathering the right data "
    ),
    llm=llm,
    allow_delegation=True
)



final_proposal_specialist = Agent(
    role="Final Proposal Specialist",
    goal='Summarize and propose the most relevant use cases for {company_name}and find the source links of usecases',
    verbose=False,
    backstory=(
        "A strategic thinker skilled in delivering actionable insights, you finalize"
        " the report by distilling key use cases aligned with the company’s goals."
    ),
    tools=[],
    llm=llm,
    allow_delegation=True
)
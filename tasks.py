from crewai import Task
from tools import search_tool
from agents import industry_researcher,use_case_researcher,resource_asset_collector,final_proposal_specialist  #news_researcher,news_writer,

# Define the task for Industry Research
industry_research_task = Task(
    description=(
        "Research the company {company_name} to understand its industry, segment, and"
        " key offerings. Analyze the company's focus areas like operations, supply chain,"
        " customer experience, and its competitive landscape."
        "use the tool only maximum 5 times"
    ),
    expected_output='A report analyzing the industry and strategic focus areas of the company.',
    tools=[search_tool],  # Web browser tool for gathering industry data
    agent=industry_researcher,
    async_execution=False,
    output_file='industry-analysis.md'  # Save the research output
)

# Define the task for Use Case Generation
use_case_task = Task(
    description=(
        "Generate AI, ML, and automation use cases based on the research from the industry analysis."
        " Propose use cases that improve operations, customer satisfaction, and efficiency in the {company_name} company."
        "use the tool only maximum 5 times"
    ),
    expected_output=(
        "A comprehensive list of AI, ML, and automation use cases that are relevant to the company’s"
    ),
    tools=[search_tool],  # Web browser tool for gathering market standards and industry trends
    agent=use_case_researcher,
    async_execution=False,
    output_file='ai-ml-use-cases.md'  # Example of output customization
)

resource_collection_task = Task(
    description=(
        "Based on the use cases generated, search for relevant code executions of that use case on platforms and find sources that are only present in"
        "Kaggle and HuggingFace and GitHub. Compile a list of resource links."
        "dont create your own links, just add some already existing ones solving the related use case"
        "use the tool only maximum 5 times"
    ),
    expected_output='A markdown file with relevant dataset links',
    tools=[search_tool],
    agent=resource_asset_collector,
    output_file='links-of-usecases.md',
    async_execution=False
)


final_proposal_task = Task(
    description=(
        "Create a comprehensive report of the top use cases generated for {company_name},"
        " ensuring that each use case aligns with the company's goals and operational needs."
        " Include references for each use case where applicable, with resource links formatted"
        " as clickable URLs."
    ),
    expected_output='A markdown report summarizing recommended use cases with clickable resource links.',
    agent=final_proposal_specialist,
    tools=[],
    async_execution=False,
    output_file='final_proposal_report.md'  # Outputs a markdown file with clickable links
)
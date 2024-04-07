from langchain.agents import load_tools, AgentType, initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.utilities import SerpAPIWrapper

search = SerpAPIWrapper()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
tools = load_tools(["llm-math", "serpapi"], llm=llm)
# tools = (
#     Tool(
#         name="search",
#         func=search.run,
#         description="useful for when you need to answer questions about current events. You should ask targeted questions",
#     ),
# )
agent = initialize_agent(
    tools, llm=llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

print(llm.predict("2024年奥运会举办地是哪里"))

print(agent.run("2024年奥运会举办地是哪里"))
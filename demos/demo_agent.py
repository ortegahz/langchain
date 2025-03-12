import os

from utils.macros import API_SECRET_KEY, BASE_URL, TAVILY_API_KEY

os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_BASE_URL"] = BASE_URL
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY

# Import relevant functionality
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model

# Create the agent
memory = MemorySaver()
# model = ChatAnthropic(model_name="claude-3-sonnet-20240229")
model = init_chat_model("gpt-4o", model_provider="openai")
search = TavilySearchResults(max_results=2)
tools = [search]
agent_executor = create_react_agent(model, tools, checkpointer=memory)

# Use the agent
config = {"configurable": {"thread_id": "abc123"}}
for step in agent_executor.stream(
        {"messages": [HumanMessage(content="hi im bob! and i live in sf")]},
        config,
        stream_mode="values",
):
    step["messages"][-1].pretty_print()

for step in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather where I live?")]},
        config,
        stream_mode="values",
):
    step["messages"][-1].pretty_print()

from langchain_community.tools.tavily_search import TavilySearchResults

search = TavilySearchResults(max_results=2)
search_results = search.invoke("what is the weather in SF")
print(search_results)
# If we want, we can create other tools.
# Once we have all the tools we want, we can put them in a list that we will reference later.
tools = [search]

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4", model_provider="openai")

from langchain_core.messages import HumanMessage

response = model.invoke([HumanMessage(content="hi!")])
print(f"ContentString: {response.content}")

model_with_tools = model.bind_tools(tools)

response = model_with_tools.invoke([HumanMessage(content="Hi!")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

response = model_with_tools.invoke([HumanMessage(content="What's the weather in SF?")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

from langgraph.prebuilt import create_react_agent

agent_executor = create_react_agent(model, tools)

response = agent_executor.invoke({"messages": [HumanMessage(content="hi!")]})

for step in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather in sf?")]},
        stream_mode="values",
):
    step["messages"][-1].pretty_print()

for step, metadata in agent_executor.stream(
        {"messages": [HumanMessage(content="whats the weather in sf?")]},
        stream_mode="messages",
):
    if metadata["langgraph_node"] == "agent" and (text := step.text()):
        print(text, end="|")

from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="hi im bob!")]}, config
):
    print(chunk)
    print("----")

for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="whats my name?")]}, config
):
    print(chunk)
    print("----")

config = {"configurable": {"thread_id": "xyz123"}}
for chunk in agent_executor.stream(
        {"messages": [HumanMessage(content="whats my name?")]}, config
):
    print(chunk)
    print("----")

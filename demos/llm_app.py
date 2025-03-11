import os

API_SECRET_KEY = "sk-3xFsyspt9KODQXdtBeD3Ce1a24344dB1868b440979A2703c"
BASE_URL = "https://aihubmix.com/v1"

os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_BASE_URL"] = BASE_URL

from langchain.chat_models import init_chat_model

model = init_chat_model("gpt-4o", model_provider="openai")

from langchain_core.messages import HumanMessage, SystemMessage

messages = [
    SystemMessage("Translate the following from English into Italian"),
    HumanMessage("hi!"),
]

model.invoke(messages)

model.invoke("Hello")

model.invoke([{"role": "user", "content": "Hello"}])

model.invoke([HumanMessage("Hello")])

for token in model.stream(messages):
    print(token.content, end="|")

from langchain_core.prompts import ChatPromptTemplate

system_template = "Translate the following from English into {language}"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", "{text}")]
)

prompt = prompt_template.invoke({"language": "Italian", "text": "hi!"})

response = model.invoke(prompt)
print(response.content)

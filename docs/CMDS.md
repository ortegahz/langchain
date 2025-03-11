# keys

API_SECRET_KEY = "sk-3xFsyspt9KODQXdtBeD3Ce1a24344dB1868b440979A2703c"
BASE_URL = "https://aihubmix.com/v1"

os.environ["OPENAI_API_KEY"] = API_SECRET_KEY
os.environ["OPENAI_BASE_URL"] = BASE_URL

# install
cd /media/manu/ST2000DM005-2U91/workspace/langchain/libs/langchain
pip install -e .
pip install -e .[openai]
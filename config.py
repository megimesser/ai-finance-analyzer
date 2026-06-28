import os 
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))


CLAUDE_API = os.environ.get("CLAUDE_API","")



# importer
F_EXCEL = (os.path.join(BASE_DIR, "finance.xlsx"))


# kurs
F_JSON = (os.path.join(BASE_DIR, "finance.json"))


# konverter
V_PROMPT = (os.path.join(BASE_DIR,"vanilla_prompt.txt"))
S_PROMPT = (os.path.join(BASE_DIR,"systemprompt.txt"))
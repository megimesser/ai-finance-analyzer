import os 
from dotenv import load_dotenv


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

load_dotenv(os.path.join(BASE_DIR, '.env'))


CLAUDE_API = os.environ.get("CLAUDE_API","")



# Importer
F_EXCEL = (os.path.join(BASE_DIR, "finance.xlsx"))


# Kurs
F_JSON = (os.path.join(BASE_DIR, "finance.json"))


# Konverter
V_PROMPT = (os.path.join(BASE_DIR,"vanilla_prompt.txt"))
S_PROMPT = (os.path.join(BASE_DIR,"systemprompt.txt"))


# Outputdateien
O_JSON = (os.path.join(BASE_DIR,"output.json"))
O_TEXT = (os.path.join(BASE_DIR,"output.txt"))
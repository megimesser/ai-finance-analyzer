import json
from config import V_PROMPT,S_PROMPT,F_JSON

path = "finance.json"
sys_prompt = "systemprompt.txt"
path_3 = "vanilla_prompt.txt"



def prompt_designer(json_path,systemprompt,vanillaprompt):
    with open(json_path, "r", encoding="utf-8") as f :
        data = json.load(f)

    data = json.dumps(data, indent=2)

    with open(vanillaprompt, "r", encoding="utf-8") as f:
        data_2 = f.read()

    prompt = data + "\n" + data_2

    print(prompt)

    with open(systemprompt, "w", encoding="utf-8") as b:
        b.write(prompt)

if __name__ == "__main__":
    prompt_designer(F_JSON,S_PROMPT,V_PROMPT)
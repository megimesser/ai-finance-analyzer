import requests
import os
import json
import time
from importer import importer, ticker_format,format_portfolio
from config import F_EXCEL, S_PROMPT,CLAUDE_API,NEWS_PROMPT_PORT

#Nach test löschen 


df = importer(F_EXCEL)
api_key=os.getenv("CLAUDE_KEY")


def prompt_news(excel,path):
    print(excel)
    probe = ""


    for i in excel:
        i = list(i)
        for s in i: 
            if isinstance(s,str):
                probe += s
                print(s)

    with open(path, "a") as f:
        f.write(probe + "\n")
      
    



    #with open(prompt, "r") as message:
      #  content = message.read()
      #  content = str(content)

    




def request_news(prompt,key):

    with open(prompt, "r") as message:
        content = message.read()
        content = str(content)




    response = requests.post(
        "https://api.anthropic.com/v1/messages",
        headers={
            "x-api-key": key,
            "content-type": "application/json",
            "anthropic-version": "2023-06-01"
        },
        json={
            "model": "claude-sonnet-4-6",
            "max_tokens": 1500,
            "tools": [
                {
                    "type": "web_search_20250305",
                    "name": "web_search"
                }
            ],
            "messages": [
                {"role": "user", "content": content}
            ]
        }
    )

    print(f"Status: {response.status_code}")

    if response.status_code != 200:
        print(f"API Error: {response.json()}")
        exit(1)

    data = response.json()

    # Alle Text-Blöcke zusammensammeln (Web Search erzeugt mehrere Blöcke)
    antwort = ""
    for block in data["content"]:
        if block["type"] == "text":
            antwort += block["text"]

    print(antwort)

    with open("output.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    with open("antwort.txt", "w", encoding="utf-8") as file:
        file.write(antwort)






# Sogenannter "Guard" - Block wird nur ausgeführt wenn Script direkt gestartet wird 
if __name__ == "__main__":
    df = importer(F_EXCEL)
    #print(df.columns.tolist())
    #print(format_portfolio(df))
    #request_news(S_PROMPT,CLAUDE_API)
   
    #print(ticker_format(df))
    prompt_news(format_portfolio(df),NEWS_PROMPT_PORT)
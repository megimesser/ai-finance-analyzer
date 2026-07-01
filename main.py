#Variablenimport
from config import F_EXCEL, F_JSON,CLAUDE_API,O_JSON,O_TEXT,S_PROMPT


from modules.analyzer.importer import importer, format_portfolio, ticker_format
from modules.analyzer.kurs import finance_info,json_writer
from modules.analyzer.merger import merger
from modules.requester.requester import api_caller




# Öffnen der finance - Excel 
df = importer(F_EXCEL)
formator = format_portfolio(df)
print(formator)
("Excelimport fertig")

# Kursdatenabruf
kürzel = ticker_format(importer(F_EXCEL))
finance_info(kürzel)
print("API - Abruf fertig")
json_writer(F_JSON,finance_info(kürzel))



# Merger
merger(F_JSON,formator)
print("Formatierung fertig")


# Requester 
api_caller(CLAUDE_API,S_PROMPT,O_JSON,O_TEXT)
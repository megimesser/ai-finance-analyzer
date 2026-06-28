#Variablenimport
from config import F_EXCEL, F_JSON


from importer import importer, format_portfolio, ticker_format
from kurs import finance_info,json_writer
from merger import merger




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
import requests
from bs4 import BeautifulSoup 
import openpyxl
from datetime import datetime   

link = "https://www.google.com/search?q=cotação+dolar&client=opera-gx&hs=knV&sca_esv=757e01b514b177ca&sxsrf=ADLYWIIzH1Rw2r9gWxN7f046cYRNF0ncLg%3A1729174216340&ei=yBoRZ4i6FMi45OUPpJXB8AE&oq=cotação+&gs_lp=Egxnd3Mtd2l6LXNlcnAiCmNvdGHDp8OjbyAqAggAMhAQABiABBixAxhDGIMBGIoFMgsQABiABBixAxiDATINEAAYgAQYsQMYQxiKBTIKEAAYgAQYQxiKBTIKEAAYgAQYQxiKBTIQEAAYgAQYsQMYQxiDARiKBTIKEAAYgAQYQxiKBTIFEAAYgAQyCBAAGIAEGLEDMg4QABiABBixAxiDARiKBUiLBVAfWB9wAHgCkAEAmAGiAaABogGqAQMwLjG4AQHIAQD4AQGYAgKgAq8BwgIEEAAYR5gDAIgGAZAGCJIHAzEuMaAH0AU&sclient=gws-wiz-serp"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 OPR/114.0.0.0"}

site = requests.get(link,headers=headers)

html_site = BeautifulSoup(site.text, "html.parser")

produto = html_site.find("input", class_="lWzCpb a61j6")

valor_produto = produto.get("value")

wb = openpyxl.load_workbook("cotacao_dolar.xlsx")
sheet = wb.active

data_hora_atual = datetime.now().strftime("%d-%m-%Y")
sheet.append([data_hora_atual, valor_produto])

wb.save("cotacao_dolar.xlsx")
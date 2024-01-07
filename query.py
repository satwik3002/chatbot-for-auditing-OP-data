import os
import pandas as pd
from pandas_llm import PandasLLM
# import openai
# openai.api_key = ""
# data = [('John Doe', 25, 50), 
#  ('Jane Smith', 38, 70),
#  ('Alex Johnson', 45, 80),
#  ('Jessica Brown', 60, 40),
#  ('Michael Davis', 22, 90),
#  ('Emily Wilson', 30, 60),
#  ('Daniel Taylor', 35, 75),
#  ('Sophia Moore', 40, 85),
#  ('David Thomas', 50, 65),
#  ('Olivia Jackson', 29, 55)]
# df = pd.DataFrame(data, columns=['name', 'age', 'donation'])
df=pd.read_excel('C:/Users/SATWIK/Desktop/CAPSTONE PROJECT 1/Satwick/Backed/April to June.xlsx')
conv_df = PandasLLM(data=df, llm_api_key = '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')
result = conv_df.prompt("get paitent with UMRNO UMR2360")
code = conv_df.code_block
print(f"Executing the following expression of type {type(result)}:\n{code}\n\nResult is:\n {result}\n")
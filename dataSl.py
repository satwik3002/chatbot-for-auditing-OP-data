from datasloth import DataSloth
import pandas as pd
# sloth = DataSloth(openai_api_key='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')
sloth = DataSloth(openai_api_key='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')

import pandas as pd
import seaborn as sns

df=pd.read_excel('C:/Users/SATWIK/Desktop/CAPSTONE PROJECT 1/Satwick/Backed/April to June.xlsx')

def Que(que):
    result=sloth.query(que)
    # print(result)
    # return result.to_json()
    data=result.to_dict(orient='records')
    print(data)
    return data
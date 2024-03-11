import pandas as pd
from pandasai
from pandasai.llm import OpenAI
import os
from sklearn import datasets
import numpy as np


iris=datasets.load_iris()
llm=OpenAI(api_token=os.getenv("openai+api"))

df=pd.DataFrame(data=np.c_[iris['data'],iris['target']],columns=iris['feature_names']+['target'])
df=SmartDataframe(df,configparser={"llm":llm})
df.chat("""Plot a scatter plot of sepal length versus sepal width color according to the target variable""")
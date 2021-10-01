
import pandas as pd
from pandas.core.arrays.categorical import contains
df = pd.read_csv("../../IRAhandle_tweets_1.csv")
df = df.iloc[:10000,]
print(df.shape)

#remove non-English tweets
df_eng = df[df["language"] == "English"]
#remove tweets with "?" and store these tweets
df_eng_state = df_eng[df_eng["content"].str.contains("\?")==False]
print(df_eng_state.shape)

#df_eng["content"].str vextorizes the Series to access its values
#str.contains() is a specific function for checking content in each series
#here, this doesn't check for "-Trump" case, only " Trump" cases:
#df_eng_state["trump_mention"] = df_eng_state["content"].str.contains("Trump", case=True)
df_eng_state["trump_mention"] = df_eng_state["content"].str.split('[^A-Za-z0-9]').apply(lambda x: "Trump" in x)
#print(df_eng_state[["content","trump_mention"]])
df_eng_state =  df_eng_state[['tweet_id','publish_date','content','trump_mention']]
df_eng_state.to_csv("dataset.tsv", sep="\t", encoding='utf-8', header=True, index=False)

mention,_ = df_eng_state[df_eng_state["trump_mention"]==True].shape
total,_ = df_eng_state.shape
percent_mention = float(str(mention/total)[:5])
#print(mention)
#print(percent_mention)

result = pd.DataFrame({'result':['frac-trump-mentions'],'value':[percent_mention]})
result.to_csv('results.tsv',sep='\t',header=True,index=False)
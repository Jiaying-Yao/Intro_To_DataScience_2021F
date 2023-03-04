import pandas as pd

df = pd.DataFrame({'a':[True, False,True],'b':['apple','banana','banana']})
x,y=df[df['a']==True].shape
#print(x)

a=pd.DataFrame({'a':[1,2,3,4,5], 'b':[1,2,3,4,5]})
print(a.iloc[:2,])
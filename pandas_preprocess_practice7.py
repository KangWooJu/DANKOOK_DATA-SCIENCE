import pandas as pd 
import itertools

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv') 

# 임의 표본추출  
df20 = df.sample(n=20,random_state=123)                               # random_state : 임의 추출의 결과를 일정하게 고정한다. 
df20 

# 층화 표본추출 
strtified = df.groupby('Species').apply(
    lambda x: x.sample(frac=0.2,random_state=123)                     # frac : 전체에서 몇 %의 행을 추출할지를 지정한다. 0.2 -> 20%
)
strtified 

# 조합 
species = df.Species.unique()
comb = list(itertools.combinations(species,2))
comb 



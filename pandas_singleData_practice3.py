import pandas as pd
from scipy import stats

ds = [60,62,64,65,68,69]
weight = pd.Series(ds) 
ds.append(120)                                 # ds에 120 추가 
weight_heavy = pd.Series(ds)
weight
weight_heavy

weight.mean()                                  # 평균 
weight_heavy.mean()                            # 평균 

weight.median()                                # 중앙값 
weight_heavy.median()                          # 중앙값  

stats.trim_mean(weight,0.2)                    # 절사평균 ( 상하위 20%제외 )
stats.trim_mean(weight_heavy,0.2)              # 절사평균 ( 상하위 20%제외 ) 

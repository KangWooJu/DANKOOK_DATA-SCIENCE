import seaborn as sns 

df = sns.load_dataset('tips')
df.head()

p1 = df.pivot_table(index='sex',                     # 행 위치에 들어갈 컬럼  
                    columns='day',                   # 열 위치에 들어갈 컬럼  
                    values='totla_bill',             # 데이터로 사용할 컬럼  
                    aggfunc='mean')                  # 데이터 집계함수  

p1.head()

p2 = df.pivot_table(index='sex',                     # 행 위치에 들어갈 컬럼  
                    columns='time',                  # 열 위치에 들어갈 컬럼  
                    values='total_bill',             # 데이터로 사용할 컬럼  
                    aggfunc='mean')                  # 데이터 집계함수  
p2.head()

p3 = df.pivot_table(index='time',                    # 행 위치에 들어갈 컬럼   
                    columns='day',                   # 열 위치에 들어갈 컬럼  
                    values='tip',                    # 데이터로 사용할 컬럼  
                    aggfunc='max')                   # 데이터 집계함수   
p3.head()
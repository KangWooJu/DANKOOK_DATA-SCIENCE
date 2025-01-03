import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/wooju-kang/Downloads/data/user_behavior_dataset.csv')

df=df.iloc[:,3:10]
df.columns=['App_Usage_Time','Screen_On_Time','Battery_Drain',
            'No_of_Apps','Data_Usage','Age','Gender']

# 문제 1

df.plot.scatter(x='App_Usage_Time',                
                y='No_of_Apps',                 
                s=50,                    
                c='blue',                
                marker='s')             
plt.show()

# 문제 2 

dict = {'Male':'red','Female':'blue'}
colors=list(dict[key] for key in df.Gender)

dict2 = {'Male':'o','Female':'s'}
markers=list(dict2[key] for key in df.Gender)


df.plot.scatter(x='App_Usage_Time',
                y='No_of_Apps',
                s=50,
                c=colors,
                marker='o')
plt.show()


# 문제 3

vars = ['App_Usage_Time','Screen_On_Time','Battery_Drain','No_of_Apps']
pd.plotting.scatter_matrix(df[vars])
plt.show()

# 문제 4 

df['App_Usage_Time'].corr(df['No_of_Apps'])

# 문제 5

df = df.loc[:,~df.columns.isin(['Gender'])]         
df.corr()         


# 문제 6
import pandas as pd
import matplotlib.pyplot as plt


df2 = pd.read_csv('/mnt/data/students.csv')


for col in ['초등학교', '중학교', '고등학교']:
    df2[col] = df2[col].str.replace(',', '').astype(float)


df2.set_index('연도', inplace=True)


df2.plot(marker='o', title='연도별 학생수', xlabel='연도', ylabel='학생수')


plt.legend(loc='upper right')


plt.show()

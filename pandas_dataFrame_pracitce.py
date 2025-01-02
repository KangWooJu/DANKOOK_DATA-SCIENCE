import pandas as pd

df = pd.read_csv('/Users/wooju-kang/Downloads/data/iris.csv')                   # csv 파일 읽기 -> 경로 삽입 필요 , header = None 으로 설정 시 , Column 지정이 안되어 있는 것으로 인식 
df                                                                                # 내용 확인 
                                                                                  # csv 파일 형식으로 저장시 to_csv() 메서드를 사용한다. ex) df.to_csv('파일경로')

# 데이터프레임 객체의 정보 확인 

df.info()                                             # 배열의 정보
df.shape                                              # 배열의 형태                                 
df.shape[0]                                           # 행의 개수 
df.shape[1]                                           # 컬럼의 개수 


df.dtypes                                             # 각 컬럼의 자료형
df['Species'] = df['Species'].astype('category')      # 별도의 자료형을 부여 : Pandas에서는 기본적으로 문자열 값의 컬럼에 대해 Object type으로 지정한다.
df.dtypes


df.columns                                            # 컬럼들의 이름 보
df.head()                                             # 데이터 앞부분기 일부 보기 -> () 안에 보고싶은 데이터의 개수 지정 가능 
df.tail()                                             # 데이터 뒷부분 일부 보기 -> () 안에 보고싶은 데이터의 개수 지정 가능 
df['Species'].unique()                                # 자료에서 중복된 값들을 제거하여 어떤 종류의 값들이 있는지 파악 


# 인덱싱과 슬라이싱

df.iloc[2,3]                                          # 2행 3열의 값 
df.loc[3,'Petal_Width']                               # 'Petal_Width' 칼럼의 3행 값
df.loc[[0,2,4],['Petal_Length','Petal_Width']]        # 

df.loc[5:8,'Petal_Length']                            # 'Petal_Length' 컬럼의 5 ~ 7행 값 
df.iloc[:5,:4]                                        # 0 ~ 4행 , 0 ~ 3열의 값

df.loc[:,'Petal_Length']                              # 'Petal_Length' 칼럼의 모든 행의 값 (1) : 정식 
df['Petal_Length']                                    # 'Petal_Length' 칼럼의 모든 값 (2) : 약식 
df.Petal_Length                                       # 'Petal_Length' 칼럼의 모든 값 (3) : 약식 

df.iloc[:5,:]                                         # 0 ~ 4행의 모든 컬럼의 값  
df.iloc[:5]                                           # 0 ~ 4행의 모든 칼럼의 값 


# 조건문을 이용한 슬라이싱 
df.loc[df.Petal_Length >= 6.5, :]                     # Petal_Length >= 6.5를 만족하는 행들의 모든 컬럼 
df.loc[df.Petal_Length >= 6.5]                        # 모든 컬럼인 경우 컬럼 인덱스 생략 


df.loc[df.Petal_Length >= 6.5].index                  # Petal_Length >= 6.5를 만족하는 행들의 인덱스 번호 

df.loc[(df.Petal_Length >= 3.5)&                      # AND 연산 
       (df.Petal_Length <= 3.8)] 

df.loc[(df.Petal_Length < 1.3) |                      # OR 연산을 만족하는 'Petal_Length' 와 'Petal_Width' 보여주기
       (df.Petal_Length > 6.5),
       ['Petal_Length','Petal_Width']]

df.where(df.Petal_Length >= 6.5).dropna()             # Where()를 이용한 조건 검색   



# 데이터프레임 객체에 대한 산술 연산


df.loc[:,df.columns != 'Species']                     # 'Species' 컬럼을 제외 (1)
df.loc[:, ~df.columns.isin(['Speices'])]              # 'Species' 컬럼을 제외 (2) 
df.loc[:, df.columns !='Species'] + 10                # 모든 값들에 10을 더함  -> df의 내용이 변경되지는 않는다.  

df['Sepal_Length'] + df['Petal_Length']               # 두 컬럼의 같은행 값들끼리 연산 : 자료형이 숫자형인 컬럼들끼리는 산술 연산이 가능 



tmp = df['Petal_Length'].apply(lambda x:-1 if x>= 5 else 1) 
df['Petal_Length'] * tmp                              # Petal_Length >= 5를 만족하는 경우 -1을 곱하기 


# 데이터프레임의 통계 관련 메소드 

df2 = df.loc[:,df.columns != 'Species']               # 숫자타입 컬럼만 추출 
df2.sum()                                             # 값들의 합계값 : 동일한 표현식으로 ' df2.sum(axis=0) ' 이 있다. axis=0 : 세로방향  
df2.mean()                                            # 값들의 평균값  
df2.median()                                          # 값들의 중앙값  
df2.max()                                             # 값들의 최대값  
df2.min()                                             # 값들의 최소값  
df2.std()                                             # 값들의 표준편차  
df2.var()                                             # 값들의 분산  
df2.abs()                                             # 값들의 절대값  
df2.describe()                                        # 기초통계정보  


# 데이터프레임 객체에 있는 값의 수정 

df3 = df.copy()                                       # df를 df3에 복사 
df3.iloc[1,2] = 5.5                                   # 1행 2열의 값을 수정  
df3.loc[1,'Petal_Length'] = 1.1                       # 1행 1열의 값을 수정 

df3.Petal_Length.to_list()                            # 시리즈를 리스트로 변환하기 
df3.loc[df.Petal_Length > 6.5,'Petal_Length'] *= 100  # Petal_Length >= 6.5를 만족하는 행과 'Petal_Length'열에 100 곱하기 


# 데이터프레임 객체에 대한 행과 칼럼의 추가 

# 뒷 부분에 새로운 행 추가하기  
new_idx = df3.shape[0]                                # 추가할 행번호 결정 
df3.loc[new_idx] = [1.1,4.5,3.4,2.2,'setosa']         # 마지막 행에 데이터 추가 
df3.tail()      


# 중간에 새로운 행 추가하기 
new_row = pd.DataFrame([[1.1,2.2,3.3,4.4,'virginica']], # 새로운 데이터프레임 생성 
                       columns=df3.columns)
new_row
df3 = pd.concat([df3.iloc[:10],new_row,df3.iloc[10:]] # concat()를 통해서 중간에 끼워넣기 concat(A,B,C) : B를 A와C 사이에 끼워넣기  
                ,ignore_index= True) 

df3.iloc[8:13,:]            

# 여러 행 추가 
ext = pd.DataFrame([[1.2,3.5,4.3,3.1,'setosa'],       # 새로운 데이터 프레임 생성 
                    [2.1,3.2,2.3,5.2,'versicolor']],
                   columns=df3.columns)

ext
df3 = df3._append(ext,ignore_index=True)              # appned()를 통해 뒷 부분에 붙이기 
df3


# 뒤쪽에 컬럼 추가 
new_col = df3.Petal_Length * 10          
df3['new_col'] = new_col
df3


# 중간에 컬럼 추가
df4 = df.copy()
df4.insert(loc=2,column='new_col2',value=new_col)     # loc : 삽입 위치 , column : 컬럼 이름 , value : 데이터 값 
df4



# 데이터프레임 객체에 대한 행과 컬럼의 삭제 
df5 = df.copy()


# 행의 삭제 
df5 = df5.drop(index=[1,3])
df5
df5 = df5.reset_index()                               # reset_index() : 인덱스 초기화 하기  -> 초기화 이전의 인덱스가 첫 번째 컬럼에 자동으로 생성된다. ' drop = True ' 를 추가하면 컬럼 추가
df5


# 컬럼의 삭제 
df5 = df5.drop(columns='Petal_Length')
df5
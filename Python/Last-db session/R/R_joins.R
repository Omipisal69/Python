library(dplyr)
df<-data.frame(id=c(1:5))
df1<-data.frame(id=c(4:8))

df
df1
inner_join(df,df1,by="id")
left_join(df,df1,by="id")
right_join(df,df1,by="id")
full_join(df,df1,by="id")

library(dplyr)
setwd("C:\\Users\\admin\\Desktop\\data")
df=read.csv("Sample_Superstore.csv")
df
group_by(df,Region)
summarise(group_by(df,Region),totalsales=sum(Sales))
summarise(group_by(df,Region),maxsales=max(Sales))
summarise(group_by(df,Region),minsales=min(Sales))

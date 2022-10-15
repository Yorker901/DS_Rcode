df = read.csv(file="F:\\ExcelR\\data\\Lungcapdata.csv",header=T)
head(df)
dim(df)

df=read.csv(file="Lungcapdata.csv")
df

#accessing the variable
df$LungCap
mean(df$LungCap)
summary(df$LungCap)

df[1,1] #first row,first column
df[,1] # only first column
df[,1:3] # column 1 - 3
df[, c(1,3,5)] # selected columns 1,3,5

summary(df)

#converting into factor
df$smoke = as.factor(df$Smoke)
df$Gender = as.factor(df$Gender)
df$Caesarean = as.factor(df$Caesarean)
df$AgeRange = as.factor(df$AgeRange)
summary(df)

df$Gender
levels(df$Gender)
nlevels(df$Gender)
summary(df$Gender)

# box plot
boxplot(df$Age,horizontal = TRUE,col="pink")
boxplot(df$LungCap,horizontal = TRUE,col="blue")

# histogram
hist(df$LungCap)

#scatter plot
plot(df$Age,df$LungCap)
plot(df$Height,df$LungCap)

cov(df$Age,df$Height)
cor(df$Age,df$Height) # no relationship

import random

processBlock=[{'name':'Firefox','size':3467},{'name':'Mass Effect','size':356545},{'name':'GingerCup','size':1565},{'name':'VeraSmoke','size':3424},{'name':'decaG','size':356},{'name':'Alphone','size':145},{'name':'Vantage','size':675},{'name':'mailerBird','size':245},{'name':'Insightica','size':9895},{'name':'LoreFore','size':247},{'name':'Litra','size':2321},{'name':'Havji','size':35612},{'name':'SauceBee','size':6456},{'name':'Perco','size':323},{'name':'ExtremeBench','size':351},{'name':'jedX','size':3503},{'name':'Lavarella','size':523},{'name':'NorthPoint','size':2145},{'name':'Calculator','size':12},{'name':'BoxIt','size':1228},{'name':'Crisp','size':9821},{'name':'HellCat','size':3891},{'name':'Vim','size':8891},{'name':'Porter','size':1891},{'name':'Artx','size':9821},{'name':'ModPro','size':12891}]    

loadProcess=processBlock

for process in loadProcess:
    process['relIndex']=random.randint(0, 10)
    

memoryBlock=[{'partition':'A','size':134546}]

loadMemory=memoryBlock

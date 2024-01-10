d={'Roll':1,'Name':'A','Marks':[30,50,35,60,75]}
d['total']=sum(d['Marks'])
d['avg']=d['total']//len(d['Marks'])
print(d)
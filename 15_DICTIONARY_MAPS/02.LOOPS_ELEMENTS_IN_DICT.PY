a={1:2,3:4,"list":[1,23],"dict":{1:2}}
a

a['list']
a.get('list')
print(a.get("li"))
a.get('li',0)
a.keys()
a.values()
a.items()

for i in a:
    print(i,a[i])

for i in a.values():
    print(i)

"list" in a

2 in a
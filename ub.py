#dict = {".----":1,"..---":2,"...--":3,"....-":4,".....":5,"-....":6,"--...":7,"---..":8,"----.":9,"-----":0}
#i = ''.join([input()[0] for o in range(5)])
#print(i)1
#if i in dict:
#    print(dict[i])

ma,div  = int(input("max:")),int(input("div:"))
[print(i) for i in range(ma)if i%div == 0]
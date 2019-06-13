import json
with open("../Downloads/incidents.json",'r') as load_f:
    load_dict = json.load(load_f)
    arr = set()
    arr.clear
    load_dict = load_dict[u'tickets']
    for i in load_dict:
        #print (i[u'file_hash'],u'src_ip')
        arr.add((i[u'dst_ip'],i[u'file_hash']))
    a=len(arr)
    print a
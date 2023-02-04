def insert_file(tenfile,data):
    f = open(tenfile,"a",encoding='utf8')
    f.write(data)
    f.close()



def read_file(tenfile):
    f = open(tenfile)
    data = f.readlines()
    header = data[0].strip().split(",")
    D_data = {}
    for i in header:
        D_data[i] = []
    data = data[1:]
    for i in data:
        i = i.strip().split(",")
        for j in range(len(header)):
            D_data[header[j]].append(i[j])
    return D_data

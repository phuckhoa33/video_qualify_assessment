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

def convert_standard_text():
    f = open("contentAssessment/readContent/recognized.txt")
    data = f.readlines()
    result = ""
    for item in data[1:]:
        temp_value = item.split(' ')
        if len(temp_value) > 10:
            temp_value.insert(10, "\n")
        value_at_item = " ".join(temp_value)
        result += value_at_item
    return result

def solve_with_qualify_file():
    f = open("qualify_of_video.csv")
    data = f.readlines()
    result = []
    for i in data:
        temp = i.split(',')
        result.append(temp)
    return result
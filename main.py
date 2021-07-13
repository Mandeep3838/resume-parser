from resume_parser import resumeparse
import os
import json

# json_data = resumeparse.read_file('Resumes/TeresaNeetipudi IT BA.docx')
# print(json_data)
# with open("./Resume-testing/Anil Krishna Mogalaturthi.json",'w+') as f:
#     f.write(json.dumps(json_data))

for x in os.listdir('Resumes/'):
    print("processing file" + x)
    if os.path.isfile('Resumes/' + x):
        print("file exist")
        name = x.split(".")[:-1]
        print("file " + name[0] + "processed")
        if os.path.isfile('Resume-testing/' + name[0] + ".json"):
            print("json present")
        else:
            json_data = resumeparse.read_file('Resumes/' + x)
            with open("./Resume-testing/" + name[0] + ".json", "w+") as f:
                f.write(json.dumps(json_data))
    else:
        print("file" + x + "not found")
    

# data = 

# print(data)

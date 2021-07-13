import numpy
from resume_parser import resumeparse
import json
import os
import pickle

# Import Binary file
f = open('linear_regressor.pkl', 'rb')
lr = pickle.load(f)
if lr:
    print("Linear Regression Model Loaded")
g = open('desig_rating.pkl', 'rb')
desig_rating = pickle.load(g)
if desig_rating:
    print("Ratings loaded")


# Take input from user
file = input("Location of file: ")

if os.path.isfile(file):
    # default values
    name=""
    city=""
    phone_no=""
    email=""
    companies=""
    college=""
    degree=""
    experience=""
    skills=""
    designition=""
    # read file
    json_data = resumeparse.read_file(file)
    if json_data.get("name"):
        name = json_data["name"].lower()
    if json_data.get("phone"):
        phone_no=json_data["phone"].lower()
    if json_data.get('email'):
        email=json_data["email"].lower()
    if json_data.get('total_exp'):
        experience=json_data["total_exp"]
    if json_data.get('degree'):
        degree= [x.lower() for x in json_data['degree']]
    if json_data.get('university'):
        college=[x.lower() for x in json_data['university']]
    if json_data.get('designition'):
        designition=[x.lower() for x in json_data['designition']]
    if json_data.get('skills'):
        skills=[x.lower() for x in json_data['skills']]
    if json_data.get('Companies worked at'):
        companies=[x.lower() for x in json_data['Companies worked at']]

    # Preprocessing Data for model
    if not experience or experience < 1 or experience > 80:
        print("Taking default value of experience: 0 yrs")
        experience=0

    # Separate Designition
    if len(designition) != 0:
        desig_list = designition
        # get unique list
        uniq_desig = []
        [uniq_desig.append(x) for x in desig_list if x not in uniq_desig]
        rating_value=0
        designition_count=0
        for desig in uniq_desig:
            if desig in desig_rating.keys():
                rating_value+=int(desig_rating[desig])
                designition_count+=1
    else:
        print("Taking default value for desingation: 0 positions")
        rating_value=0
        designition_count=0
        
    # get skills
    if len(skills) != 0:
        skills = [x.strip() for x in skills if len(x) < 20]
        skill_count=len(skills)
    else:
        print("Taking default value for skills: 0")
        skill_count=0
    
    # Use model to predict rating
    X = numpy.array([experience, rating_value, designition_count, skill_count])
    X = X.reshape(1,-1)
    rating = lr.predict(X)
    if rating < 1:
        rating = 1.0
    elif rating > 5:
        rating = 5.0
    else:
        rating = numpy.ceil(rating)
    print("====================================")
    print("Details for file: ", file.split("/")[-1])
    print("====================================")
    print(name + " | " + phone_no + " | " + email + " | " + " ".join(degree))
    print("-------------------------------------")
    print(" ".join(companies) + " | " + " ".join(college) + " | " + str(experience) + " years")
    print("-------------------------------------")
    print ("Skills", " ".join(skills))
    print("-------------------------------------")
    print("Designation", " ".join(designition))
    print("-------------------------------------")
    print("Rating given by System", rating)

else:
    print("File " + file + " not found")
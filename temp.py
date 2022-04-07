# from flask import request


# data = [
#     {"id": 1, "name": "Jyoti"},
#     {"id": 2, "name": "shashank"},
#     {"id": 3, "name": "Divya"},
# ]

# id = int(input("Enter id"))

# new_id = 3
# new_name = "radha"
# # new_id=request.json['id']
# # new_name=request.json['name']

# for row in data:
#     print(row)
#     if row["id"] == id:
#         row["id"] = new_id
#         row["name"] = new_name

# print(data)

from builtins import print
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)
courses = [
    {
        "Name": "jiya",
        "E_id": "0",
        "description": "WELCOME TO THE GSLAB",
        "price": "57645",
    },
    {
        "Name": "jyoti",
        "E_id": "1",
        "description": "WELCOME TO THE GSLAB",
        "price": "65345",
    },
    {
        "name": "divya",
        "E_id": "2",
        "description": "WELCOME TO THE GSLAB",
        "price": "65236",
    },
    {
        "name": "twinkle",
        "E_id": "3",
        "description": "WELCOME TO THE GSLAB",
        "price": "65236",
    },
]

# method= GET (Retrive all the courses)


@app.route("/courses", methods=["GET"])
def get_course():
    return jsonify({"courses": courses})


# By GET Retrive one course

# @app.route("/courses/getcourse/<int:E_id>", methods=['GET'])
# def get_course_details(E_id):
#     # course = [course for course in courses if(course['E_id']==E_id)]
#     for course in courses:
#         if course['E_id'] == E_id:
#             print(course)
#     return jsonify({'message': 'course is not found!'})


@app.route("/courses/<int:E_id>", methods=["GET"])
def get_courses(E_id):
    course = [course for course in courses if (course["E_id"] == E_id)]
    if "E_id" in request.json:
        print(courses)
    # accessing a element using get()
    # method
    # print("Accessing a element using get:")
    # print(courses.get(""))
    # for data in courses:
    #  for a in data['E_id']:
    #   a1=int(a)
    #   if(a1 == E_id):
    return jsonify({"courses": courses[E_id]})
    # else:
    #  print("asdasdasd")
    #  return jsonify({'sd':"Valid Input"})


# method= POST (create a new course)


@app.route("/courses", methods=["POST"])
def create_courses():
    body_data = request.get_json()
    print(body_data)
    for data in courses:
        if body_data["E_id"] in data["E_id"]:
            return jsonify({"message": "E_id already taken"})
    courses.append(body_data)
    return jsonify({"message": "customer has been created"})


# method= PUT (Updating a an existing resource)


@app.route("/courses/<int:E_id>", methods=["PUT"])
def update_course(E_id):
    course = [course for course in courses if (course["E_id"] == E_id)]
    if "E_id" in request.json:
        print("courses available")
    if "Name" in request.json:
        print(
            request.json["Name"]
        )  # (I am reading the name from the  request and updating the exixt course name)
    courses[0]["Name"] = request.json["Name"]
    if "description" in request.json:
        courses[0]["description"] = request.json["description"]
    if "price" in request.json:
        courses[0]["price"] = request.json["price"]
        return jsonify({"course": courses[0]})


# method= DELETE (Delete the resoures)


@app.route("/courses/<int:E_id>", methods=["DELETE"])
def delete(E_id):
    courses.remove(courses[E_id])
    courses.clear()
    print("\nDeleting Entire Dictionary: ")
    print(courses)
    return jsonify({"message": "Record has been deleted"})


# dict={1:"shyam",2:"Ram"}
# id,name=input("Enter id").split(" ")
# if int(id) in dict:
#     print("Err: Id already taken")
# else:
#     dict[int(id)]=name
#
# print(dict)
# ************Refer Above Code***********

# dict={1:{"Name":"shyam","age":20},2:{"Name":"Ram","age":25}}
# id,name,age=input("Enter Id Name Age").split(" ")
# if int(id) in dict:
#     print("Err: Id already taken")
# else:
#     dict[int(id)]={"Name":name,"age":age}
#
# print(dict)
#
#
# ----------------------------------------------------
# input Format = 2 Shashank 22
# input Format = 3 Jyoti 23
# input Format = 4 Prakhar 20


if __name__ == "__main__":
    app.run(debug=True)

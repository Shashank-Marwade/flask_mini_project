from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = "Secret Key"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///dataEMP.db"
db = SQLAlchemy(app)


class Employee(db.Model):
    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    salary = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.Integer)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.salary} - {self.phone}"


# db.create_all()
@app.route("/")
def Index():
    records = Employee.query.all()
    return render_template("index.html", employees=records)


# Insert
@app.route("/addemp", methods=["POST"])
def addemp():
    """Adding Employee details"""
    if request.method == "POST":
        emp = Employee(
            name=request.form.get("name"),
            phone=int(request.form.get("phone")),
            salary=int(request.form.get("salary")),
        )
        db.session.add(emp)
        db.session.commit()
        flash("Employee Details Added Successfully")
        return redirect(url_for("Index"))


# Delete
@app.route("/delete/<int:id>", methods=["POST", "GET"])
# @app.route("/delete/<int:id>", methods=["GET"])
def delete(id):
    emp = Employee.query.get(id)
    db.session.delete(emp)
    db.session.commit()
    flash("Employee Details Deleted ")
    return redirect(url_for("Index"))


# Upadate
@app.route("/update", methods=["POST"])
# @app.route("/update", methods=["PUT"])
def update():
    if request.method == "POST":
        emp = Employee.query.get(request.form.get("id"))
        # print(type(emp.phone))
        emp.name = request.form["name"]
        emp.salary = int(request.form["salary"])
        emp.phone = int(request.form["phone"])
        db.session.commit()
        flash("Employee Details Updated")
        return redirect(url_for("Index"))


# Nth Highest Salary
@app.route("/salary", methods=["POST", "GET"])
def salary():
    n = int(request.form.get("N")) - 1
    print(
        row := db.session.query(Employee)
        .order_by(Employee.salary.desc())
        .distinct()[n:]
    )

    if row:
        flash("{}th Highest Salary is {}".format(n + 1, row[0].salary))
    else:
        flash("Invalid input")
    return redirect(url_for("Index"))


if __name__ == "__main__":
    app.run(debug=True)

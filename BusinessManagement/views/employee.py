from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    query = """SELECT e.id, e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS company_name from 
    IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""  
    #UCID:ac298; DATE:04/08/23 
    args = []  # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v, v) for v in allowed_columns]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    first_name = request.args.get('fn')
    last_name = request.args.get('ln')
    email = request.args.get('email')
    company = request.args.get('company')
    limit = 10
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    #UCID:ac298; DATE:04/08/23 
    # TODO search-3 append like filter for first_name if provided
    if first_name:
        query += " AND e.first_name like %s"
        args.append(f"%{first_name}%")
    # TODO search-4 append like filter for last_name if provided
    if last_name:
        query += " AND e.last_name like %s"
        args.append(f"%{last_name}%")
    # TODO search-5 append like filter for email if provided
    if email:
        query += " AND email like %s"
        args.append(f"%{email}%")
    # TODO search-6 append equality filter for company_id if provided
    if company:
        query += f" AND company_id = {company}"
    #UCID:ac298; DATE:04/08/23 
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    if column and order:
        print(column, order)
        if column in allowed_columns \
            and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')
    #UCID:ac298; DATE:04/08/23 
 
    print("query", query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        flash(e, "error")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation
    

    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_list)
    
 
@employee.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # TODO add-5a verify email is in the correct format
        has_error = False  # use this to control whether or not an insert occurs

        first_name = str(request.form.get('first_name'))
        if not first_name:
            has_error = True
            flash("First name is required", "danger")
        last_name = str(request.form.get('last_name'))
        if not last_name:
            has_error = True
            flash("Last name is required", "danger")
        email = str(request.form.get('email'))
        if not email:
            has_error = True
            flash("email is required", "danger")
        company = str(request.form.get('company')) or None
    

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Employees
                (first_name, last_name, company_id, email) VALUES (%s, %s, %s, %s);
                """, first_name, last_name, company, email)  # <-- TODO add-6 add query and add arguments
                if result.status:
                    flash("Created Employee Record", "success")
            except Exception as e:
                print(e)
                # TODO add-7 make message user friendly
                flash(str(e), "danger")
    return render_template("add_employee.html")
    


@employee.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get('id')
    if not id:  # TODO update this for TODO edit-1
        flash("Company ID is missing", "danger")
    else:
        if request.method == "POST":            
            # TODO edit-1 retrieve form data for first_name, last_name, company, email
            first_name = str(request.form.get('first_name'))
            last_name = str(request.form.get('last_name'))
            email = str(request.form.get('email'))
            company_id = str(request.form.get('company'))
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == '' or first_name == None:
                flash("first name is required", "danger")
                return redirect("add")
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == '' or last_name == None:
                flash("last name is required", "danger")
                return redirect("add")
            # TODO edit-4 company (may be None)
            if company_id == '':
                company_id = None
            # TODO edit-5 email is required (flash proper error message)
            if email == '' or email == None:
                flash("email is required", "danger")
                return redirect("add")
            # TODO edit-5a verify email is in the correct format
            has_error = False  # use this to control whether or not an insert occurs
            
            if not has_error:
                try:
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                    """,first_name,last_name,company_id, email, id)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-7 make this user-friendly
                    flash(f" Following exception occured while updating the employee", "danger")
                    
        row = {}
        try:
            # TODO edit-8 fetch the updated data
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS 
            company_name from IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE e.id = %s""", id)
            
            if result.status:
                row = result.row
        except Exception as e:
            # TODO edit-9 make this user-friendly
            flash(f" Following exception occured while fetching the updated employee record", "danger")
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)
    


@employee.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 if id is missing, flash necessary message and redirect to search
    id = request.args.get("id")
    
    args = {**request.args}
    if id:
        try:
            result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
            if result.status:
                flash("Deleted Employee record", "success")
        except Exception as e:
            flash(f" Following exception occured while deleting the employee record", "danger")
        del args["id"]
    flash(f" id is missing", "danger")
    return redirect(url_for("employee.search", **args))
    pass
    

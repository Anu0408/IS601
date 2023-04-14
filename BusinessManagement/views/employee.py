from flask import Blueprint, render_template, request, flash, redirect, url_for
from sql.db import DB
employee = Blueprint('employee', __name__, url_prefix='/employee')


@employee.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve employee id as id, first_name, last_name, email, company_id, company_name using a LEFT JOIN
    # Select query to get the required data
    query = """SELECT e.id as id, e.first_name, e.last_name, e.email, e.company_id, c.name as company_name 
    FROM IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE 1=1"""
    args = [] # <--- append values to replace %s placeholders
    allowed_columns = ["first_name", "last_name", "email", "company_name"]
    allowed_list = [(v,v) for v in allowed_columns]
    # TODO search-2 get fn, ln, email, company, column, order, limit from request args
    # retreving the arguments from form
    fn = request.args.get('first_name')
    ln = request.args.get('last_name')
    email = request.args.get('email')
    company = request.args.get('company')
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    # TODO search-3 append like filter for first_name if provided
    # TODO search-4 append like filter for last_name if provided
    # TODO search-5 append like filter for email if provided
    # TODO search-6 append equality filter for company_id if provided
    # TODO search-7 append sorting if column and order are provided and within the allowed columns and order options (asc, desc)
    # TODO search-8 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-9 provide a proper error message if limit isn't a number or if it's out of bounds
    # adding the where statemnts based on input
    if fn:
        query += " AND e.first_name like %s"
        args.append(f"%{fn}%")
    if ln:
        query += " AND e.last_name like %s"
        args.append(f"%{ln}%")
    if email:
        query += " AND e.email like %s"
        args.append(f"%{email}%")
    if company:
        query += " AND e.company_id = %s"
        args.append(int(company))
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')
    #UCID:ac298
    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-10 make message user friendly
        # flash message for exception
        print(e)
        flash("Error occured, please check the data and try again", "error")
    # hint: use allowed_columns in template to generate sort dropdown
    return render_template("list_employees.html", rows=rows, allowed_columns=allowed_list)

@employee.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for first_name, last_name, company, email
        # TODO add-2 first_name is required (flash proper error message)
        # TODO add-3 last_name is required (flash proper error message)
        # TODO add-4 company (may be None)
        # TODO add-5 email is required (flash proper error message)
        # retrieving the employee data and checking for the required files
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        company = request.form.get("company")
        print(company)
        email = request.form.get("email")
        if first_name == "":
            flash("Enter first name", 'warning')
            return redirect(request.url)
        if last_name == "":
            flash("Enter last name", 'warning')
            return redirect(request.url)
        if email == "":
            flash("Enter email", 'warning')
            return redirect(request.url)
        #UCID: ac298
        
        try:
            # Insert query to add the employee data to DB
            result = DB.insertOne("""INSERT INTO IS601_MP3_Employees (first_name, last_name, email, company_id)
                        VALUES (%(first_name)s, %(last_name)s, %(email)s, %(company_name)s)
                        ON DUPLICATE KEY UPDATE first_name=%(first_name)s, last_name = %(last_name)s, email = %(email)s, company_id = %(company_name)s""",
            {'first_name':first_name, 'last_name':last_name, 'email':email, 'company_name':company})
            # <-- TODO add-6 add query and add arguments
            if result.status:
                flash("Created Employee Record", "success")
        except Exception as e:
            # TODO add-7 make message user friendly
            # message for exception
            print(e)
            flash("Exception occured: " + str(e), "danger")
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
            #UCID: ac298
            # TODO edit-2 first_name is required (flash proper error message)
            if first_name == '' or first_name == None:
                flash("first name is required", "danger")
                return redirect("add")
             #UCID: ac298
            # TODO edit-3 last_name is required (flash proper error message)
            if last_name == '' or last_name == None:
                flash("last name is required", "danger")
                return redirect("add")
             #UCID: ac298
            # TODO edit-4 company (may be None)
            if company_id == '':
                company_id = None
                 #UCID: ac298
            # TODO edit-5 email is required (flash proper error message)
            if email == '' or email == None:
                flash("email is required", "danger")
                return redirect("add")
             #UCID: ac298
            # TODO edit-5a verify email is in the correct format
            has_error = False  # use this to control whether or not an insert occurs
            
            if not has_error:
                try:
                     #UCID: ac298
                    # TODO edit-6 fill in proper update query
                    result = DB.update("""
                    UPDATE IS601_MP3_Employees SET first_name = %s, last_name = %s, company_id = %s, email = %s WHERE id = %s
                    """,first_name,last_name,company_id, email, id)
                    
                    if result.status:
                        flash("Updated record", "success")
                except Exception as e:
                     #UCID: ac298
                    # TODO edit-7 make this user-friendly
                    flash(f" Following exception occured while updating the employee", "danger")
                    
        row = {}
        try:
             #UCID: ac298
            # TODO edit-8 fetch the updated data
            result = DB.selectOne("""SELECT e.first_name, e.last_name, e.email, e.company_id, IF(c.name is not null, c.name,'N/A') AS 
            company_name from IS601_MP3_Employees e LEFT JOIN IS601_MP3_Companies c ON e.company_id = c.id WHERE e.id = %s""", id)
            
            if result.status:
                row = result.row
        except Exception as e:
             #UCID: ac298
            # TODO edit-9 make this user-friendly
            flash(f"{e}", "danger")
             #UCID: ac298
    # TODO edit-10 pass the employee data to the render template
    return render_template("edit_employee.html", employee=row)
 #UCID: ac298

@employee.route("/delete", methods=["GET"])
def delete():
     #UCID: ac298

    # code for deleting employee
    id = request.args.get('id')
    args = {**request.args}
    # TODO delete-1 delete employee by id
    # TODO delete-2 redirect to employee search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    if id:
        result = DB.delete("DELETE FROM IS601_MP3_Employees WHERE id = %s", id)
        del args['id']
        if result:
            flash("Deleted successfully", 'success')
    return redirect(url_for("employee.search", **args))
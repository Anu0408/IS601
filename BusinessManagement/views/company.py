from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
company = Blueprint('company', __name__, url_prefix='/company')

@company.route("/search", methods=["GET"])
def search():
    rows = []
    # DO NOT DELETE PROVIDED COMMENTS
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    # don't do SELECT *

    query = """SELECT c.id, c.name, c.address, c.city, c.country, c.state, c.zip, c.website, COUNT(e.id) AS employees FROM IS601_MP3_Companies c 
    LEFT JOIN IS601_MP3_Employees e ON e.company_id = c.id WHERE 1=1 """
    #UCID:ac298;Date:04/08/23
    args = []  # <--- add values to replace %s/%(named)s placeholders
    allowed_columns = ["name", "city", "country", "state"]
    allowed_list = [(v, v) for v in allowed_columns]
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get('name')
    country = request.args.get('country')
    state = request.args.get('state')
    limit = 10
    column = request.args.get('column')
    order = request.args.get('order')
    limit = request.args.get('limit')
    #UCID:ac298;Date:04/08/23
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        query += " AND c.name like %s"
        args.append(f"%{name}%")
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND c.country like %s"
        args.append(f"%{country}%")
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND c.state like %s"
        args.append(f"%{state}%")
    #UCID:ac298;Date:04/08/23
    query += " GROUP BY c.id"
    # TODO search-6 append sorting if column and order are provided and within the allows columsn and allowed order asc,desc
    if column and order:
        if column in allowed_columns and order in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
     #UCID:ac298;Date:04/08/23
    # TODO search-7 append limit (default 10) or limit greater than 1 and less than or equal to 100
    # TODO search-8 provide a proper error message if limit isn't a number or if it's out of bounds
    if limit and int(limit) > 0 and int(limit) <= 100:
        query += " LIMIT %s"
        args.append(int(limit))
    elif limit and (int(limit) <= 0 or int(limit) > 100):
        flash("Enter the limit between 1 and 100", 'warning')
         #UCID:ac298;Date:04/08/23

    print("query", query)
    print("args", args)
    try:
        result = DB.selectAll(query, *args)
        # print(f"result {result.rows}")
        if result.status:
            rows = result.rows
            print(f"rows {rows}")
    except Exception as e:
        # TODO search-9 make message user friendly
        flash(str(e), "danger")
    # hint: use allowed_columns in template to generate sort dropdown
    # hint2: convert allowed_columns into a list of tuples representing (value, label)
    # do this prior to passing to render_template, but not before otherwise it can break validation

    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_list)
    #UCID:ac298;Date:04/08/23


@company.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        has_error = False  # use this to control whether or not an insert occurs

        name = str(request.form['name'])
        if not name:
            has_error = True
            flash("Company name is required", "danger")
        address = str(request.form['address'])
        if not address:
            has_error = True
            flash("Address is required", "danger")
        city = str(request.form['city'])
        if not city:
            has_error = True
            flash("city is required", "danger")
        country = str(request.form['country'])
        state = str(request.form['state'])
        zip = str(request.form['zip'])
        if not name:
            has_error = True
            flash("Zipcode is required", "danger")
        website = str(request.form['website'])
        #UCID:ac298;Date:04/08/23

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies
                (name, address, city, country, state, zip, website) VALUES(%s, %s, %s, %s, %s, %s, %s)
                """, name, address, city, country, state, zip, website)  # <-- TODO add-8 add query and add arguments
                #UCID:ac298;Date:04/08/23
                if result.status:
                    flash("Added Company", "success")
            except Exception as e:
                # TODO add-9 make message user friendly
                flash(str(e), "danger")

    return render_template("add_company.html")


@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get('id') or False
    if not id:  # TODO update this for TODO edit-1
        flash("Company ID is missing", "danger")
    else:
        if request.method == "POST":
            # use this as needed, can convert to tuple if necessary
            data = {"id": id}
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)

            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            has_error = False  # use this to control whether or not an insert occurs


            name = str(request.form.get('name'))
            if not name:
                has_error = True
                flash("Company name is required", "danger")
            address = str(request.form.get('address'))
            if not address:
                has_error = True
                flash("Address is required", "danger")
            city = str(request.form.get('city'))
            if not city:
                has_error = True
                flash("city is required", "danger")
            country = str(request.form.get('country'))
            state = str(request.form.get('state'))
            zip = str(request.form.get('zip'))
            if not zip:
                has_error = True
                flash("Zipcode is required", "danger")
            website = str(request.form.get('website') or '')
            #UCID:ac298;Date:04/08/23

            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET
                        name = %s,
                        address = %s,
                        city = %s,
                        country = %s,
                        state = %s,
                        zip = %s,
                        website = %s
                    WHERE id = %s
                    """, name, address, city, country, state, zip, website, id)
                                #UCID:ac298;Date:04/08/23

                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash(str(e), "danger")
                    #UCID:ac298;Date:04/08/23
    row = {}
    try:
        # TODO edit-11 fetch the updated data
        result = DB.selectOne(
            "SELECT name, address, city, country, state, zip, website FROM IS601_MP3_Companies WHERE id = %s", id)
        if result.status:
            row = result.row
    #UCID:ac298;Date:04/08/23
    except Exception as e:
        # TODO edit-12 make this user-friendly
        flash(str(e), "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", company=row)
#UCID:ac298;Date:04/08/23

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search

    id = request.args.get('id')
    #UCID:ac298; Date: 04/08/23
    print("printing id:",id)
    args = {**request.args}
    if id:
        DB.update("""UPDATE IS601_MP3_Employees SET company_id = %s where company_id = %s""", None, id)
        result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %s", id)
        del args['id']
        if result:
            flash("Deleted successfully", 'success')
    return redirect(url_for("company.search", **args))
    pass
     #UCID:ac298; Date: 04/08/23
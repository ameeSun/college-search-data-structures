from flask import Flask, redirect, render_template, request
from helpers import state_select, main_campus, locale_select
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", methods=["GET", "POST", "POST1"])
def main():
	where_sql=""
	selected_state=""
	locale=""
	search = ""
	main_checked = False
	admission_checked = False
	search1 = ""
	admission=""
	tuition=""
	if request.method=="POST":
		selected_state=request.form.get('state')
		locale=request.form.get('locale')
		search=request.form.get('query')
		admission=request.form.get('admission')
		tuition=request.form.get('tuition')
		if search !=None:
			search1 = search
			where_sql=f" AND INSTNM LIKE '%{search}%'"
		else:
			if search1 !="":
				where_sql=f" AND INSTNM LIKE '%{search1}%'"
			if selected_state!="":
				where_sql= where_sql+f" AND STABBR = '{selected_state}'"
			if 'main' in request.form:
				main_checked = True
				where_sql = where_sql + " AND MAIN = 1"
			if locale !="":
				where_sql= where_sql+ f" AND LOCALE = '{locale}'"
			if admission!="":
				if admission=="Ascending":
					where_sql=where_sql + " and adm_rate != 0 ORDER BY ADM_RATE ASC"
				elif admission=="Descending":
					where_sql=where_sql + " and adm_rate != 0 ORDER BY ADM_RATE DESC"
			if tuition!="":
				if tuition=="Ascending":
					where_sql=where_sql + " and TUITIONFEE_OUT != 'NULL' ORDER BY TUITIONFEE_OUT ASC"
				elif tuition=="Descending":
					where_sql=where_sql + " and TUITIONFEE_OUT != 'NULL' ORDER BY TUITIONFEE_OUT DESC"
	with sqlite3.connect('college.db') as conn:
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		# assemble the db query
		que = "update colleges set ADM_RATE = ADM_RATE *100 where 1 = 1"
		#que1 = "update colleges set TUITIONFEE_OUT = 0 where TUITIONFEE_OUT IS NULL and 1=1"
		query = f"SELECT UNITID, INSTNM, CITY, STABBR, ZIP, INSTURL, ROUND(ADM_RATE,2) as ADM_RATE, TUITIONFEE_OUT FROM colleges WHERE 1=1 {where_sql}"
		#cursor.execute(que1)
		cursor.execute(query)
		rows = (cursor.fetchall())
	return render_template("index.html", colleges = rows, states=state_select(selected_state), main=main_campus(main_checked), adm=admission, srch = search, locales=locale_select(locale), tuit=tuition)

# College detail page
@app.route('/college/<college_id>')
def detail(college_id):
	with sqlite3.connect('college.db') as conn:
		conn.row_factory = sqlite3.Row
		cursor = conn.cursor()
		cursor.execute("SELECT UNITID, INSTNM, CITY, STABBR, ZIP, INSTURL, LATITUDE, LONGITUDE, ADM_RATE, SAT_AVG, COSTT4_A, TUITIONFEE_IN, TUITIONFEE_OUT, UGDS, UGDS_WHITE, UGDS_BLACK, UGDS_HISP, UGDS_ASIAN, UGDS_AIAN, UGDS_NHPI, UGDS_2MOR, UGDS_NRA, UGDS_UNKN, ACTCMMID FROM colleges WHERE UNITID=?", [college_id])
		row = (cursor.fetchone())
	return render_template("detail.html", college = row)



app.run(host='0.0.0.0', port=8080)

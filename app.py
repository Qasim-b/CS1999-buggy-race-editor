from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)

DATABASE_FILE = "database.db"
DEFAULT_BUGGY_ID = "1"

BUGGY_RACE_SERVER_URL = "http://rhul.buggyrace.net"


#------------------------------------------------------------
# the index page
#------------------------------------------------------------
@app.route('/')
def home():
   return render_template('index.html', server_url=BUGGY_RACE_SERVER_URL)

#------------------------------------------------------------
# creating a new buggy:
#  if it's a POST request process the submitted data
#  but if it's a GET request, just show the form
#------------------------------------------------------------
@app.route('/new', methods = ['POST', 'GET'])
def create_buggy():
  if request.method == 'GET':

      con = sql.connect(DATABASE_FILE)
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * FROM buggies")
      record = cur.fetchone();

      return render_template("buggy-form.html",buggy = record)
  elif request.method == 'POST':  ## added all data entry fields, need to validate and add costs

    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies")
    record = cur.fetchone();

    msg=""
    violations=""
    qty_wheels = request.form['qty_wheels'] # basic validation for integer entries., used to work until did task2-edit. But since then user only able to input numbers so no need to check if string
    flag_color = request.form['flag_color']
    flag_color_secondary = request.form['flag_color_secondary']
    flag_pattern = request.form['flag_pattern']
    power_type = request.form['power_type']
    power_units = request.form['power_units']
    aux_power_type = request.form['aux_power_type']
    aux_power_units = request.form['aux_power_units']
    hamster_booster = request.form['hamster_booster']
    tyres = request.form['tyres']
    qty_tyres = request.form['qty_tyres']
    armour = request.form['armour']
    attack = request.form['attack']
    qty_attack = request.form['qty_attack']
    fireproof = request.form['fireproof']
    insulated = request.form['insulated']
    antibiotic = request.form['antibiotic']
    banging = request.form['banging']
    algo = request.form['algo']
    if not qty_wheels.isdigit(): ##has no use, just used to show i did task 1-valid. Dont need anymore.
        msg = f"rule violated, enter a number for quantity of wheels!"
        return render_template("buggy-form.html",buggy = record, msg=msg)
    if int(qty_wheels)%2 != 0: ## check if even
        msg = f"rule violated, there needs to be an even number of wheels!"
        return render_template("buggy-form.html",buggy = record, msg=msg)
    if str(flag_color) == str(flag_color_secondary) and str(flag_pattern) != "plain": ## check if flag colors are not similar if pattern not plain
        msg = f"rule violated, both flag colors cannot be the same"
        return render_template("buggy-form.html",buggy = record, msg=msg)
    if int(qty_tyres) < int(qty_wheels): ## check if enough tyres
        msg = f"rule violated, there are not enough tires!"
        return render_template("buggy-form.html",buggy = record, msg=msg)


    power_cost = 0

    if power_type == "petrol": ##cost calculations hardcoded into program
        power_cost = int(power_units) * 4
    elif power_type == "fusion":
        power_cost = int(power_units) * 400
    elif power_type == "steam":
        power_cost = int(power_units) * 3
    elif power_type == "bio":
        power_cost = int(power_units) * 5
    elif power_type == "electric":
        power_cost = int(power_units) * 20
    elif power_type == "rocket":
        power_cost = int(power_units) * 16
    elif power_type == "hamster":
        power_cost = int(power_units) * 3
    elif power_type == "thermo":
        power_cost = int(power_units) * 300
    elif power_type == "solar":
        power_cost = int(power_units) * 40
    elif power_type == "solar":
        power_cost = int(power_units) * 20

    aux_power_cost = 0

    if aux_power_type == "petrol":
        aux_power_cost = int(aux_power_units) * 4
    elif aux_power_type == "fusion":
        aux_power_cost = int(aux_power_units) * 400
    elif aux_power_type == "steam":
        aux_power_cost = int(aux_power_units) * 3
    elif aux_power_type == "bio":
        aux_power_cost = int(aux_power_units) * 5
    elif aux_power_type == "electric":
        aux_power_cost = int(aux_power_units) * 20
    elif aux_power_type == "rocket":
        aux_power_cost = int(aux_power_units) * 16
    elif aux_power_type == "hamster":
        aux_power_cost = int(aux_power_units) * 3
    elif aux_power_type == "thermo":
        aux_power_cost = int(aux_power_units) * 300
    elif aux_power_type == "solar":
        aux_power_cost = int(aux_power_units) * 40
    elif aux_power_type == "solar":
        aux_power_cost = int(aux_power_units) * 20

    tyres_cost= 0
    if tyres == "knobbly":
        tyres_cost = int(qty_tyres) * 15
    if tyres == "slick":
        tyres_cost = int(qty_tyres) * 10
    if tyres == "steelband":
        tyres_cost = int(qty_tyres) * 20
    if tyres == "reactive":
        tyres_cost = int(qty_tyres) * 40
    if tyres == "maglev":
        tyres_cost = int(qty_tyres) * 50

    armour_cost=0
    if armour == "wood": ##need to modify cost based on number of wheels
        armour_cost=40
    elif armour == "aluminium":
        armour_cost=200
    elif armour == "thinsteel":
        armour_cost=100
    elif armour == "thicksteel":
        armour_cost=200
    elif armour == "titanium":
        armour_cost=290

    attack_cost=0
    if attack == "spike":
        attack_cost = int(qty_attack) * 5
    if attack == "flame":
        attack_cost = int(qty_attack) * 20
    if attack == "charge":
        attack_cost = int(qty_attack) * 28
    if attack == "biohazard":
        attack_cost = int(qty_attack) * 30

    hamster_booster_cost = int(hamster_booster) * 5
    fireproof_cost = 0
    if fireproof == "True":
        fireproof_cost=70
    insulated_cost= 0
    if insulated == "True":
        insulated_cost=100
    antibiotic_cost=0
    if antibiotic == "True":
        antibiotic_cost=90
    banging_cost= 0
    if banging == "True":
        banging_cost=42


    overall_cost = power_cost + aux_power_cost + tyres_cost + armour_cost + attack_cost + hamster_booster_cost + fireproof_cost + insulated_cost + antibiotic_cost + banging_cost


    try:
      with sql.connect(DATABASE_FILE) as con:
        cur = con.cursor()
        cur.execute("UPDATE buggies set qty_wheels=?, flag_color=?, flag_color_secondary=?, flag_pattern=?, power_type=?, power_units=?, aux_power_type=?, aux_power_units=?, hamster_booster=?, tyres=?, qty_tyres=?, armour=?, attack=?, qty_attack=?, fireproof=?, insulated=?, antibiotic=?, banging=?, algo=?, total_cost=? WHERE id=?",
        (qty_wheels, flag_color, flag_color_secondary, flag_pattern, power_type, power_units, aux_power_type, aux_power_units, hamster_booster, tyres, qty_tyres, armour, attack, qty_attack, fireproof, insulated, antibiotic, banging, algo, overall_cost, DEFAULT_BUGGY_ID))
        con.commit()
        msg = "Record successfully saved"
    except:
      con.rollback()
      msg = "error in update operation"
    finally:
      con.close()
      return render_template("updated.html", msg = msg)

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/buggy')
def show_buggies(): ## test hardcode code cost into this
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies")
  record = cur.fetchone();
  return render_template("buggy.html", buggy = record) ##test cost

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/new')
def edit_buggy():
  return render_template("buggy-form.html")


#------------------------------------------------------------
# get JSON from current record
#   this is still probably right, but we won't be
#   using it because we'll be dipping diectly into the
#   database
#------------------------------------------------------------
@app.route('/json')
def summary():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies WHERE id=? LIMIT 1", (DEFAULT_BUGGY_ID))
  return jsonify(
      {k: v for k, v in dict(zip(
        [column[0] for column in cur.description], cur.fetchone())).items()
        if (v != "" and v is not None)
      }
    )

#------------------------------------------------------------
# delete the buggy
#   don't want DELETE here, because we're anticipating
#   there always being a record to update (because the
#   student needs to change that!)
#------------------------------------------------------------
@app.route('/delete', methods = ['POST'])
def delete_buggy():
  try:
    msg = "deleting buggy"
    with sql.connect(DATABASE_FILE) as con:
      cur = con.cursor()
      cur.execute("DELETE FROM buggies")
      con.commit()
      msg = "Buggy deleted"
  except:
    con.rollback()
    msg = "error in delete operation"
  finally:
    con.close()
    return render_template("updated.html", msg = msg)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")

from flask import Flask, render_template, request
from carbon_calculator import CarbonCalculator
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
   if request.method == "POST":
       origin = request.form.get("origin")
       destination = request.form.get("destination")
       distance_km = float(request.form.get("distance_km"))
       mode = request.form.get("mode")
       # Calculate carbon emissions
       emissions = CarbonCalculator.calculate_emissions(distance_km, mode)
       eco_mode = CarbonCalculator.suggest_eco_friendly_mode(distance_km)
       return render_template("results.html", emissions=emissions, eco_mode=eco_mode)
   return render_template("index.html")
if __name__ == "__main__":
   app.run(debug=True)
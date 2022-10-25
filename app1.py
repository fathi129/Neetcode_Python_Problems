from flask import Flask, jsonify

justice_league_members = [
    {"superhero": "Aquaman", "real_name": "Arthur Curry"},
    {"superhero": "Batman", "real_name": "Bruce Wayne"},
    {"superhero": "Cyborg", "real_name": "Victor Stone"},
    {"superhero": "Flash", "real_name": "Barry Allen"},
    {"superhero": "Green Lantern", "real_name": "Hal Jordan"},
    {"superhero": "Superman", "real_name": "Clark Kent Kal-El"},
    {"superhero": "Wonder Woman", "real_name": "Princess Diana"}
]

#################################################
# Flask Setup
#################################################
app1 = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app1.route("/api/v1.0/justice-league")
def justice_league():
    """Return the justice league data as json"""

    return jsonify(justice_league_members)


@app1.route("/")
def welcome():
    return (
        f"Welcome to the Justice League API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/justice-league<br/>"
        f"/api/v1.0/justice-league/Arthur%20Curry<br/>"
        f"/api/v1.0/justice-league/Bruce%20Wayne<br/>"
        f"/api/v1.0/justice-league/Victor%20Stone<br/>"
        f"/api/v1.0/justice-league/Barry%20Allen<br/>"
        f"/api/v1.0/justice-league/Hal%20Jordan<br/>"
        f"/api/v1.0/justice-league/Clark%20Kent%20Kal-El<br/>"
        f"/api/v1.0/justice-league/Princess%20Diana"
    )


# @app1.route("/api/v1.0/justice-league/<real_name>")
# def justice_league_character(real_name):
#     """Fetch the Justice League character whose real_name matches
#        the path variable supplied by the user, or a 404 if not."""

#     canonicalized = real_name.replace(" ", "").lower()
#     for character in justice_league_members:
#         search_term = character["real_name"].replace(" ", "").lower()

#         if search_term == canonicalized:
#             return character

#     return {"error": f"Character with real_name {real_name} not found."}, 404

@app1.route("/api/v1.0/justice-league/super/<superhero>")

def justice_league_superhero(superhero):
    rtn = {}
    found = False
    for hero in justice_league_members:
        if(hero["superhero"]==superhero):
            rtn = hero
            found = True
            break
    if not found:
        rtn = {"error": f"Character with superhero {superhero} not found."}
        status_code = 404
    else:
        status_code = 200  
    
    return(jsonify(rtn),status_code)

@app1.route("/api/v1.0/justice-league/<real_name>")
def justice_league_realname(real_name):
    user_term = real_name.replace(" ","").lower()
    for real in justice_league_members:

        original = real["real_name"].replace(" ","").lower()
        if user_term == original:
            return real  
        return "error:not found"    
if __name__ == "__main__":
    app1.run(debug=True)


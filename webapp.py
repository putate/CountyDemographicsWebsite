from flask import Flask, request, Markup, render_template, flash, Markup import os
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')
  
 def get_state_options
    listOfStates = []
    for county in counties
        if county["State"] in listOfStates:
        else:
            listOfStates.append(county["State"])
    options = ""
    for state in listOfStates
        options = options + ""
        return options
  
  
    
if __name__=="__main__":
    app.run(debug=False, port=54321)

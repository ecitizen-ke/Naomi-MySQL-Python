from flask import Blueprint, request, jsonify, make_response
from app.model import State

import os
from dotenv import load_dotenv
load_dotenv()

state_bp = Blueprint("state_bp", __name__)

@state_bp.route("/register", methods=["POST"])
def register():
    """
    this function creates a new state
    """
    # initialize the state object
    state=State()

    # Get data from the request object
    data = request.get_json()

    name=data.get("name")
    abbreviation=data.get("abbreviation")
    capital=data.get("capital")
    population=data.get("population")
    year_admitted=data.get("year_admitted")

    # invoke create state method

    result=state.create(name, abbreviation, capital,population, year_admitted)

    if result:
        response=make_response({"message": "state created successfully", "status": 201,"result":data},201)
        return response
    else:
        response=make_response({"message": "state not created successfully", "status": 400},400)
        return response


@state_bp.route("/states",methods=["GET"])
def getStates():
    """
    this function lists all states
    """
    state=State()

    result=state.get_States()
    
    if result:
        response=make_response({"message": "state displayed successfully", "status": 201,"result":result},201)
        return response
    else:
        response=make_response({"message": "states not displayed", "status": 400},400)
        return response


@state_bp.route("/updateState",methods=["PUT"])
def updateState():
    state=State()

    data=request.get_json()

    id=data.get("id")
    population=data.get("population")
    
    result=state.update_State(id,population)
    
    if result:
        response=make_response({"message": "state updated successfully", "status": 202,"result":result},202)
        return response
    else:
        response=make_response({"message": "states not updated", "status": 400},400)
        return response


@state_bp.route("/deleteState",methods=["DELETE"])
def deleteState():
    state=State()

    data=request.get_json()

    id=data.get("id")

    result=state.delete_State(id)
    
    if result:
        response=make_response({"message": "state deleted successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "states not deleted", "status": 400},400)
        return response

@state_bp.route("/filterStateStartingWithA",methods=["GET"])
def filterStateStartingWithA():
    """
    this function filters all states staring with letter 'A'
    """
    state=State()

    result=state.filter_State_Starting_with_A()
    
    if result:
        response=make_response({"message": "state filtered successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "states not filtered", "status": 400},400)
        return response

@state_bp.route("/searchStateByName",methods=["POST"])
def searchStateByName():
    """
    this functions searches for state details by name
    """
    state=State()

    data=request.get_json()

    name=data.get("name")

    result=state.search_State_By_Name(name)

    if result:
        response=make_response({"message": "search successful", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "search unsuccessful", "status": 400},400)
        return response

@state_bp.route("/listStateCapitals",methods=["GET"])
def listStateCapital():
    """
    this function lists state capitals in ascending format
    """
    state=State()

    result=state.list_State_Capital()
    
    if result:
        response=make_response({"message": "states listed successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "states not listed", "status": 400},400)
        return response


@state_bp.route("/findMostPopulousState",methods=["GET"])
def findMostPopulousState():
    """
    this function finds most populous states
    """
    state=State()

    result=state.find_Most_Populous_State()
    
    if result:
        response=make_response({"message": "most popular state listed successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "most popular state not listed", "status": 400},400)
        return response

@state_bp.route("/averagePopulation",methods=["GET"])
def averagePopulation():
    """
    this function finds average of population
    """
    state=State()

    result=state.average_Population()

    if result:
        response=make_response({"message": "average of population listed successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "average of population not listed", "status": 400},400)
        return response

@state_bp.route("/statesAdmittedBetween1750And1850",methods=["GET"])
def statesAdmittedBetween1750And1850():
    """
    this function lists states admitted between 1750 and 1850
    """
    state=State()

    result=state.states_Admitted_Between_1750_And_1850()
    
    if result:
        response=make_response({"message": "states admitted between 1750 and 1850 listed successfully", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "states not listed", "status": 400},400)
        return response


@state_bp.route("/countStatesByPopulation",methods=["GET"])
def countStatesByPopulation():
    """
    this function counts states by population range
    """
    state=State()

    result=state.count_States_By_Population()
        
    if result:
        response=make_response({"message": "states counted within population range 1000000 and 5000000 listed", "status": 200,"result":result},200)
        return response
    else:
        response=make_response({"message": "states not listed", "status": 400},400)
        return response

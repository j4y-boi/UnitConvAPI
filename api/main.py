# UnitConv API
# Convert values between worlds! (not literally, please dont time travel)
# made by j4y_boi

from flask import Flask, jsonify, request, redirect
app = Flask(__name__)

@app.route('/miles_kilometer', methods=['GET'])
def miles_to_kilometers():
    try:
        data = request.args

        # structure becaus yeah
        if "amount" not in data or "to_unit" not in data:
            return jsonify({"error": "Uh oh! You forgot 'amount' and/or 'to_unit'!"}), 400

        amount = float(data["amount"])
        to_unit = data["to_unit"]

        if not isinstance(amount, (int, float)):
            return jsonify({"error": "'amount' must be a number."}), 400

        # this is COMPLETELY foolproof no way anybody's gonna break this
        if "kilometer" in to_unit:
            kilometers = amount * 1.60934
            return jsonify({"miles": amount, "kilometers": kilometers}), 200
        elif "mile" in to_unit:
            miles = amount * 0.621371
            return jsonify({"kilometers": amount, "miles": miles}), 200
        else:
            return jsonify({"error": f"Invalid 'to_unit': {to_unit}. Valid options are 'kilometers' and 'miles'."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/feet_meter', methods=['GET'])
def feet_to_meters():
    try:
        data = request.args

        # structure becaus yeah
        if "amount" not in data or "to_unit" not in data:
            return jsonify({"error": "Uh oh! You forgot 'amount' and/or 'to_unit'!"}), 400

        amount = float(data["amount"])
        to_unit = data["to_unit"]

        if not isinstance(amount, (int, float)):
            return jsonify({"error": "'amount' must be a number."}), 400

        # this is COMPLETELY foolproof no way anybody's gonna break this
        if "meter" in to_unit:
            meter = amount * 0.3048 
            return jsonify({"feet": amount, "meters": meter}), 200
        elif "feet" in to_unit:
            feet = amount * 3.28084
            return jsonify({"meter": amount, "feet": feet}), 200
        else:
            return jsonify({"error": f"Invalid 'to_unit': {to_unit}. Valid options are 'meter' and 'feet'."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/inch_centimeter', methods=['GET'])
def inch_to_cm():
    try:
        data = request.args

        if "amount" not in data or "to_unit" not in data:
            return jsonify({"error": "Uh oh! You forgot 'amount' or/and 'to_unit'!"}), 400

        amount = float(data["amount"])
        to_unit = data["to_unit"]

        if not isinstance(amount, (int, float)):
            return jsonify({"error": "'amount' must be a number."}), 400

        if "inch" in to_unit:
            inch = amount / 2.54
            return jsonify({"centimeters": amount, "inches": inch}), 200
        elif "centimeter" in to_unit:
            cm = amount * 2.54
            return jsonify({"inches": amount, "centimeters": cm}), 200
        else:
            return jsonify({"error": f"Invalid 'to_unit': {to_unit}. Valid options are 'inch' and 'centimeter'."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/gallon_liter', methods=['GET'])
def gallon_to_liters():
    try:
        data = request.args

        if "amount" not in data or "to_unit" not in data or "region" not in data:
            return jsonify({"error": "Uh oh! You forgot 'amount', 'to_unit' or 'region'!"}), 400

        amount = float(data["amount"])
        to_unit = data["to_unit"]
        region = data["region"]

        if not isinstance(amount, (int, float)):
            return jsonify({"error": "'amount' must be a number."}), 400

        if region == "us":
            # this is COMPLETELY foolproof no way anybody's gonna break this
            if "gallon" in to_unit:
                gallon = amount * 0.264172
                return jsonify({"liters": amount, "gallons": gallon, "region": region}), 200
            elif "liter" in to_unit:    
                liter = amount * 3.78541
                return jsonify({"gallons": amount, "liters": liter, "region": region}), 200
            else:
                return jsonify({"error": f"Invalid 'to_unit': {to_unit}. Valid options are 'gallons' and 'liters'."}), 400
        elif region == "uk": #yeah there are two types of gallon
            if "gallon" in to_unit:
                gallon = amount * 0.219969
                return jsonify({"liters": amount, "gallons": gallon, "region": region}), 200
            elif "liter" in to_unit:    
                liter = amount * 4.54609
                return jsonify({"gallons": amount, "liters": liter, "region": region}), 200
            else:
                return jsonify({"error": f"Invalid 'to_unit': {to_unit}. Valid options are 'gallons' and 'liters'."}), 400
        else:
            return jsonify({"error": f"Invalid 'region: {to_unit}. Valid options are 'us' and 'uk'."}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/bulkconvert', methods=['POST'])
def bulkconvert():
    try:
        data = request.get_json()

        # gotta have the S T R U C T U R E
        if "conversions" not in data:
            return jsonify({"error": "Whoops! You forgot the 'conversions' part..."}), 400

        conversions = data["conversions"]
        results = []

        # all the conversion stuffs
        supported_units = ["miles", "kilometers", "feet", "meter", "inch", "centimeter", "gallon", "liter"]

        for conv in conversions:
            if "amount" not in conv or "from_unit" not in conv or "to_units" not in conv:
                results.append({"error": "Uh oh! Each conversion must include 'amount', 'from_unit', and 'to_units'."})
                continue

            amount = conv["amount"]
            from_unit = conv["from_unit"]
            to_units = conv["to_units"]

            if from_unit not in supported_units:
                results.append({"error": f"Unsupported from_unit: {from_unit}"})
                continue

            invalid_to_units = [unit for unit in to_units if unit not in supported_units]
            if invalid_to_units:
                results.append({"error": f"Unsupported to_units: {', '.join(invalid_to_units)}"})
                continue

            conversion_result = {from_unit: amount}

            # sooo many units to program ughhh nooo TODO: finish this
            # wooo finished it

            if from_unit == "miles":
                if "kilometers" in to_units:
                    conversion_result["kilometers"] = amount * 1.60934
                if "feet" in to_units:
                    conversion_result["feet"] = amount * 5280
                if "meter" in to_units:
                    conversion_result["meter"] = amount * 1609.34
                results.append(conversion_result)

            elif from_unit == "kilometers":
                if "miles" in to_units:
                    conversion_result["miles"] = amount * 0.621371
                if "feet" in to_units:
                    conversion_result["feet"] = amount * 3280.84
                if "meter" in to_units:
                    conversion_result["meter"] = amount * 1000
                results.append(conversion_result)

            elif from_unit == "feet":
                if "kilometers" in to_units:
                    conversion_result["kilometers"] = amount * 0.0003048
                if "miles" in to_units:
                    conversion_result["miles"] = amount * 0.000189394
                if "meter" in to_units:
                    conversion_result["meter"] = amount * 0.3048
                results.append(conversion_result)

            elif from_unit == "meter":
                if "kilometers" in to_units:
                    conversion_result["kilometers"] = amount * 0.001
                if "miles" in to_units:
                    conversion_result["miles"] = amount * 0.000621371
                if "feet" in to_units:
                    conversion_result["feet"] = amount * 3.28084
                results.append(conversion_result)

            elif from_unit == "gallon":
                if "liter" in to_units:
                    conversion_result["liter"] = amount * 3.78541
                results.append(conversion_result)

            elif from_unit == "liter":
                if "gallon" in to_units:
                    conversion_result["gallon"] = amount * 0.264172
                results.append(conversion_result)

            elif from_unit == "inch":
                if "centimeter" in to_units:
                    conversion_result["centimeter"] = amount * 2.54
                results.append(conversion_result)

            elif from_unit == "centimeter":
                if "inch" in to_units:
                    conversion_result["inch"] = amount / 2.54
                results.append(conversion_result)

        return jsonify({"results": results}), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/')
def docs():
    return jsonify({"error": "not found", "for docs:": "/docs"}), 404

@app.route('/docs')
def docs2():
    return redirect("https://github.com/j4y-boi/UnitConvAPI/blob/main/README.md", code=302)

@app.route('/repo')
def repo():
    return redirect("https://github.com/j4y-boi/UnitConvAPI/", code=302)

@app.errorhandler(404)
def not_found():
    return jsonify({"error": "not found", "for docs:": "/docs"}), 404

if __name__ == '__main__':
    app.run()

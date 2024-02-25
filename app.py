from flask import Flask,request,jsonify
import requests
app = Flask(__name__)

@app.route('/',methods=['POST'])
def index():
    data=request.get_json()
    source_curr=data["queryResult"]["parameters"]["unit-currency"]["currency"]
    sc_value=data["queryResult"]["parameters"]["unit-currency"]["amount"]
    destination_curr=data["queryResult"]["parameters"]["currency-name"]
    print(source_curr)
    print(destination_curr)
    print(sc_value)
    factor = fetching_factor(source_curr, destination_curr)
    final_amount=sc_value * factor
    final_amount=round(final_amount,3)
    print("Final amount in INR is : " + str(final_amount))
    response={
        'fulfillmentText': '{} {} is {} {}'.format(sc_value,source_curr,final_amount,destination_curr)
    }
    return jsonify(response)


def fetching_factor(source,destination):
    url="https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_M0lT2R3x4BvYwcz9Y9K0fzbHcf5pcKdcKeiPNm3t&currencies={}&base_currency={}".format(destination,source)
    response=requests.get(url)
    response=response.json()
    print(response)
    return response['data']['{}'.format(destination)]


if __name__ == "__main__":
    app.run(debug=True)
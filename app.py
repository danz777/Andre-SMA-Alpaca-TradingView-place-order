import alpaca_trade_api as tradeapi
import time

from chalice import Chalice

app = Chalice(app_name='dre-trade')

key = "api-key"
sec = "secret"

#API endpoint URL
url = "https://api.alpaca.markets"

#api_version v2 refers to the version that we'll use
#very important for the documentation
api = tradeapi.REST(key, sec, url, api_version='v2')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/dretrade', methods=['POST'])
def dretrade():
    request = app.current_request
    webhook_message = request.json_body
    
    data = api.submit_order(symbol=webhook_message['ticker'],
                            qty="1",
                            side=webhook_message['side'],
                            type="market",
                            time_in_force="gtc")
    
    return {
        'webhook_message': webhook_message
    }

import requests
from time import sleep


class Jadi:

    def btc_price(self):
        response = requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy')
        j = response.json()
        print(j['data']['amount'])

    def send_sms(self):
        url = "https://rest.nexmo.com/sms/json"
        querystring = {"api_key": "6f612444", "api_secret": "w3Zo2sMhibUjx4DA", "to": "16044429075",
                       "from": "15878012283", "text": "%22Hello%20maximooz%20%22"}
        headers = {
            'Cache-Control': "no-cache",
            'Postman-Token': "b2af3a4b-64ce-2b2b-6e73-0431528e73f0"
        }
        response = requests.request("POST", url, headers=headers, params=querystring)
        print(response.text)

    def stock_price(self,stock_symbol):

         send_request = requests.get('https://api.iextrading.com/1.0/stock/{}/price'.format(stock_symbol))
         requests_json = send_request.json()
         #print requests_json
         #current_price = float((requests_json['Global Quote']['05. price']))
         print (requests_json)



    def statu(self):
        status = requests.get("w")

    def alert(self,stock):

        current_price = Jadi.stock_price(self,stock)

        while current_price <= 188:
            #Jadi.send_sms(self)
            print("sms")
            current_price = Jadi.stock_price(self,stock)
            print(current_price)
            sleep(10)

def main():
    call = Jadi()
    #call.btc_price()
    call.stock_price('fb')
    #call.alert('fb')


if __name__ == '__main__': main()


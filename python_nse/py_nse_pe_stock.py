# Import requests for calling stock api url
import requests
class StockGet:
    def __init__(self):
        # API URL
        self.api_url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/getPEDetails.jsp"
        # Variable to store json data
        self.stock_data = ''
        # Variable to store URL with stock symbol
        self.api_url_sym = ''
    def get_stock(self, symbol):
        uri_params = {"symbol": symbol}
        # Request stock PE api
        req = requests.get(self.api_url, params=uri_params)
        self.api_url_sym = req.url
        req_dict = req.json()
        return req_dict
    def get_details(self, symbol, stock_key):
        self.stock_data = self.get_stock(symbol)
        for key in self.stock_data:
            if key == stock_key:
                return(self.stock_data[key])
        
if __name__ == "__main__":
    stock_obj = StockGet()
    # List all stock to track in stock_list file
    # add each stock in new line
    with open('stock_list.txt', 'r') as file:
        for line in file:
            stock_name = line.replace('\n', '')
            pe = stock_obj.get_details(stock_name, 'PE')
            #print(f'Requested URL : {stock_obj.api_url_sym}')
            print(f'STOCK NAME : {stock_name}')
            print(f'Response : {stock_obj.stock_data}')
            #print(f'PE Data: {pe}')
            print("PE Data:",pe)
            # Class Variable
            #print(stock_obj.stock)

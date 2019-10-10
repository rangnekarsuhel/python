# Import requests for calling stock api url
import requests
class StockGet:
    def __init__(self):
        # API URL
        self.api_url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp"
        self.api_referer = "https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=ZEEL"
        #self.api_url="https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/ajaxGetQuoteJSON.jsp?symbol=ZEEL&series=EQ"
        # Variable to store json data
        self.stock_data = ''
        # Variable to store URL with stock symbol
        self.api_url_sym = ''
        self.stock_date = ''
    def get_stock(self, symbol):
        #?symbol=ZEEL&series=EQ
        uri_params = {"symbol": symbol, "series": 'EQ'}
        try:
            # Request live stock from nse api
            req = requests.get(self.api_url, params=uri_params, headers={'referer': self.api_referer})
            if req.status_code == 200:
                self.api_url_sym = req.url
                print(req.url)
                req_dict = req.json()
                return req_dict
            else:
                return False
        except Exception as e:
            print(e)
    def get_details(self, symbol, stock_key):
        self.stock_data = self.get_stock(symbol)
        self.stock_date = self.stock_data['tradedDate']
        for key in self.stock_data['data'][0]:
            if key == stock_key:
                return(self.stock_data['data'][0][key])
        
if __name__ == "__main__":
    # Create object for Class
    stock_obj = StockGet()
    # import notification module for win
    from win10toast import ToastNotifier
    toaster = ToastNotifier()
    # List all stock to track in stock_list file
    # add each stock in new line
    with open('stock_list.txt', 'r') as file:
        for line in file:
            stock_name = line.replace('\n', '').split(':')
            last_price = stock_obj.get_details(stock_name[0], 'lastPrice')
            #print(f'Requested URL : {stock_obj.api_url_sym}')
            notify = f'STOCK NAME : {stock_name}\n'
            notify += f'STOCK Date : {stock_obj.stock_date}\n'
            notify += f'Last Price: {last_price}\n'
            notify += f'My Price: {stock_name[1]}\n'
            toaster.show_toast("Stock notification",notify,duration=5)
            #print(popup)
            # Class Variable
            #print(stock_obj.stock)

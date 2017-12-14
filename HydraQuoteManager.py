from QuoteManager import *
from HapiInformationServer import HAPIInformationServer


class HydraQuoteManager(QuoteManager):
    """
    adaptor class to connect to hydra
    """
    def __init__(self, port=10001, auto_start=True):
        super(HydraQuoteManager, self).__init__()
        self.iserver = 0
        if auto_start:
            self.open_socket(port)

    def start_quote_stream(self, symbol):
        """
        :param symbol:
        :return: the quote object
        """
        q = self.iserver.start_quote(symbol)
        return q

    def stop_quote_stream(self, symbol):
        self.iserver.stop_quote(symbol)

    def open_socket(self, port):
        self.iserver = HAPIInformationServer(port)

    def close_socket(self):
        self.iserver.close_is_socket()
        self.iserver = 0

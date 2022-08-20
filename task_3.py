import requests
from pprint import pprint
from datetime import datetime, timedelta


class StackOverflowAPIService:

    BASE_URL = 'https://api.stackexchange.com/2.3'
    QUESTIONS = '/questions'

    def __init__(self, period=2, order='desc'):
        self.period = period
        self.order = order
        self.sort = "activity"
        self.site = "stackoverflow"

    @property
    def period(self):
        return self._period

    @period.setter
    def period(self, period):
        now = datetime.now()
        self.todate = int(datetime.timestamp(now))
        self.fromdate = int(datetime.timestamp(now - timedelta(days=period)))
        self._period = period

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, order):
        if order in ('desc', 'ask'):
            self._order = order

    def _get_params(self):
        params = {
            "fromdate": self.fromdate,
            "todate": self.todate,
            "order": self.order,
            "sort": self.sort,
            "site": self.site
        }
        return params

    def get_questions_by_tag(self, tag):
        url = self.BASE_URL + self.QUESTIONS
        params = self._get_params()
        params['tagged'] = tag
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()


if __name__ == '__main__':
    st_overflow = StackOverflowAPIService()
    pprint(st_overflow.get_questions_by_tag('python'))

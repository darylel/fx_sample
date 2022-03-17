'''
Get foreign exchange rates Exchangerate.host
'''
import requests

def latest_rates(url, base):
    '''
    Get the latest rates

    :param url: string of the API's URL
    :param base: string of base currency to be used by API
    '''
    url = url + 'latest?' + base
    response = requests.get(url)
    data = response.json()

    print(data)

def historical_rate(url, base, date):
    '''
    Get rates for a previous day

    :param url: string of the API's URL
    :param base: string of base currency to be used by API
    :param date: string in format YYYY-MM-DD
    '''
    url = url + date + '?' + base
    response = requests.get(url)
    data = response.json()

    print(data)

def period_rates(url, base, start_date, end_date):
    '''
    Get rates from a timeframe no greater than a year

    :param url: string of the API's URL
    :param base: string of base currency to be used by API
    :param start_date: string in format YYYY-MM-DD
    :param end_date: string in format YYYY-MM-DD
    '''
    url =  url + 'timeseries?start_date=' + start_date + '&end_date=' + end_date + '?' + base
    response = requests.get(url)
    data = response.json()

    print(data)

def rate_fluctuation(url, base, start_date, end_date):
    '''
    Shows exchange rate fluctuation

    :param url: string of the API's URL
    :param base: string of base currency to be used by API
    :param start_date: string in format YYYY-MM-DD
    :param end_date: string in format YYYY-MM-DD
    '''
    url =  url + 'fluctuation?start_date=' + start_date + '&end_date=' + end_date + '?' + base
    response = requests.get(url)
    data = response.json()

    print(data)

def available_currencies(url):
    '''
    Return all supported currencies

    :param url: string of the API's URL
    '''
    url = url + 'symbols'
    response = requests.get(url)
    data = response.json()

    print(data)

def main():
    '''
    Produce exchange rate data
    '''
    url = 'https://api.exchangerate.host/'
    base = 'base=USD'

    #latest_rates(url, base)
    #historical_rate(url, base, '2021-04-04')
    #period_rates(url, base, '2021-04-01','2021-04-04')
    rate_fluctuation(url, base, '2021-04-01','2021-04-04')
    #available_currencies(url)

if __name__ == "__main__":
    main()

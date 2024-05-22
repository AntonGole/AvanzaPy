SECRET = 'your_totp_secret_here'

SESSION_FILE = 'session/session.json'

STOCKS_FILE = 'data/stocks.json'

SESSION_EXPIRY_TIME = 3600

BASE_URL = 'https://www.avanza.se'

PERSISTENCE_COOKIE = 'AZAPERSISTENCE=YOUR_PERSISTENCE_COOKIE'

HEADERS = {
    "Sec-Ch-Ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Content-Type": "application/json;charset=UTF-8",
    "Accept": "application/json, text/plain, */*",
    "Baggage": "sentry-environment=prod,sentry-release=2024-17,sentry-public_key=a17cf8616ceb4265a0ebc85365906ee1",
    "Sentry-Trace": "881b291139764eae8632b6d89d6586c6-9b2b743e7e6f542a",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Origin": "https://www.avanza.se",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.avanza.se/start",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

FETCH_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.118 Safari/537.36",
    "Sec-Ch-Ua": "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.avanza.se/aktier/lista.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=1, i"
}

FETCH_PARAMS = {
    "1715857661295": "",
    "widgets.marketCapitalInSek.filter.lower": "",
    "widgets.marketCapitalInSek.filter.upper": "",
    "widgets.marketCapitalInSek.active": "false",
    "widgets.stockLists.filter.list[0]": "SE.LargeCap.SE",
    "widgets.stockLists.filter.list[1]": "SE.Inofficiella",
    "widgets.stockLists.filter.list[2]": "SE.MidCap.SE",
    "widgets.stockLists.filter.list[3]": "SE.NGM+PepMarket",
    "widgets.stockLists.filter.list[4]": "SE.Nordic+SME+Sweden",
    "widgets.stockLists.filter.list[5]": "SE.SPAC.SE",
    "widgets.stockLists.filter.list[6]": "SE.SmallCap.SE",
    "widgets.stockLists.filter.list[7]": "SE.Xterna+listan",
    "widgets.stockLists.filter.list[8]": "SE.FNSE",
    "widgets.stockLists.filter.list[9]": "SE.XNGM",
    "widgets.stockLists.filter.list[10]": "SE.XSAT",
    "widgets.stockLists.active": "false",
    "widgets.numberOfOwners.filter.lower": "",
    "widgets.numberOfOwners.filter.upper": "",
    "widgets.numberOfOwners.active": "false",
    "parameters.startIndex": "0",
    "parameters.maxResults": "100",
    "parameters.selectedFields[0]": "LATEST",
    "parameters.selectedFields[1]": "DEVELOPMENT_TODAY",
    "parameters.selectedFields[2]": "DEVELOPMENT_ONE_YEAR",
    "parameters.selectedFields[3]": "MARKET_CAPITAL_IN_SEK",
    "parameters.selectedFields[4]": "PRICE_PER_EARNINGS",
    "parameters.selectedFields[5]": "DIRECT_YIELD",
    "parameters.selectedFields[6]": "NBR_OF_OWNERS",
    "parameters.selectedFields[7]": "LIST",
    "parameters.sortOrder": "ASCENDING"
}
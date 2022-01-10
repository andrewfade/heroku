import requests
from tradingview_ta import TA_Handler, Interval
import.time

# %%
def telegram_bot(bot_message):
    
    bot_token = '5031596943:AAGxNNMImdPjlEXbn5lFMQFzaddyA_0Amzc'
    bot_chatID = '1826283117'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

# %%
def RSI(i) :
    coin = TA_Handler(
        symbol= i,
        screener = "turkey",
        exchange= "BIST",
        interval=Interval.INTERVAL_1_DAY
    )
    data = coin.get_analysis().indicators
    return data["RSI"]

# %%
def RSIH(i) :
    coin = TA_Handler(
        symbol= i,
        screener = "turkey",
        exchange= "BIST",
        interval=Interval.INTERVAL_1_HOUR
    )
    data = coin.get_analysis().indicators
    return data["RSI"]

# %%
elimdekiler = ["ADESE", "CEMTS", "ECILC", "KONTR",  "KRDMA", "TMPOL", "TTRAK", "VESBE", "VESTL", "YATAS"]
hisseler = ['ACSEL', 'ADEL', 'AEFES', 'AGHOL', 'AKCNS', 'AKGRT', 'AKMGY', 'AKSA', 'ALARK', 'ALCAR', 'ALGYO',
            'ALKA', 'ALKIM', 'ANELE', 'ANHYT', 'ANSGR', 'ARCLK', 'ARENA', 'ARZUM', 'ASELS', 'AGESA', 'AYES', 
            'AYGAZ', 'BAKAB', 'BASCM', 'BFREN', 'BIMAS', 'BIZIM', 'BRISA', 'BRSAN', 'BRYAT', 'BUCIM', 'CCOLA', 
            'CELHA', 'CEMTS', 'CIMSA', 'CLEBI', 'CUSAN', 'DESPC', 'DITAS', 'DMSAS', 'DNISI', 'DOAS', 'DOCO', 
            'ECILC', 'ECZYT', 'EGEEN', 'EGGUB', 'EGPRO', 'EGSER', 'EKGYO', 'ENJSA', 'ENKAI', 'ERBOS', 'EREGL', 
            'ETYAT', 'EUKYO', 'EUYO', 'FMIZP', 'FROTO', 'GEDIK', 'GENTS', 'GOLTS', 'GOODY', 'GRNYO', 'HEKTS', 
            'INDES', 'ISDMR', 'ISGYO', 'ISMEN', 'ISYAT', 'JANTS', 'KARTN', 'KCHOL', 'KFEIN', 'KLMSN', 'KONTR',
            'KONYA', 'KORDS', 'KRVGD', 'KSTUR', 'LKMNH', 'MAVI', 'MTRKS', 'MTRYO', 'NUHCM', 'OTKAR', 'OYAKC', 
            'OYAYO', 'OZRDN', 'PAGYO', 'PAPIL', 'PETKM', 'PETUN', 'PNSUT', 'POLHO', 'POLTK', 'PRKAB', 'PSDTC', 
            'SAHOL', 'SANKO', 'SARKY', 'SELEC', 'SISE', 'SODSN', 'SUMAS', 'TATGD', 'TAVHL', 'TCELL', 'TKFEN', 
            'TLMAN', 'TOASO', 'TTKOM', 'TTRAK', 'TUPRS', 'TURSG', 'ULKER', 'ULUSE', 'VERTU', 'VERUS', 'VESBE', 
            'YAPRK', 'YGGYO', 'YKSLN', 'YONGA', 'YUNS']
print("hello trader")
# %%
telegram_bot("bist started")
counter = 0
while counter < 33:
    for i in hisseler:
        rsi = RSI(i)
        rsih = RSIH(i)
        
        if rsi < 30:
            telegram_bot(f"{i}-{rsi}")
        if rsih <25 :
            telegram_bot(f"{i} saatlik {rsih}")
        if counter == 32 and rsi < 40:
            telegram_bot(f"{i} gün sonu {rsi}")
        if counter == 32 and rsi > 70:
            telegram_bot("****************")
            telegram_bot(f"{i} OB {rsi}")
    for i in elimdekiler:
        rsi = RSI(i)
        if rsi > 70:
            telegram_bot(f"SAT\nSAT\nSAT\n{i}-{rsi}")
    counter += 1
    time.sleep(900)

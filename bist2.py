import requests
from tradingview_ta import TA_Handler, Interval
import time.

# %%
def telegram_bot(bot_message):
    
    bot_token = '5031596943:AAGxNNMImdPjlEXbn5lFMQFzaddyA_0Amzc'
    bot_chatID = '1826283117'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

# %%
def RSID(i) :
    coin = TA_Handler(
        symbol= i,
        screener = "turkey",
        exchange= "BIST",
        interval=Interval.INTERVAL_1_DAY
    )
    data = coin.get_analysis().indicators
    return data["RSI"], data["close"]

# %%
def RSI2H(i) :
    coin = TA_Handler(
        symbol= i,
        screener = "turkey",
        exchange= "BIST",
        interval=Interval.INTERVAL_2_HOURS
    )
    data = coin.get_analysis().indicators
    return data["RSI"]

def RSI30M(i) :
    coin = TA_Handler(
        symbol= i,
        screener = "turkey",
        exchange= "BIST",
        interval=Interval.INTERVAL_30_MINUTES
    )
    data = coin.get_analysis().indicators
    return data["RSI"]
# %%
elimdekiler = ["ADESE", "CEMTS", "ECILC", "EREGL",  "KRDMA", "TMPOL", "TTRAK", "VESBE", "VESTL", "YATAS", "AKCNS","BIMAS"]
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
            'TLMAN', 'TOASO', 'TTKOM', 'TTRAK', 'TUPRS', 'TURSG', 'ULKER', 'ULUSE', 'VERTU', 'VERUS', 'VESBE', 'VESTL',
            'YAPRK', 'YGGYO', 'YKSLN', 'YONGA', 'YUNSA']
print("hello trader")
# %%
telegram_bot("bist started")
counter = 0
while counter < 33:
    try:
        for i in hisseler:
            #print(i)
            rsid, price = RSID(i)
            rsi2h = RSI2H(i)
            rsi30m = RSI30M(i)
            mtf_rsi = rsi30m + rsi2h + rsid
            if rsid < 30:
                telegram_bot(f"{i} - günlük - {rsid} - price {price}")
            if rsi2h <25 :
                telegram_bot(f"{i} - 2 saatlik - {rsi2h} - price {price}")
            if rsi30m <20 :
                telegram_bot(f"{i} - 30 dakikalık - {rsi30m} - price {price}")
            if mtf_rsi < 90 :
                telegram_bot(f"{i} - MTF - {mtf_rsi} - price {price}")
            if counter == 32 and mtf_rsi < 110:
                telegram_bot(f"{i} gün sonu {mtf_rsi} - price {price}")
            # if counter == 32 and rsi > 70:
            #     telegram_bot("****************")
            #     telegram_bot(f"{i} OB {rsi}")
        for i in elimdekiler:
            #print(i)
            rsi, price = RSID(i)
            #print("elimdekiler")
            if rsi > 70:
                telegram_bot(f"SAT\nSAT\nSAT\n{i}-{rsi} - price {price}")
        counter += 1
        time.sleep(900)
    except Exception as e:
        telegram_bot(f"hata - {i} - {e}")

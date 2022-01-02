import requests
import time
from tradingview_ta import TA_Handler, Interval

# %%
def telegram_bot(bot_message):
    
    bot_token = '5062338559:AAGKbMgOxfoL4h7Xbub5QqctNKJh25EvBZA'
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
hisseler = ['ACSEL', 'ADEL', 'AEFES', 'AGHOL', 'AKCNS', 'AKGRT', 'AKMGY', 'AKSA', 'AKSGY', 'ALARK', 'ALCAR', 'ALGYO', 'ALKA', 'ALKIM', 'ANELE', 'ANHYT', 'ANSGR', 'ARCLK', 'ARENA', 'ASELS', 'AGESA', 'AYES', 'AYGAZ', 'BAGFS', 'BASCM', 'BFREN', 'BIMAS', 'BIZIM', 'BLCYT', 'BOSSA', 'BRISA', 'BRSAN', 'BRYAT', 'BSOKE', 'BTCIM', 'BUCIM', 'CCOLA', 'CEMTS', 'CIMSA', 'CLEBI', 'CRDFA', 'CUSAN', 'DESPC', 'DGATE', 'DOAS', 'DOCO', 'ECILC', 'ECZYT', 'EGEEN', 'EGGUB', 'EGPRO', 'EGSER', 'EKGYO', 'ENJSA', 'ENKAI', 'ERBOS', 'EREGL', 'ETYAT', 'EUKYO', 'EUYO', 'FMIZP', 'FROTO', 'GENTS', 'GOODY', 'GRNYO', 'HDFGS', 'HEKTS', 'HLGYO', 'INDES', 'ISDMR', 'ISGYO', 'ISMEN', 'ISYAT', 'JANTS', 'KARTN', 'KCHOL', 'KFEIN', 'KLMSN', 'KONYA', 'KORDS', 'KSTUR', 'KUTPO', 'LKMNH', 'MTRYO', 'NUHCM', 'ORGE', 'OTKAR', 'OYAKC', 'OYAYO', 'OZRDN', 'PAGYO', 'PETKM', 'PETUN', 'PNSUT', 'POLHO', 'POLTK', 'PRKAB', 'PSDTC', 'SAFKR', 'SAHOL', 'SANKO', 'SARKY', 'SASA', 'SELEC', 'SISE', 'SNGYO', 'SODSN', 'SRVGY', 'SUMAS', 'TAVHL', 'TCELL', 'TKFEN', 'TLMAN', 'TOASO', 'TRGYO', 'TTKOM', 'TTRAK', 'TUPRS', 'ULKER', 'ULUSE', 'VERUS', 'VESBE', 'YBTAS', 'YGGYO', 'YGYO', 'YONGA', 'YUNSA']
print("hello trader")
# %%
telegram_bot("bist started")
counter = 0
while counter < 32:
    for i in hisseler:
        rsi = RSI(i)
        rsih = RSIH(i)
        if rsi < 30:
            telegram_bot(f"{i}-{rsi}")
        if rsih <25 :
            telegram_bot(f"{i} saatlik {rsih}")
        if counter == 31 and rsi < 40:
            telegram_bot(f"{i} gün sonu {rsi}")
        if counter == 31 and rsi > 70:
            telegram_bot("****************")
            telegram_bot(f"{i} OB {rsi}")
    
    time.sleep(900)   
    counter += 1 
    


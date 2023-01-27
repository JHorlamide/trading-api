from iqoptionapi.api import IQOptionAPI

iq_option = IQOptionAPI("olamidejubril68@gmail.com", "#Obalola21#", "#Obalola21#")
connect_success, connection_failed = iq_option.connect()  # connect to iqoption

if connect_success:
  print("Connected successfully to IQoption")
  
  Money = 20
  ACTIVES = "EURUSD"
  ACTION = "call"
  expirations_mode = 2

  buy_success, trade_id = iq_option.buy(Money, ACTIVES, ACTION, expirations_mode)

  if buy_success:
    print("Trade ID: ", trade_id)
  else :
    print("Buy Failed")

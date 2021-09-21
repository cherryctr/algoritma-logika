beratTelur = 5
hargaTelur = 26000
uangTransport = 3500
uangSedia = 200000

telurFix = (hargaTelur * beratTelur)
butuhTransport = (uangTransport * 2)
# 2 diatas adalah ongkos pulang pergi
sisaUang = (uangSedia - telurFix - butuhTransport)
print("Uang ibu yang tersisa adalah : " , sisaUang)
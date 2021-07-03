margin=float(input("Account balance: "))
percent=float(input("% risk: "))/100
pipstopl=float(input("pip stop loss: "))

risk=margin*percent
size=(risk/pipstopl)*10000
perpip=risk/pipstopl
print("-------------------------------")
print("Risk: "+str(risk)+"$")
print("value per pip: "+str(perpip)+"$")
print("Units: "+str(int(size)))
print("lot size: "+str(int(size)/100000))#100000
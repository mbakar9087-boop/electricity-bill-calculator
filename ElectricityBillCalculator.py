print("===ELECTRICITY BILL CALCULATOR===")
unt=int(input("Enter Units Consumed:"))
if (unt<=200):
    sts="Protected"
else:
    sts="Not Protected"
tvc=700
if unt <= 100:
    unt_r = 22.44
elif unt <= 200:
    unt_r = 28.91
elif unt <= 300:
    unt_r = 33.10
elif unt <= 400:
    unt_r = 36.46
elif unt <= 500:
    unt_r = 38.91
elif unt <= 600:
    unt_r = 40.21
elif unt <= 700:
    unt_r = 41.91
else:
    unt_r = 47.20
bill=unt*unt_r
gst=(bill*17)/100
sur_crg=tvc
T_bill=bill+gst+sur_crg
print("\n\n======Electricity Bill======")
print("Energy Consumed in kWh =",unt)
print("Rate per kWh =",unt_r)
print("Energy Charges =",bill)
print("gst 17% =",gst)
print("PTV fee=",sur_crg)
print("===============================")
print("Status:",sts)
print("===============================")
print("Total Bill=",T_bill)
print("===============================")
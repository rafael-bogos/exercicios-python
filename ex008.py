m = float(input('\033[4;31;40mDigite o numero a ser convertido:\033[m '))
mm = m*1000
cm = m*100
dm = m*10
dam = m/10
hm = m/100
km = m/1000
print(f' {m}m tem: \n mm: {mm:.0f} \n cm: {cm:.0f} \n dm: {dm:.0f} \n dam: {dam} \n hm: {hm} \n km: {km}')
# 1 metro tem 100 centimetros e 1 centimetro tem 10mm
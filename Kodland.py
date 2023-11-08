import random

sifre1 = "TıjdksajEasdAosadksMkskdasjFaksdOajRdajTskjRasjEsdkjSS"
sifre2 = "1234487123023125"
sifre3 = "*-.,!'^^=+=)!(%_!)"
uzunluk = int(input("Parolanız ne kadar uzun olsun?: "))

ba = ""

sayi = 0


for i in range(uzunluk):
    ba += random.choice(sifre1)
    sayi = sayi + 1
for i in range(uzunluk):
    ba += random.choice(sifre2)
    sayi = sayi + 1
for i in range(uzunluk):
    ba += random.choice(sifre3)
    sayi = sayi + 1

print(ba)
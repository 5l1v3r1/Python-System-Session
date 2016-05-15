#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

def sistemi_kapat():
	os.system("poweroff")
	
def sistemi_yeniden_baslat():
	os.system("reboot")

def sistemin_sifresini_degistir():
	os.system("passwd")

system_ico = """
#########################################################
#       PYTHON - SYSTEM SESSION - GH0ST S0FTWARE        #
######################################################### 
#                       CONTACT                         #
#########################################################
#              DEVELOPER : İSMAİL TAŞDELEN              #                       
#           GMAIL : pentestdatabase@gmail.com           #
# Linkedin : https://www.linkedin.com/in/ismailtasdelen #
#           Whatsapp : + 90 534 295 94 31               #
#########################################################
"""

islemler_ico = """
(1) Bilgisiyarı Kapat
(2) Bilgisiyarı Yeniden Başlat
(3) Bilgisiyar Oturum Şifresini Değiştir
"""

print system_ico

print islemler_ico

star = "*******************************************";

print star

islem = input("Yapılcak işlem numarasını giriniz : ")

print star

if islem == 1:
	mesaj = "Sistem kapatılıyor... %100";
	print mesaj
	sistemi_kapat()	

elif islem == 2:
	mesaj = "Sistem yeniden başlatılıyor... %100";
	print mesaj
	sistemi_yeniden_baslat()

elif islem == 3:
	mesaj = "Kullanıcı şifrenizi değiştirmek için iki kere yeni şifrenizi giriş yapmalısınız. ";
	print mesaj
	sistemin_sifresini_degistir()	

else:
	if islem != 1 and 2 and 3:
		print star
		hata_mesaji = "İşlem numaranızı yanlış girdiniz."
		print hata_mesaji
		print star

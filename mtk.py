import os
import sys

os.system ('clear')
os.system ('figlet MTK | lolcat')
print "========================"
print "AutHor : danGaming13114"
print "YouTube: daniGeming13114"
print "========================"
print
print "[+] PILIH MENU  [+]"
print
print "[1] kurangi"
print "[2] tambah"
print "[3] bagi"
print
pilih = raw_input('[+] pilih nomor : ')
if pilih == "1":
        print
        angka_1 = input('angka 1 : ')
        angka_2 = input('angka 2 : ')
        total = angka_1 - angka_2
        print
        print 'hasil : ', total
        print
elif pilih == "2":
        print
        angka_1 = input('angka 1 : ')
        angka_2 = input('angka 2 : ')
        total = angka_1 + angka_2
        print
        print 'hasil : ', total
        print
elif pilih == "3":
        print
        angka_1 = input('angka 1 : ')
        angka_2 = input('angka 2 : ')
        total = angka_1 / angka_2
        print
        print 'hasil : ', total
        print

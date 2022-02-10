import gspread

from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheets = client.open("Informationen").sheet1


import smtplib
import time
from info import password

mail= smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()  # mail serverina kendimizi tanitiyoruz
mail.starttls()  # girecegimiz mail adresini gizliyor
mail.login("ulutepenesrin@gmail.com", password)

counter = 9

while  counter <= sheets.row_count :
    
    soyad = sheets.cell(counter+1,2).value
    ad = sheets.cell(counter+1,3).value
    mail_adress = sheets.cell(counter+1,4).value

    content=f"MERHABA {ad} {soyad}, AILEMIZE HOSGELDINIZ. BU FORMU DOLDURAN {counter}. KISI OLDUNUZ. MAIL ADRESINIZ {mail_adress} SISTEMIMIZE EKLENMISTIR.BU MESAJ PYTHONLA GONDERILMISTIR.TESEKKUR EDERIZ."
    
    mail.sendmail("ulutepenesrin@gmail.com", mail_adress, content.encode("utf-8"))
    print(f"{ad} {soyad} kisisine mesaj basariyla iletilmistir.")  
    counter += 1
    time.sleep(10)

mail.close()
sheets.close()
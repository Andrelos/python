#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib 
     
from email.MIMEText import MIMEText 
    
emisor = "andrezblanco@gmail.com" 
receptor = "andrezblanco@gmail.com" 
    
# Configuracion del mail 
mensaje = MIMEText("Este correo ha sido enviado desde Python") 
mensaje['From']=emisor 
mensaje['To']=receptor 
mensaje['Subject']="Mi segundo correo desde Python" 
    
# Nos conectamos al servidor SMTP de Gmail 
serverSMTP = smtplib.SMTP('smtp.gmail.com',587) 
serverSMTP.ehlo() 
serverSMTP.starttls() 
serverSMTP.ehlo() 
serverSMTP.login(emisor,"cotonr31n4d0") 
    
# Enviamos el mensaje 
serverSMTP.sendmail(emisor,receptor,mensaje.as_string()) 
    
# Cerramos la conexion 
serverSMTP.close()

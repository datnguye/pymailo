from pymailo import smtp
smtp.send(recipient=['datnguyen.it09@gmail.com','ulalahecuca@gmail.com'],subject='Hello World!',body='Why, oh  why?')

from pymailo import sendgridapi
sendgridapi.send(recipient='datnguyen.it09@gmail.com;ulalahecuca@gmail.com',subject='Hello World!',body='Why, oh  why?')
Imapsync
========

Wrapper en python que hace uso del imapsync escrito en perl. 
Algunas de las cosas que se pueden hacer con el son las siguientes:

- Permite sincronizar una lista de cuentas de correo almacenadas en el archivo `userlist`
- Sincroniza correctamente cuentas de gmail.
- El script funciona principalmente para sincronizar cuentas de GMAIL y Google APPS.
- De momento, tanto el servidor de origen como de destino, deben de soportar el metodo de autenticación LOGIN.

uso:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com

Proyecto basado en el script de [Gustavo Díaz](http://artistic.lnxteam.org/?p=231)

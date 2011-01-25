Imapsync
========

Wrapper en python que hace uso del imapsync escrito en perl. 
Algunas de las cosas que se pueden hacer con el son las siguientes:

- Permite sincronizar una lista de cuentas de correo almacenadas en el archivo `userlist`
- Sincroniza correctamente cuentas de gmail.
- El script funciona principalmente para sincronizar cuentas de GMAIL y Google APPS.
- De momento, tanto el servidor de origen como de destino, deben de soportar el metodo de autenticación LOGIN.
- Si no se especifican los servidores, por defecto toma los de google mail.googlemail.com.
- Agregada la posibilidad de seleccionar las carpetas que se desean sincronizar.

uso si solo te interesa sincronizar el inbox:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com
    
en caso que desees sincronizar las carpetas enviados, borradores, basura y spam:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com -sa
    
En caso que desees sincronizar solo la carpeta enviados:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com -sm
    
En caso de que desees sincronizar solo la carpeta spam:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com -sp
    
En caso de que desees sincronizar solo la carpeta borradores:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com -d
    
En caso de que desees sincronizar la papelera o basura:
    python imapsync.py -h1 mail.googlemail.com -h2 mail.googlemail.com -t

Proyecto basado en el script de [Gustavo Díaz](http://artistic.lnxteam.org/?p=231)

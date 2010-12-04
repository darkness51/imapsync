
#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Script para poder migrar de manera automatizada las cuentas de email con imapsync ##

import os
import sys
from subprocess import Popen, PIPE
from time import strftime

# Para genera un log de la ejecucción de imapsync
log = True

# Comprobamos la existencia de la lista de usuarios a migrar
# Nota: esta lista debe ser un usuario por línea. Ej: email@dominio.com MiContraseña
try:
    userList = open("userlist", "r")
except:
    print 'El archivo con la lista de Usuarios no existe.'
    sys.exit()

# Comprobamos si la aplicación imapsync está instalado
try:
    os.path.exists("/usr/bin/imapsync")
except:
    print 'Necesita instalar la aplicación "imapsync".'
    sys.exit()

# Path del ejecutable de imapsync
command = "/usr/bin/imapsync"
# Argumentos de imapsync
args = " --host1 %s --user1 %s --password1 %s --host2 %s --user2 %s --password2 %s --subscribed --subscribe"
# IP servidor IMAP viejo
host1 = "192.168.15.1"
# IP servidor IMAP nuevo
host2 = "192.168.15.5"

# Leemos el archivo de la lista de usuarios y ejecutamos imapsync por cada uno de ellos
for line in userList.readlines():
    imapsync = Popen(command + args % (host1, line.split(" ")[0], line.split(" ")[1].rstrip('\n'),
        host2, line.split(" ")[0], line.split(" ")[1].rstrip('\n')), stdout=PIPE, shell=True)
    print '%s --- Sincronizando la cuenta "%s"...' % (strftime("%d-%m-%Y %H:%M:%S"), (line.split(" ")[0]))

    # Si el log está habilitado, lo escribimos en un archivo
    if log:
        stdout = imapsync.stdout.read()
        logFile = open("imapsync.log", "a")
        logFile.write('%s --- Sincronizando la cuenta "%s"... \n\n %s \n\n' % (strftime("%d-%m-%Y %H:%M:%S"),
            (line.split(" ")[0]), stdout))
        logFile.close()

    # De lo contrario, lo mostramos por pantalla
    else:
        print imapsync.stdout.read()

# Cerramos el archivo
userList.close()

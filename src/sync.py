#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Script para poder migrar de manera automatizada las cuentas de email con imapsync ##

import os
import sys
from subprocess import Popen, PIPE
from time import strftime
from optparse import OptionParser


def sync (origen, destino):
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
    args = " --syncinternaldates --useheader 'Message-Id' --host1 %s --port1 993 --user1 %s --password1 %s --ssl1 \
            --host2 %s --port2 993 --user2 %s --password2 %s --ssl2 --authmech1 LOGIN --authmech2 LOGIN --split1 200 --split2 200 \
            --nofoldersizes --skipsize --allowsizemismatch --exclude 'Drafts|Trash|Spam|Sent'"
        
    args2 = " --syncinternaldates --useheader 'Message-Id' --host1 %s --port1 993 --user1 %s --password1 %s --ssl1 \
            --host2 %s --port2 993 --user2 %s --password2 %s --ssl2 --noauthmd5 --authmech1 LOGIN --authmech2 LOGIN --split1 200 --split2 200 --nofoldersizes --skipsize --allowsizemismatch \
            --folder 'Inbox/Sent' --prefix2 '[Gmail]/' --regextrans2 's/Inbox\/Sent/Sent Mail/' \
            --folder \"Inbox/Spam\" --prefix2 '[Gmail]/' --regextrans2 's/Inbox\/Spam/Spam/' \
            --folder \"Inbox/Trash\" --prefix2 '[Gmail]/' --regextrans2 's/Inbox\/Trash/Trash/' \
            --folder \"Inbox/Drafts\" --prefix2 '[Gmail]/' --regextrans2 's/Inbox\/Drafts/Drafts/'"
    # IP servidor IMAP viejo
    host1 = origen
    # IP servidor IMAP nuevo
    host2 = destino

    # Leemos el archivo de la lista de usuarios y ejecutamos imapsync por cada uno de ellos
    for line in userList.readlines():
        imapsync = Popen(command + args % (host1, line.split(" ")[0], line.split(" ")[1],
                                           host2, line.split(" ")[2], line.split(" ")[3].rstrip('\n')), stdout=PIPE, shell=True)
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
        
    # Sincronizamos las carpetas que se excluyeron en el paso anterior
    for line in userList.readlines():
        imapsync = Popen(command + args2 % (host1, line.split(" ")[0], line.split(" ")[1],
                                            host2, line.split(" ")[2], line.split(" ")[3].rstrip('\n')), stdout=PIPE, shell=True)
        print '%s --- Sincronizando carpetas especiales en la cuenta "%s"...' % (strftime("%d-%m-%Y %H:%M:%S"), (line.split(" ")[0]))

        # Si el log está habilitado, lo escribimos en un archivo
        if log:
            stdout = imapsync.stdout.read()
            logFile = open("imapsync.log", "a")
            logFile.write('%s --- Sincronizando carpetas especiales en la cuenta la cuenta "%s"... \n\n %s \n\n' % (strftime("%d-%m-%Y %H:%M:%S"),
                                                                                                                    (line.split(" ")[0]), stdout))
            logFile.close()

            # De lo contrario, lo mostramos por pantalla
        else:
            print imapsync.stdout.read()

    # Cerramos el archivo
    userList.close()

def main():
    usage = "Usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-h1", "--host1", dest="host1", help="Servidor de Origen", default="imap.googlemail.com", metavar="HOST1")
    parser.add_option("-h2", "--host2", dest="host2", help="Servidor de Destino", default="imap.googlemail.com", metavar="HOST2")
    
    (options, args) = parser.parse_args()
    main(options.host1, options.host2)
    
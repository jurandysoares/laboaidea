#!/usr/bin/env python3

import cgi
import cgitb
import os
import pwd
import time

cgitb.enable()

print("Content-type: text/plain; charset=utf-8")
print()
if 'PATH_INFO' in os.environ:
    caminho = os.environ['PATH_INFO'][1:].split('/')
    if len(caminho) == 2:
        protocolo = caminho[0]
        usuario = caminho[1]

        print(f'Protocolo: {protocolo}')
        print(f'Usuario: {usuario}')
        try:
            dados_usuario = pwd.getpwnam(usuario)
            print(dados_usuario)
            if dados_usuario.pw_uid >= 1000:
                print('Acesso liberado.')
            else:
                print('Acesso negado.')
        except:
            print('Usuario nao encontrado.')

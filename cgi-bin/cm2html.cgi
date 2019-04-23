#!/bin/sh

DOCS="/var/www/docs"

echo "Content-type: text/html; charset=utf-8"
echo

if [ -z $PATH_INFO ]; then
  SRC=${DOCS}/index.md
else
  SRC=${DOCS}${PATH_INFO}
fi

if [ -f $SRC ]; then
   /usr/bin/cm2html $SRC
else
cat << EOF | /usr/bin/cm2html 
# Página não encontrada
Erro 404 - página não encontrada
EOF

fi

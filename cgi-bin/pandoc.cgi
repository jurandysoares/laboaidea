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
   /usr/bin/pandoc -f markdown_github $SRC
else
cat << EOF | /usr/bin/pandoc -f markdown_github 
# Página não encontrada :disappointed:
Erro 404 - página não encontrada :disappointed:
EOF

fi

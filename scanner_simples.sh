#!/bin/bash

while read -r linha; do
    linha=$(echo "$linha" | tr -d ' \t\r')
    echo "[SCANNER] Linha recebida: '$linha'"
done

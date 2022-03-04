#!/bin/bash
filename=$(echo "$1" | cut -f 1 -d '.')
pandoc -f docx -t markdown ./files/$filename.docx -o ./temp/$filename.md --filter=remove_img_size.py --extract-media=./temp/
python3 convertBase64.py

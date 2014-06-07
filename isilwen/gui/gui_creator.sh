#!/bin/sh

# pyrcc4 gui/icons.qrc > icons.py

for i in `ls -1 *.ui`; do
    file=`basename ${i} .ui`
    pyuic4 $i > ${file}Ui.py
done

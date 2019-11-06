#!/bin/sh

SOURCES='setup.py progressbar.py logging/log.py'

if [ ! -e ./dist ]
then
	mkdir dist
fi

tar -cvzf ./dist/ai42-1.0.0.tar.gz $SOURCES

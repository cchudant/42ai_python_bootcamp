#!/bin/bash

URL=https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
INSTALL_SCRIPT=/tmp/Miniconda3-latest-MacOSX-x86_64.sh
INSTALL_DIR=/goinfre/anaconda3

function remove_python {
	rm -rf $INSTALL_DIR
	sed -i '' "/^export PATH='\/goinfre\/anaconda3\/bin:\$PATH'$/d" ~/.zshrc
	echo "Python has been removed."
}

function install_python {
	if curl $URL 2>/dev/null >$INSTALL_SCRIPT &&
		bash $INSTALL_SCRIPT -b -p $INSTALL_DIR >/dev/null &&
		rm $INSTALL_SCRIPT
	then
		echo "export PATH=$INSTALL_DIR/bin:\$PATH" >> ~/.zshrc
		echo "Python has been installed."
		echo "Use \`source ~/.zshrc\` or restart your shell to update your environment."
	else
		echo "Install error."
		exit -1
	fi
}

if [ "$1" = 'install-python' ]
then

	VERSION="$(python -V 2>&1 | grep '3.7')"
	if [ -z "$VERSION" ]
	then

		if [ -e "$INSTALL_DIR" ]
		then
			echo "Something is wrong with your configuration.." 1>&2
			echo "Please remove folder $INSTALL_DIR and retry." 1>&2
			exit 1
		fi

		install_python
		exit 0

	else
		echo "Python is already installed, do you want to reinstall it ?"

		while [ "$ANSWER" != yes ] && [ "$ANSWER" != no ]
		do
			echo -n "[yes|no]> "
			read ANSWER
		done
		
		if [ "$ANSWER" = yes ]
		then
			remove_python
			install_python
		else
			echo "exit."
		fi

		exit 0
	fi

elif [ "$1" = 'remove-python' ]
then

	if [ ! -e "$INSTALL_DIR" ]
	then
		echo "Python is not installed!" 1>&2
		exit 1
	fi

	remove_python
	exit 1

else
	echo "Usage: $0 [install-python|remove-python]" 1>&2
	exit 1
fi

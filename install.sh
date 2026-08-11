#!/usr/bin/env bash

dev_env=

read -p "enter your prefered development environment (absolute path eg. '~/Code/open-source/'): " dev_env

cd $DE || mkdir $DE
#git clone github.com/marcmav/dotfiles.git
#cd dotfiles/

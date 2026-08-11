#!/usr/bin/env bash

dev_env=

read -p "enter your prefered development environment (absolute path eg. '~/Code/src/open-source/'): " dev_env

cd $dev_env || mkdir $dev_env
#git clone github.com/marcmav/dotfiles.git
#cd dotfiles/

#!/usr/bin/env bash

DE=

read -p "enter your prefered development environment (absolute path eg. '~/Code/open-source/'): " DE

cd $(DE) || mkdir $(DE)
git clone github.com/marcmav/dotfiles.git
cd dotfiles/

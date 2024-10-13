#!/bin/bash

RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

extension=*
directory=.

while [ $# -gt 0 ]; do
  case $1 in
    -h | --help)
      echo "search_file.sh"
      echo "    [--extension <extension>] [--directory <directory>]"
      echo "    [--help] [--interactive]"
      exit 0
      ;;

    --extension)
      if [[ -z "$2" || "$2" == -* ]]; then
        printf "${RED}error: file extension not specified.${NC}" >&2
        exit 1
      fi

      extension=.$2
      ;;
    
    --directory)
      if [[ -z "$2" || "$2" == -* ]]; then
        printf "${RED}error: directory not specified.${NC}" >&2
        exit 1
      fi

      directory=$2
      ;;

    --interactive)
      interactive=true
      ;;
  esac
  shift
done

search_and_print () {
  extension=$1
  directory=$2

  files=$(ls $directory)
  count=0
  for file in $files
  do
    if [[ $file == *$extension ]]; then
      echo $file
      let count+=1
    fi
  done

  echo "Total $count files."
}

if [ -z $interactive ]; then
  search_and_print $extension $directory
else
  for (( ; ; )) do
    printf "${CYAN}Please input file extension (q to quit): ${NC}"
    read extension

    if [ $extension == q ]; then
      exit 0
    fi

    printf "${CYAN}Please input directory to search (q to quit): ${NC}"
    read directory

    if [ $directory == q ]; then
      exit 0
    fi

    search_and_print $extension $directory
  done
fi


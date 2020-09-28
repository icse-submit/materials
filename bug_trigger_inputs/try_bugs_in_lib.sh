#!/bin/bash

lib=$1

function run_bugs() {
   choice=$1
   pushd $choice > /dev/null
   bash run_each.sh
   popd
}

if [[ -z "$lib" ]];then
  echo "Please provide a valid choice [mxnet | pytorch | tensorflow]"
  exit 1
elif [[ "$lib" != "mxnet" && "$lib" != "pytorch" && "$lib" != "tensorflow" ]];then
  echo "Unknown choice $lib. Please select from [mxnet | pytorch | tensorflow]"
  exit 1
fi

run_bugs "$lib"

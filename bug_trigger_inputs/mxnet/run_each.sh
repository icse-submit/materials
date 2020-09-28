#!/bin/bash

for i in */;do
  for j in ${i}*;do
    echo "----- In $j -----"
    pushd $j > /dev/null
      for p in *.py;do
        echo $p
        timeout 10s python $p
        if [[ "$?" == 124 ]];then
          echo "timeout"
        fi
        echo "> continue? [enter/n]"
        read choice
        if [[ $choice == "n" ]];then
          exit 0
        fi
      done
     popd > /dev/null
  done
done

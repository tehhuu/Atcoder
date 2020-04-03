#!/bin/sh

<< COMMENTOUT
Ex) abc 13 b
./ABC/13 に 13-B.py を作成 → 開く → テンプレ記入
Ex) arc 13 b
./ARC/ARC13 に ARC13-B.py を作成 → 開く → テンプレ記入
Ex) agc 13 b
./ARC/AGC13 に AGC13-B.py を作成 → 開く → テンプレ記入
Ex) edc (なんでもOK) b
./Others/EDC/に EDC-B.py を作成 → 開く → テンプレ記入
COMMENTOUT

make_files(){
    #echo $1
    dir=`echo | tr '[a-z]' '[A-Z]' <<< $1`
    #echo $dir
    if [ $dir = 'ABC' ]
    then
        cd $dir
        if [ ! -d $2 ]
        then
            mkdir $2
        fi
        cd $2
        filename=$2
        filename+='-'
        filename+=`echo | tr '[a-z]' '[A-Z]' <<< $3`

    else
        if [ ! -d $dir ]
        then
            cd Others
            if [ ! -d $dir ]
            then
                mkdir $dir
            fi
            cd $dir
        else
            cd $dir
            dir+=$2
            if [ ! -d $dir ]
            then
                mkdir $dir
            fi
            cd $dir
        fi
        filename=$dir
        filename+='-'
        filename+=`echo | tr '[a-z]' '[A-Z]' <<< $3`
    fi

    touch "$filename.py"

}

make_files $1 $2 $3

open $filename.py

cat <<EOS > $filename.py
    import sys
    def ii(): return int(sys.stdin.readline())
    def mi(): return map(int, sys.stdin.readline().split())
    def li(): return list(map(int, sys.stdin.readline().split()))
    def li2(N): return [list(map(int, sys.stdin.readline().split())) for i in range(N)]
    def dp2(ini, i, j): return [[ini]*i for i2 in range(j)]
    def dp3(ini, i, j, k): return [[[ini]*i for i2 in range(j)] for i3 in range(k)]
    #import bisect #bisect.bisect_left(B, a)
    #from collections import defaultdict #d = defaultdict(int) d[key] += value
EOS
#!/bin/sh

<< COMMENTOUT
source makefile.sh $1 $2 $3
Ex)abc 13 b
./ABC/013 に移動 → 13-B.py を作成 → 開く → テンプレ記入
Ex) arc 13 b
./ARC/ARC13 に移動 → ARC13-B.py を作成 → 開く → テンプレ記入
Ex) agc 13 b
./ARC/AGC13 に移動 → AGC13-B.py を作成 → 開く → テンプレ記入
Ex) *** (なんでもOK) b
./Others/***/ に移動 → EDC-B.py を作成 → 開く → テンプレ記入
COMMENTOUT

make_files(){
    #echo $1
    dir=`echo | tr '[a-z]' '[A-Z]' <<< $1`
    #echo $dir
    if [ $dir = 'ABC' ]
    then
        cd $dir
        sub_dir="00$2"
        sub_dir=${sub_dir: -3}
        if [ ! -d $sub_dir ]
        then
            mkdir $sub_dir
        fi
        cd $sub_dir
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
sys.setrecursionlimit(10**8)
def ii(): return int(sys.stdin.readline())
def mi(): return map(int, sys.stdin.readline().split())
def li(): return list(map(int, sys.stdin.readline().split()))
def li2(N): return [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
def dp2(ini, i, j): return [[ini]*i for _ in range(j)]
#import bisect #bisect.bisect_left(B, a)
#from collections import defaultdict #d = defaultdict(int) d[key] += value
#from collections import Counter # a = Counter(A).most_common()
#from itertools import accumulate #list(accumulate(A))

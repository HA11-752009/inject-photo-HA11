#!/bin/bash HA11 Hacker 😂
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'
figlet -f Univers "HA11" | lolcat
echo -e "${RED}سيتم تشغيل الاسكربت بعد 10 ثواني"
for h in {10..1}
do
  echo  -e "${BLUE} الوقت المتبقي : $h ثانيه"
  sleep 1
done
echo -e "${GREEN}سبتم فتح الاداه الان"
echo -e "${YELLOW}برجاء انتظار لحظه....؟${NC}"
sudo python run.py
exit
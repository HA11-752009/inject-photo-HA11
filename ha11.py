#/usr/evn python HA11 Hacker 😂
# `تم عمل هذا الاسكربت من HA11`
# فضلا وليس امراً اشترك في القنوات التاليه 
# youtube
# https://youtube.com/@abdallah-ha11?si=hajqVkWLuHGDeHnG
# تبرع علي spectrocoin
# bc1qs7pcruqtyjmxe84hfpz9atyw20kh763ywfq72j
import os
import sys
import subprocess
from colorama import Fore, Back, Style, init

# تهيئة مكتبة colorama
init(autoreset=True)

def check_root_privileges():
    if os.geteuid() != 0:
        print(Fore.RED + "error : عليك التحقق من الرووت")
        sys.exit(1)

def install():
    run_script('run2.sh')
def run_script(script_name):
        script_path = find_script(script_name)
        if script_path:
            print(Back.LIGHTBLUE_EX +f"جار تشغيل الاسكربت: {script_path}")
            subprocess.run(['bash', script_path])
            print(f"تم الانتهاء من الاسكربت run2.sh.")

def find_script(script_name):
    # Example: search for script in a specific directory
    # You may customize this to fit your actual script search logic
    return script_name
def main():
    check_root_privileges()
    print(Fore.LIGHTYELLOW_EX+'y == yes \nn == no')
    install = input(Fore.MAGENTA+'هل تريد تنزيل الادوات.....؟ (y/n): ')

    if install.lower() == 'y':
        print(Fore.GREEN + "true : 🥰 تم التحقق من الرووت بنجاح")
        os.system('figlet -f 3d "HA11" | /usr/games/lolcat')
        print(Fore.LIGHTGREEN_EX + 'true : جاري تحميل الموارد')
        os.system('sudo apt-get update')
        os.system('sudo apt-get install lolcat -y')
        os.system('sudo apt install figlet -y')
        print(Fore.BLUE + 'true : جاري فك ضغط الملف برجاء الانتظار......')
        os.system('sudo unzip figlet-fonts-master.zip -d /usr/share/figlet/')
        print(Fore.GREEN + 'true : جاري التشغيل')
        script_name = 'run2.sh'
        script_path = find_script(script_name)
        run_script(script_path)
    elif install.lower() == 'n':
        script_name = 'run2.sh'
        script_path = find_script(script_name)
        run_script(script_path)
    else:
        print(Back.BLACK + 'error : هناك خطاء يبدو ان ليس لديك هناك مساحه او ليس هذا متوفر لي النظام الخاص بك الرجاء الدخول الي موقع كالي لينكس عبر هذا الموقع https://www.kali.org/docs/general-use/kali-linux-sources-list-repositories/')
         

if __name__ == "__main__":
    main()

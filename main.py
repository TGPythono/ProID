import os
import json
import random
import requests
from faker import Faker
from datetime import datetime
from PIL import Image
from io import BytesIO
import qrcode

fake = Faker()

قائمة دول

countries = ['Iraq', 'USA', 'Germany', 'France', 'Egypt', 'Japan', 'Turkey', 'Brazil', 'Russia', 'India']

إنشاء مجلد التخزين

if not os.path.exists("output/ids"): os.makedirs("output/ids")

توليد صورة شخصية وهمية

def generate_fake_image(save_path): try: response = requests.get("https://thispersondoesnotexist.com", headers={"User-Agent": "Mozilla/5.0"}) if response.status_code == 200: with open(save_path, 'wb') as f: f.write(response.content) return True except: pass return False

توليد هوية وهمية

def generate_fake_id(country): full_name = fake.name() id_number = fake.unique.uuid4() birth_date = fake.date_of_birth(minimum_age=18, maximum_age=60).strftime("%Y-%m-%d") address = fake.address().replace("\n", ", ") phone = fake.phone_number() email = fake.email() blood_type = random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']) gender = random.choice(['Male', 'Female']) job = fake.job() signature = fake.name() + "_sig" fingerprint = fake.sha1() coordinates = f"{fake.latitude()}, {fake.longitude()}" creation_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

image_path = f"output/ids/{full_name.replace(' ', '_')}_photo.jpg"
generate_fake_image(image_path)

qr_data = f"{full_name} | {id_number} | {country}"
qr_img = qrcode.make(qr_data)
qr_path = f"output/ids/{full_name.replace(' ', '_')}_qr.png"
qr_img.save(qr_path)

identity = {
    "full_name": full_name,
    "id_number": id_number,
    "birth_date": birth_date,
    "gender": gender,
    "country": country,
    "address": address,
    "phone": phone,
    "email": email,
    "blood_type": blood_type,
    "job": job,
    "signature": signature,
    "fingerprint": fingerprint,
    "coordinates": coordinates,
    "created_at": creation_time,
    "photo": image_path,
    "qr_code": qr_path
}

json_path = f"output/ids/{full_name.replace(' ', '_')}_id.json"
with open(json_path, 'w') as f:
    json.dump(identity, f, indent=4)

print(f"[+] Generated ID for {full_name} ({country})")

تشغيل الأداة

if name == 'main': print("\n--- توليد هويات وهمية احترافية ---") for i, c in enumerate(countries): print(f"{i + 1}. {c}")

choice = int(input("اختر الدولة: ")) - 1
num = int(input("كم هوية تريد توليدها؟: "))

for _ in range(num):
    generate_fake_id(countries[choice])

print("\nتم توليد جميع الهويات بنجاح وحفظها في مجلد 'output/ids'")


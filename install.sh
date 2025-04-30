#!/bin/bash

# تنصيب المتطلبات
echo "جاري تنصيب المتطلبات..."
pkg update -y
pkg install python -y
pip install -r requirements.txt

# تشغيل الأداة
echo "تم التنصيب! لتشغيل الأداة اكتب:"
echo "python main.py"
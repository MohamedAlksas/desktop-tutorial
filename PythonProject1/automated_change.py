import socket
import time

# بيانات الاتصال
host = "192.168.127.69"   # IP الراوتر
port = 23                # Telnet بيشتغل على بورت 23
password = "cisco"    # باسورد الدخول
enable_password = "newpass"  # باسورد enable
new_password = "cisco"   # الباسورد الجديد اللي عايز تعمله

# إنشاء اتصال socket
tn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tn.connect((host, port))

# استقبال الرسائل المبدئية
time.sleep(1)
output = tn.recv(4096).decode('ascii', errors='ignore')
print(output)

# إرسال الباسورد
tn.sendall((password + "\n").encode('ascii'))

# انتظار دخول
time.sleep(1)
output = tn.recv(4096).decode('ascii')
print(output)

# دخول enable mode
tn.sendall(b"enable\n")
time.sleep(1)
tn.sendall((enable_password + "\n").encode('ascii'))

# دخول config mode
time.sleep(1)
tn.sendall(b"configure terminal\n")
time.sleep(1)

# تغيير الباسورد
tn.sendall(b"enable password " + new_password.encode('ascii') + b"\n")
time.sleep(1)

# الخروج من config mode
tn.sendall(b"end\n")
time.sleep(1)

# حفظ الإعدادات
tn.sendall(b"write memory\n")
time.sleep(1)
tn.sendall(b"\n")  # تأكيد على الكتابة
time.sleep(2)


# قفل الاتصال
tn.sendall(b"exit\n")

# قراءة اللي حصل
print(tn.recv(4096).decode('ascii'))

# إغلاق السوكيت
tn.close()

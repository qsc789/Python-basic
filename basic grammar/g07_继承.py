class Phone:
    IMEI=None# 序列号
    producer="aaa"# 厂商


    def call_by_4g(self):
        print("4g通话")

class Phone2024(Phone):
    face_id="10001"# 面部识别id

    def call_by_5g(self):
        print("新功能，5g通话")

phone=Phone2024()
print(phone.IMEI)
phone.call_by_4g()
print(phone.face_id)
phone.call_by_5g()

# 多继承
class NFCReader:
    nfc_type="第五代"
    producer="bbb"
    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type="红外遥控"
    def control(self):
        print("红外遥控开启")

class MyPhone(Phone,NFCReader,RemoteControl):
    pass# 不想写新功能，就用pass占位

phone=MyPhone()
print(phone.IMEI)
print(phone.producer)# 父类Phone中属性优先，多继承时，最左边父类属性优先级最高
print(phone.nfc_type)
print(phone.rc_type)
phone.read_card()
phone.write_card()
phone.control()

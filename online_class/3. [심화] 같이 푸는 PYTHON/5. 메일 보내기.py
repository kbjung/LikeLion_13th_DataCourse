import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

def sendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"
    if bool(re.match(reg, addr)):
        smtp.send_message(message)
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")
#유효성 검사 통과하면 메일이 발송되는 함수 작성

message = EmailMessage()

message["From"] = "kbjoong@likelion.org"
message["To"] = "kbjoong11@gmail.com"
message["Subject"] = "제목입니다."
message.set_content("코드라이언 수업중입니다.")
#message에 기록

with open("codelion.png","rb") as image:
    image_file = image.read()
#codelion.png를 읽어서 image 파일에 출력
#image를 읽어 image_file에 저장(컴퓨터가 이미지를 이해할 수 있는 파일로 변환하는 과정)

image_type = imghdr.what("codelion", image_file)
#codelion 파일을 image_file로 읽어서 무슨 확장자인지 파악

message.add_attachment(image_file, maintype = "image", subtype = image_type)
#이메일에 첨부 파일을 첨부.(첨부할 파일, 파일 형식, 파일 확장자)

smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
smtp.login("kbjoong@likelion.org", "###")
sendEmail("kbjoong11@gmail.com")
smtp.quit()
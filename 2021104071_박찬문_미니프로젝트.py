name = input("이름을 입력해 주세요: ")
b_y = int(input("태어난 연도를 입력해 주세요: "))
b_mnd = int(input("태어난 달과 일을 네자리 수로 입력해 주세요: "))
c_y = int(input("현재 연도를 입력해 주세요: "))
c_mnd = int(input("이번 달과 오늘 날짜를 네자리 수로 입력해 주세요: "))

K_age = c_y - b_y +1
C_age = c_y - b_y

if b_mnd > c_mnd:
    C_age -= 1
    print(name,"님의 만 나이는", C_age,"입니다.")
else:
    print(name,"님의 만 나이는",C_age,"입니다.")
    
print(name,"님의 한국식 나이는",K_age,"입니다.")


Asian_zodiac={0:'신',1:'유',2:'술',3:'해',4:'자',5:'축',6:'인',7:'묘',8:'진',9:'사',10:'오',11:'미'}
tst={0:'경',1:'신',2:'임',3:'계',4:'갑',5:'을',6:'병',7:'정',8:'무',9:'기'}
#ten celestial stems


Y_A = b_y%12 #your asian zordiac

n1=Y_A
n2=b_y%10

print("당신은",tst[n2]+Asian_zodiac[n1]+"년에 태어났습니다.")

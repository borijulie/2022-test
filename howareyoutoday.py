import time
student = []
bad = []
st_feel = {}

print("안녕!! 우주반에 온 걸 환영해")
time.sleep(2)
while True :
    name = input("너의 이름을 알려줄래? : ")
    time.sleep(2)
    print("안녕 "+name)
    feel = int(input("오늘 너의 기분이 궁금해! 너의 기분을 1~5단계로 알려줄래?"))
    if feel <= 2 :
        bad.append(name)
        st_feel[name] = feel
        print("오늘은 " +name + "(이)가 기분이 좋지 않구나 선생님께 잘 살펴봐달라고 말씀드릴게 오늘의 아침활동은 무엇을 해야 할지 확인하자!")
    else :
        print("오늘 학교에서 기분이 더 좋아지기 바라^^ 오늘의 아침활동은 무엇을 해야 할지 확인하자!")
    selection = input("학생이 입력을 다 하였나요? (예/아니요) : ")
    if selection == '예' :
        break
    else :
        continue
print("오늘 기분이 좋지 않은 친구는 다음과 같습니다.")
print(bad)
print(st_feel)

# 생일 문제를 시뮬레이션하여 23명의 사람들 중에서 같은 생일을 가진 사람이 있는지를 확인하는 코드

def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")


if __name__ == "__main__":
    test_birthday_problem()
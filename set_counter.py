import msvcrt
import sys

def _stand_by():
    ch=msvcrt.getch()
    if (ch==b'q' or ch==b'Q'):
        sys.exit()


def juarez_valley_set_method():  # 운동 세트법
    print("input maximum reps: ", end="")
    sys.stdout.flush()  # 출력 버퍼를 비워 사용자의 입력을 즉시 화면에 출력
    reps = int(input())
    b_set = [i+1 for i in range (reps)]
    a_set = sorted(b_set, reverse=True)

    for i in range(len(a_set)):
        print("\n\n--------", i+1, "set --------\n")
        print("a_set: ", a_set[i])
        print("b_set: ", b_set[i], "\n\n--Press (q/Q) to exit--")
        _stand_by()

if __name__ == "__main__":
    juarez_valley_set_method()
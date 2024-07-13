import msvcrt
import sys
import time

def _stand_by():
    ch=msvcrt.getch()
    if (ch==b'q' or ch==b'Q'):
        sys.exit()

def _timer(break_time):
    for remaining in range(break_time, 0, -1):
        print(f"Break Timer: {remaining:02d} seconds", end='\r')
        time.sleep(1)
    print(" " * 30, end='\r') # 라인에 공백 출력하여 _timer 함수의 문자열 지움

def juarez_valley_set_method():  # 운동 세트법
    print("Input Maximum Reps: ", end="")
    sys.stdout.flush()  # 출력 버퍼를 비워 사용자의 입력을 즉시 화면에 출력
    reps = int(input())
    even_set = [i+1 for i in range (reps)]
    odd_set = sorted(even_set, reverse=True)

    print("Input Break Time(sec): ", end="")
    sys.stdout.flush() 
    break_time = int(input())

    for i in range(len(odd_set)):
        print(f"\n\n--------- {i+1:2d} ---------\n")
        print(f"{i*2+1:2d} Set: \t{odd_set[i]:2d} reps")
        _stand_by()
        _timer(break_time)
        print(f"{i*2+2:2d} Set: \t{even_set[i]:2d} reps")
        _stand_by()
        _timer(break_time)
        print("\n--Press (q/Q) to exit--")

if __name__ == "__main__":
    juarez_valley_set_method()
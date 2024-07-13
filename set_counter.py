import sys
import asyncio
import msvcrt

async def _timer(break_time):
    for remaining in range(break_time, 0, -1):
        print(f"Break Timer: {remaining:02d} seconds", end='\r')
        await asyncio.sleep(1)
    print(" " * 30, end='\r')  # 타이머 종료 후 공백 출력하여 지우기

async def _check_for_quit_and_run_timer(timer_event):
    loop = asyncio.get_event_loop()
    while True:
        user_input = await loop.run_in_executor(None, msvcrt.getch)
        if user_input.lower() == b'q':
            print("\nExiting...")
            loop.call_soon_threadsafe(loop.stop)
            break
        else:
            timer_event.set()

async def juarez_valley_set_method():  # 운동 세트법
    print("Input Maximum Reps: ", end="")
    sys.stdout.flush()  # 출력 버퍼를 비워 사용자의 입력을 즉시 화면에 출력
    reps = int(input())
    even_set = [i + 1 for i in range(reps)]
    odd_set = sorted(even_set, reverse=True)

    print("Input Break Time(sec): ", end="")
    sys.stdout.flush()
    break_time = int(input())

    timer_event = asyncio.Event()
    asyncio.create_task(_check_for_quit_and_run_timer(timer_event))

    for i in range(len(odd_set)):
        print(f"\n\n--------- {i + 1:2d} ---------\n")
        print(f"{i * 2 + 1:2d} Set: \t{odd_set[i]:2d} reps")
        await timer_event.wait()
        timer_event.clear()
        await _timer(break_time)
        print(f"{i * 2 + 2:2d} Set: \t{even_set[i]:2d} reps")
        await timer_event.wait()
        timer_event.clear()
        await _timer(break_time)
        print("\n--Press (q/Q) to exit--")

if __name__ == "__main__":
    try:
        asyncio.run(juarez_valley_set_method())
    except RuntimeError as e:
        if str(e) != "Event loop stopped before Future completed.":
            raise

from collections import deque

def main():
    dq = deque([], maxlen=3)
    for i in range(6):
        dq.append(i)
        print(dq)


if __name__ == "__main__":
    main()


import argparse

def wordcount(fname):
    try: 
        fhand = open(fname)
    except Exception:
        print("Cound not open the file")
        exit()

    count = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word not in count:
                count[word] = 1
            else:
                count[word] += 1
    return count

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", type=str, help="filename")
    args = parser.parse_args()

    counts = wordcount(args.f)
    filtered = {key:value for key, value in counts.items() if value < 20 and value > 16}
    print(filtered)


if __name__ == "__main__":
    main()

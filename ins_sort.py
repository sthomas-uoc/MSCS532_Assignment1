
def ins_sort(data):
    for i in range(0, len(data) - 1):
        # print(i)
        for j in range(i, len(data)):
            # print(i, j)
            if data[i] < data[j]:
                t = data[i]
                data[i] = data[j]
                data[j] = t
            # print(i, j, data)

    return data

def demo_ins_sort():

    data = list(range(0, 10))

    print(data)

    print(data[0], data[len(data) - 1])

    sorted = ins_sort(data)

    print(data)

    assert sorted[0] == data[len(data) - 1]

if __name__ == "__main__":
    demo_ins_sort()



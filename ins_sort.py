import random

# Sorts data using insertion sort in monotoncally decreasing order
def ins_sort(data):
    for i in range(0, len(data) - 1):
        # print(i)
        for j in range(i, len(data)):
            # print(i, j)
            if data[i] < data[j]: # Ensures decreasing order
                t = data[i]
                data[i] = data[j]
                data[j] = t
            # print(i, j, data)

def demo_ins_sort():

    # Create serial data
    data = list(range(0, 10))

    # print(data)

    # print(data[0], data[len(data) - 1])

    ins_sort(data)

    # print(data)

    # Verify 
    assert 0 == data[len(data) - 1]
    assert 9 == data[0]

    # Create reversed serial data
    data = list(range(10, 0, -1))
    # print(data)
    ins_sort(data)
    # print(data)
    assert 1 == data[len(data) - 1]
    assert 10 == data[0]

    # Create random data
    data = random.sample(range(50, 5000), 100)
    # print(data)
    ins_sort(data)
    # print(data)
    assert data[0] > data[len(data) - 1]

if __name__ == "__main__":
    demo_ins_sort()



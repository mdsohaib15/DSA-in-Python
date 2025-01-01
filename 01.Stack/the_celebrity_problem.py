from stack import Stack
l = [
    [0, 0, 1, 1],  # Person 0 knows 2 and 3
    [0, 0, 1, 0],  # Person 1 knows 2
    [0, 0, 0, 0],  # Person 2 knows no one (candidate for celebrity)
    [0, 0, 1, 0]   # Person 3 knows 2
]

def find_the_celeb(l):
    s = Stack()

    for i in range(len(l)):
        s.push(i)

    while s.size() >= 2:
        i = s.pop()
        j = s.pop()

        if l[i][j] == 0:
            s.push(i)
        else:
            s.push(j)

    celeb = s.pop()

    for i in range(len(l)):
        if i != celeb:
            if l[i][celeb] == 0 or l[celeb][i] == 1:
                # Ensure all rows are checked before concluding
                print('No one is a celebrity')
                return

    # If all conditions are satisfied, declare the celebrity
    print('The celebrity is:', celeb)


find_the_celeb(l)
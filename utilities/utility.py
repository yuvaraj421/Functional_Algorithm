import time
import random
import math


def my_fun():
    start_time = 0
    stop_time = 0
    elapsed = 0

    def start1():
        start1.start_timer = time.time()
        print("start time is", start1.start_timer)

    def stop1():
        stop1.stop_timer = time.time()
        print("stop time is", stop1.stop_timer)

    def elapsed1():
        elapsed1.elapse_timer = stop1.stop_timer - start1.start_timer
        print("elapse time is", elapsed1.elapse_timer)
        print("converting million to seconds", (elapsed1.elapse_timer // 1000), "sec")

    try:
        a = int(input("Press 0 to start the time "))
        b = int(input("Press 1 to Stop the time "))
        start1()
        stop1()
        elapsed1()

    except ValueError:
        print("Invalid Input")


"**************************************** leap year *************************************************"


def replace_fun():
    # assign input number to the name
    name = input("enter user name")
    # if length of the name is greater than 2
    if len(name) > 2:
        print("hello" + name + " how are you")
    else:
        print("enter minimum 3 character")


"************************************************* power of 2 ********************************************************"


def pow_func():
    num = 4
    for i in range(num):
        print(math.pow(2, i))


"************************************************** leap year *********************************************"


def leap_year():
    year = str(input("Enter year to be checked:"))
    number = int(year)
    if len(year) == 4:
        if (number % 4 == 0) and (number % 100 != 0) or (number % 400 == 0):
            print("The year is a leap year!")
        else:
            print("The year isn't a leap year!")
    else:
        print("enter valid year format 4digit")


"************************************************ 2d array ********************************************************"


def my_func(row, col, list1):
    # loop1 in range of 0 to row
    for i in range(row):
        # loop2 in range of 0 to col
        for j in range(col):
            # assign input number to the val
            val = input('enter the number')
            # list1[i][j] = val
            # loop1 in range of 0 to row
            for i in range(row):
                # loop2 in range of 0 to col
                for j in range(col):
                    # print list1 if i and j
                    print(list1[i][j], end=" ")
                    print()
                    print()

    row = int(input("enter row number \n"))
    col = int(input("enter col number\n"))
    list1 = [[0 for i in range(col)] for j in range(row)]
    my_func(row, col, list1)


"******************************************* quadratic *********************************************************"


def quadratic_func():
    a = float(input("enter the value of A"))
    b = float(input("enter the value of B"))
    c = float(input("enter the value of C"))
    delta = b * b - 4 * a * c
    print("delta", delta)
    try:
        root1 = float(-b + math.sqrt(delta)) / (2 * a)
        root2 = float(-b - math.sqrt(delta)) / (2 * a)

        print("value of root1:", root1)
        print("value of root2:", root2)
    except Exception as e:
        print(e)


"******************************************** triplets ************************************************"


def triplets(size, list1):
    # assign zero value to the count
    count = 0
    # loop1 in range of 0 to size
    for i in range(0, size):
        # loop2 in range of 0 to size
        for j in range(i + 1, size):
            # loop3 in range of 0 to size
            for k in range(j + 2, size):
                # if list1 of i and list1 of j and list3 of k is equal to zero
                if (list1[i]) + (list1[j]) + (list1[k]) == 0:
                    # print the values of list1
                    print("list1[i]+ list1[j]+ list1[k]")
                    # now count is incremented
                    count = count + 1
                    # print the total triplets
    print("total number of triplets = ", count)


"******************************************* harmonic number *****************************************"


def harm_func():
    # assign input number to the n
    n = int(input("Enter the number of terms: "))
    # assign zero value to sum1
    sum1 = 0
    for i in range(1, n + 1):
        # if i range between 1 , n+1 it prints harmonic number
        sum1 = sum1 + (1 / i)
        # print the harmonic number of series
    print("The sum of series is", round(sum1, 2))


"*********************************************************** gambler method *******************************************"


def gambler_method(stake, goals, trails):
    # random function to generate random number
    ran_num = random.randint(0, 1)
    # initialize bet, win and loss to zero
    bet, win, loss = 0, 0, 0

    for i in range(trails):
        # assigning stake value to the cash
        cash = stake

        while (cash > 0) and (cash < goals):
            # while cash grater than zero and cash is less than goals increment bet
            bet = bet + 1
        if ran_num < 0.5:
            # if random number is less than 0.5 then increment the cash
            cash = cash + 1
        else:
            # if condition fails then decrement cash
            cash = cash - 1

        if cash == goals:
            # if cash equals goals then increment the wins
            win = win + 1
        else:
            # if cash is not equals to goals then increment loss
            loss = loss + 1

        print("win ", win)
        print("loss ", loss)
        print("win %", (win / trails) * 100)
        print("loss %", (loss / trails) * 100)


"***************************************** flip coin *************************************************************"


def coinToss():
    # assign input number into the number
    number = int(input("Number of times to flip coin: "))
    # assign zero value to heads
    heads = 0
    # assign zero value to tails
    tails = 0
    # count = 0
    for amount in range(0, number):
        flip = random.random()
        # count += 1
        if flip < 0.5:
            # if condition is true heads will be incremented
            heads += 1
        else:
            # if condition false tails will incremented
            tails += 1
            # print the count of heads and tails
    print("Count of head is : ", heads)
    print("Count of tails : ", tails)
    print("percentage of Heads : ", (heads / number) * 100)
    print("percentage of Tails : ", (tails / number) * 100)

    # print(str(recordList))
    # print(str(recordList.count("Heads")) + str(recordList.count("Tails")))


"****************************************************** factors *******************************************************"


def fac_fun():
    n = int(input("enter the number"))
    # input is converted to integer
    i = 2
    factors = []
    while i * i <= n:
        # if condition true i will be incremented
        if n % i:
            i += 1
    else:
        # if condition fails factors append to i
        n //= i
        factors.append(i)
    if n > 1:
        factors.append(n)
        # if condition true print the factors
        print(factors)


"************************************************* distance **********************************************************"


def my_function():
    try:
        # assign input number to x
        x = int(input("enter the number"))
        # assign input number to y
        y = int(input("enter the number"))
        # assign value to a
        a = x * x
        # assign y value to b
        b = y * y
        distance = math.sqrt(a + b)
        # print the euclidean distance
        print("euclidean distance =", distance)
    except Exception as e:
        print(e)


"************************************************** wind chill ********************************************************"


def windchill(temperature, wind_speed):
    # condition between temperature and wind speed
    if temperature > 50 and 120 > wind_speed > 3:

        print("it is not possible ")

    else:

        # formula for wind chill

        wind_chill = 35.74 + 0.6215 * temperature + ((0.4275 * temperature) - 35.75 * (math.pow((wind_speed), 0.16)))
        # print wind chill equal to wind chill
        print("wind_chill = ", wind_chill)


"******************************************* coupon *******************************************************************"


def coupon(coupon_number):
    # assign zero value to the count
    count = 0
    # assign empty list to a
    a = []
    # loop in range of 0 to coupon_number
    while len(a) < coupon_number:
        rand_num = random.randint(1, coupon_number)
        count += 1
        # count is incremented
        if rand_num not in a:
            a.append(rand_num)
            # assigned random function to the number
    print(a)
    # print total random numbers is equal to count
    print("Total random numbers to generate coupon", count)


"******************************************************* anagram ******************************************************"


# anagram method


def anagram(string1, string2):
    # assign the value to count as 0
    count = 0
    # string3 equal to upper case of string1
    string3 = string1.upper()
    # string4 equal to upper case of string2
    string4 = string2.upper()
    # if length of string1 is equal to length os string2
    if len(string1) == len(string2):
        # loop1 is of range  0 to length of string3
        for loop1 in range(0, len(string3)):
            # loop2 is of range  0 to length of string4
            for loop2 in range(0, len(string4)):

                # if string3 is equal to string4
                if string3[loop1] == string4[loop2]:
                    # now count is increment
                    count += 1
                    # break the condition
                    break
                    # if length of the string is equal to count
        if len(string1) == count:
            # now print string1 is matching string2
            print(string1, "is a matching ", string2, "\n")
            # now it's an anagram
            print("it's  anagram", "\n")
        else:
            # if condition fails print not an anagram
            print("it's  not a anagram", "\n")
    else:
        # print valid data
        print("enter valid data")


"********************************************* prime num **************************************************************"


def prime():
    # loop range of 0 to 1001
    for i in range(0, 1001):
        # assign zero value to the status
        status = 0
        # loop in range between 2 to i-1
        for j in range(2, i - 1):
            # if reminder is equal to zero
            if i % j == 0:
                # assign  1 value to the status
                status = 1
                # now break the condition
                break
                # if status is equal to zero
        if status == 0:
            # print the i value
            print(i, end="" "\n")


"********************************************* palindrome *************************************************************"


def palin_func():
    def reverse(str):
        return str[::-1]

    def isPalindrome(str):
        rev = reverse(str)

        if str == rev:
            return True
        return False

    str = "1"
    ans = isPalindrome(str)
    if ans == 1:
        print("Yes")
    else:
        print("False")


"*************************************************** search number ****************************************************"


def search_number(low, high):
    if high - low == 1:
        return low
        # if the difference between high and low is 1 then return low value
    mid = low + (high - low) / 2
    # mid value
    print("Is Your Number Less then", mid, "Press 1 for Yes and 0 for No")
    val = int(input())
    if val == 1:
        return search_number(low, mid)
        # if val equals to 1 then return low and mid
    elif val == 0:
        return search_number(mid, high)
        # if val equals to 0 then return mid and high
    else:
        print("Valid Input")


"************************************************ binary search*****************************************************"


def string_binary():
    n = int(input("enter the array size\n"))
    temp = []
    # adding values to the list
    for i in range(n):
        str1 = input("enter the elements\n")
        temp.append(str1)

    str1 = sorted(temp)
    # assign start as zero
    print(str1)
    start = 0
    # end as length of list minus 1
    end = len(str1) - 1
    # element to be searched
    target = input("enter the element to search\n")
    flag = True
    while start <= end:
        # formula to find the mid value
        middle = (start + end) // 2
        # print(middle)
        # mid value of the list
        if str1[middle] == target:
            # result = str1[middle]
            print("Element ", str1[middle], " found at ", middle)
            flag = False

        if str1[middle] > target:
            # if the mid value is greater than target then end equals mid -1
            end = middle - 1

        elif str1[middle] < target:
            # if the mid value is lesser than target then start equals mid +1
            start = middle + 1
            # print("element is not search")
        else:
            # if condition is not satisfied then value equals to middle
            result = str1[middle]
            # print("Condition not satisfied", result)
            break

    # print("element is not present \n")

    if flag:
        print("Element is not present")
        # print()
    else:
        r = result
        print(r)


"******************************************** binary search integer ***************************************************"


def int_binary():
    size = int(input("enter the size \n"))
    lis = []
    temp = []
    # adding values to the list
    for i in range(size):
        val = int(input("enter the elements\n"))
        temp.append(val)
        lis = sorted(temp)
        # assign start as zero
    print(lis)
    start = 0
    # end as length of list minus 1
    end = len(lis) - 1
    # element to be searched
    target = int(input("enter the element to search\n"))
    flag = True
    while start <= end:
        # formula to find the mid value
        middle = (start + end) // 2
        # print(middle)
        # mid value of the list
        if lis[middle] == target:
            # result = lis[middle]
            print("Element ", lis[middle], " found at ", middle)
            flag = False

        if lis[middle] > target:
            # if the mid value is greater than target then end equals mid -1
            end = middle - 1

        elif lis[middle] < target:
            # if the mid value is lesser than target then start equals mid +1
            start = middle + 1

        else:
            # if condition is not satisfied then value equals to middle
            result = lis[middle]
            break

    # print("element is not present \n")

    if flag:
        print("Element is not present")


"*********************************************** temperature conversion **********************************************"


def temp_func(cel):
    fahrenheit = 32 + ((9 / 5) * cel)
    cel = 5 / 9 * (fahrenheit - 32)

    print("enter temperature is", fahrenheit)
    print("enter temperature is", cel)


"*************************************************** day of week ******************************************************"


def day_func():
    month = int(input("enter the month \n"))
    date = int(input("enter the date \n"))
    year = int(input("enter the year \n"))
    match = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

    try:
        if (date <= 31) and (month <= 12):
            year = year - (14 - month) / 12
            # year value
            x = year + year / 4 - year / 100 + year / 400
            month = month + 12 * ((14 - month) / 12) - 2
            day = int((date + x + 31 * month / 12) % 7)
            print("day =", day)
            # print("month=", month)
            print(match[day])

        else:
            print("enter the correct date and month")

    except NameError as e:
        print(e)


"************************************************* to binary**********************************************************"


def to_binary(number):
    # assigned string value to the binary_num
    bin_num = " "
    for i in range(1, number):
        # i in range of the 1 to the number
        while number != 0:
            # holds the reminder value
            remainder = number % 2
            # adding string values
            bin_num = str(remainder) + bin_num
            # holding the coefficient value
            number = number // 2

    print("static to binary", bin_num)


"*********************************************** monthly payment ******************************************"


def month_fun():
    principal = float(input("enter the principal\n"))
    year = int(input("enter the year\n"))
    interest = float(input("enter the interest_rate\n"))
    r = interest / (12 * 100)
    n = 12 * year
    payment = (principal * r) / (1 - (1 + r) ** (-n))
    print(payment)


"*********************************************** newton ***************************************************"


def newton_fun():
    try:
        c = int(input("enter the c value \n"))
        t = c
        epsilon1 = 1e-15
        while abs(t - c / t) > epsilon1 * t:
            t = (c / t + t) / 2
        print("avg =", t)
    except ValueError as a:
        print(a)
        print("enter integer value ")


"******************************************** bubble sort **********************************************************"


def bubble_sort():
    number = int(input("enter the size of list\n"))
    list1 = []
    for i in range(number):
        val = int(input("enter the elements \n"))
        list1.append(val)
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    print(list1)


"************************************** insertion sort  *********************************************************"


def insertion_sort():
    size = int(input("enter the size \n"))
    list1 = []
    # from range i to size
    for i in range(size):
        val = input("enter the numbers\n")
        # to insert the words in to the list
        list1.append(val)
    # from range 1 to the length of the list1
    for i in range(1, len(list1)):
        temp = list1[i]
        # j value is one less than i value
        j = i - 1
        while (j >= 0) and (temp <= list1[j]):
            # swapping vales of the list
            list1[j + 1] = list1[j]
            j = j - 1  # j value is 1 less than j
        list1[j + 1] = temp
    print(list1)


"******************************************** merge sort ************************************************************"


def merge_sort1(left_half, right_half, list1):
    i = 0
    j = 0
    k = 0
    while (i < len(left_half)) and (j < len(right_half)):
        if left_half[i] < right_half[j]:
            list1[k] = left_half[i]  # assign left half value to the list
            i = i + 1  # increment i value
        else:
            list1[k] = right_half[j]  # assign right half value to the list
            j = j + 1  # increment j value
            k = k + 1  # increment k value
    while i < len(left_half):
        list1[k] = left_half[i]  # assign left half to list when i is lesser than length of left half
        i = i + 1  # increment i
        k = k + 1  # increment k
    while j < len(right_half):
        list1[k] = right_half[j]  # assign right half to list when j is lesser than length of right half
        j = j + 1  # increment j
        k = k + 1  # increment k

    print(list1)


def merge_sort(list1):
    n = len(list1)
    left_half = []  # left half list
    right_half = []  # right half list
    if len(list1) <= 1:
        return  # returns list1
    mid = len(list1) // 2  # mid value
    for i in range(mid):
        left_half.append(list1[i])  # adding values to the left half
    for j in range(mid, n):
        right_half.append(list1[j])  # adding values to the right half
    merge_sort(left_half)
    merge_sort(right_half)
    merge_sort1(left_half, right_half, list1)


"********************************************* bubble sort ************************************************"


def bubble_sort():
    number = int(input("enter the size of list\n"))
    list1 = []
    for i in range(number):
        val = input("enter the elements \n")
        list1.append(val)
    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]

    print(list1)


"******************************************* string insertion *********************************************************"


def string_insertion_sort():
    size = int(input("enter the size \n"))
    list1 = []
    # from range i to size
    for i in range(size):
        val = input("enter the word\n")
        # to insert the words in to the list
        list1.append(val)
    # from range 1 to the length of the list1
    for i in range(1, len(list1)):
        temp = list1[i]
        # j value is one less than i value
        j = i - 1
        while (j >= 0) and (temp <= list1[j]):
            # swapping vales of the list
            list1[j + 1] = list1[j]
            j = j - 1  # j value is 1 less than j
        list1[j + 1] = temp
    print(list1)


"************************************************* permutation **************************************************"


def permut(a, j):
    if j == len(a):
        for i in range(0, len(a)):
            print(a[i], end=" ")
        print()
    else:
        for k in range(j, len(a)):
            temp = a[k]
            a[k] = a[j]
            a[j] = temp
            permut(a, j + 1)
            temp = a[k]
            a[k] = a[j]
            a[j] = temp


"********************************************* string bubble sort *************************************************"


def string_bubble_sort():
    size = int(input("enter the size of list \n"))
    list1 = []
    for i in range(size):
        # adding values to the list
        val = input("enter the elements \n")
        # append() is used to add values
        list1.append(val)

    for i in range(len(list1)):
        for j in range(len(list1) - 1):
            # if condition is true, swapping happens
            if list1[j] > list1[j + 1]:
                # swapping the elements in the list1
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)


"*************************************************** vending machine ***********************************************"


def vending_machine(rupees):
    # enter the rupee notes
    money = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    # initialize note as zero
    note = 0
    for i in range(len(money)):
        # // is used to generate integer value
        if rupees // money[i] > 0:
            print("number of notes in ", money[i], "is ", rupees // money[i])
            note = note + (rupees // money[i])
            rupees = rupees % money[i]
            # reminder is generated and assigned to rupee

    print("number of notes are ", note)


"******************************************** anagram prime ****************************************************"


def get_anagram_prime():
    x = get_prime()

    x = [str(i) for i in x]
    anagram1 = []
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if sorted(x[i]) == sorted(x[j]):
                anagram1.append(x[i])
                anagram1.append(x[j])
    return anagram1


"**************************************************** get prime **********************************************"


def get_prime():
    list = []
    is_prime = True
    for i in range(1001):
        if i == 0 or i == 1:
            continue
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
        if is_prime:
            list.append(i)
    return list


"******************************************** Queued linked list *****************************************"


class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class QueueLinked:
    # This Queue class is used to create Queue.

    front = None

    rear = None

    def __init__(self):

        # This is the constructor of Queue class .

        pass

    def enqueue(self, data):

        # This method is used to insert data in the Queue .

        node = Node(data)

        if self.front is None and self.rear is None:  # If Null

            self.front = node  # Assign Nodes in front and a rear

            self.rear = node

        else:

            self.rear.next = node  # assign node to rear of next

            self.rear = self.rear.next

    def show(self):

        # This method is used to display content of queue .

        if self.front is None:
            print("Linked List  is empty")

            return

        while self.front.next is not None:
            print(self.front.data)

            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):

        # This method is used to delete data from the Queue.
        # data will deleted according to FIFO principle

        temp = self.front  # keep data in a temporary variable for deletion

        self.front = self.front.next

        return temp.data

    def is_empty(self):

        # This method is used to know whether Queue is empty or not.

        if self.front is None:

            return True

        else:

            return False

    def size(self):

        # This method is used to display content of queue.

        size = 1

        traverse = self.front

        if self.front is None:
            return 0

        while traverse.next is not None:
            traverse = traverse.next

            size += 1

        return size


queue1 = QueueLinked()



"********************************************** stack ***************************************************"


class Node:
    def __init__(self, data):

        self.data = data
        self.next = None


class Stacklinked:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        # this block check the linked list

        if self.top == None:
            return True
        else:
            return False

    def push(self, data):

        # this block add the element into stack

        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):

        # this block pop the element one by one

        if self.top is None:
            return "Stack empty"

        element = self.top
        self.top = self.top.next
        return element.data

    def size(self):

        # this block check the size of the linked list

        temp = self.top
        count = 0
        while temp != None:
            count += 1
            temp = temp.next
        return count

    def print(self):

        # this block print the element

        if self.top is None:
            print("Stack is empty!!!")
            return
        current = self.top
        while current != None:
            print(current.data)
            current = current.next


"*************************************************** queue ************************************************"




class Queue:
    """
    This Queue class is used to create Queue.
    """
    front = None
    rear = None

    def __init__(self):
        """
        This is the constructor of Queue class .
        """
        pass

    def enqueue(self, data):

        node = Node(data)

        if self.front is None and self.rear is None:

            self.front = node       # front and rear assign to new node
            self.rear = node

        else:

            self.rear.next = node        # else add element in queue by rear
            self.rear = self.rear.next

    def show(self):
        """
        This method is used to display content of queue .
        """

        if self.front is None:
            print("Queue is empty")     # print if queue is empty
            return

        while self.front.next is not None:
            print(self.front.data)          # print queue data
            self.front = self.front.next

        print(self.front.data)

    def dequeue(self):
        """
        This method is used to delete data from the Queue.
        data will deleted according to FIFO principle
        """
        global temp
        temp = self.front
        self.front = self.front.next        # delete data which is pointed by front pointer
        return temp.data                # return deleted data

    def is_empty(self):
        """
       This method is used to know whether Queue is empty or not.
       """
        if self.front is None:
            return True
        else:
            return False

    def size(self):
        """
        This method is used to display content of queue.
        """

        size = 1
        traverse = self.front
        if self.front is None:      # return 0 if queue is empty
            return 0

        while traverse.next is not None:
            traverse = traverse.next        # traverse till last element and count size
            size += 1
        return size


queue = Queue()
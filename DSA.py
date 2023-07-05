# define students array
students = ["Muskan Kamran", "M.Umair Khan", "Bilal Ahmad Khan Durrani", "M.Hamza Noor", "M.Hamza", "M.Ihtesham Khan", "Rehbar Ghalib", "Yasir Mukhtiar", "Javid Khan", "Hassan Rafey", "Mudassir Khan", "M.Aamir Khan", "Mehmood Ul Hassan", "Ahmad Khan", "Mubashir Ihtisham", "Ata-ur-Rehman", "Salah ud Din", "Osama Hidayat", "Muhib ullah", "Aakif Ullah Khan", "Atta Ur Rehman", "Sikandar Azam", "Siham ullah Shah", "Sharif Ullah", "Tawab Khan", "Rizwan Ullah", "Hamid Riaz Khattack", "Danyal Younas", "Mamoon Shah", "Afnan Zia", "Burhan Ud Din", "Rooh Ullah", "Hubaib Khan", "Atif Nawaz", "Maaz Khan", "Ahmad Fazil", "M.Talha", "Noman Khan", "Safeer ullah Khan", "M. Nasir Khan", "Mutahir", "M.Roman Khan", "Waqas Khan", "Manzoor Ahmad", "Hamza Siddique"]

# display names of all students
print("===Names of all students:===\n", ", ".join(students))

my_name = "M.Ihtesham Khan"

# function for linear search
def Linear_Search(arr, name):
    for i in range(len(arr)):
        if name == arr[i]:
            return i
index = Linear_Search(students, my_name)
print(f"{my_name} found at index {index} using linear search. after {index} iterations")


# binary Search function
def Binary_search(arr, name):
    iterations = 0
    arr = sorted(arr)
    low = 0
    high = len(arr) - 1
    while low <= high:
        iterations +=1
        mid = (low + high) // 2
        if arr[mid] == name:
            return [mid, iterations]
        if arr[mid] < name:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# search for my name using binary search
info = Binary_search(students,my_name)

if info[0] != -1:
    print(f"{my_name} found at index {info[0]} using binary search. after {info[1]} iterations")
else:
    print('sorry your name is not in the array.')
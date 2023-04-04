# define students array
students = ["Muskan Kamran", "M.Umair Khan", "Bilal Ahmad Khan Durrani", "M.Hamza Noor", "M.Hamza", "M.Ihtesham Khan", "Rehbar Ghalib", "Yasir Mukhtiar", "Javid Khan", "Hassan Rafey", "Mudassir Khan", "M.Aamir Khan", "Mehmood Ul Hassan", "Ahmad Khan", "Mubashir Ihtisham", "Ata-ur-Rehman", "Salah ud Din", "Osama Hidayat", "Muhib ullah", "Aakif Ullah Khan", "Atta Ur Rehman", "Sikandar Azam", "Siham ullah Shah", "Sharif Ullah", "Tawab Khan", "Rizwan Ullah", "Hamid Riaz Khattack", "Danyal Younas", "Mamoon Shah", "Afnan Zia", "Burhan Ud Din", "Rooh Ullah", "Hubaib Khan", "Atif Nawaz", "Maaz Khan", "Ahmad Fazil", "M.Talha", "Noman Khan", "Safeer ullah Khan", "M. Nasir Khan", "Mutahir", "M.Roman Khan", "Waqas Khan", "Manzoor Ahmad", "Hamza Siddique"]

# display names of all students
print("Names of all students:")
print(", ".join(students))

# search for my name using linear search
my_name = "M.Ihtesham Khan"
index = -1
for i in range(len(students)):
    if students[i] == my_name:
        index = i
        break
print(f"{my_name} found at index {index} using linear search.")

# search for my name using binary search
students.sort()
index = -1
low = 0
high = len(students) - 1
while low <= high:
    mid = (low + high) // 2
    if students[mid] == my_name:
        index = mid
        break
    elif students[mid] < my_name:
        low = mid + 1
    else:
        high = mid - 1
print(f"{my_name} found at index {index} using binary search.")

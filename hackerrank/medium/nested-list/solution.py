if __name__ == '__main__':
    students = []
    s = set()
    st = list()
    sec_low_list = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    # print(students)
    for name,scores in students:
        s.add(scores)
    st = list(s)
    st.sort()
    second_low = float(st[1])
    for name,score in students:
        if score==second_low:
            sec_low_list.append(name)
            # print(sec_low_list)
    sec_low_list.sort()
    # print(sec_low_list)
    
    for i in sec_low_list:
        print(i)
        

        

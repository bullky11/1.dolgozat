def stadionok():
    stadion_list=[]
    city_list=[]
    team_number=[]
    first_match=[]
    last_match=[]
    f= open("stadionok.txt","r", encoding="utf-8")
    stadions=f.readlines()

    i=1
    while i<len(stadions):
        list=stadions[i].strip().split(";")
        stadion_list.append(list[0])
        city_list.append(list[1])
        team_number.append(list[2])
        first_match.append(list[3])
        last_match.append(list[4])
        i+=1
    print(stadion_list)
    print(city_list)
    print(team_number)
    print(first_match)
    print(last_match)
    print(len(team_number))
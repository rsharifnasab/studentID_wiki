import webbrowser
n_db = ["۰","۱","۲","۳","۴","۵","۶","۷","۸","۹","۱۰","۱۱","۱۲","۱۳","۱۴","۱۵","۱۶","۱۷","۱۸","۱۹","۲۰","۲۱","۲۲","۲۳","۲۴","۲۵","۲۶","۲۷","۲۸","۲۹","۳۰","۳۱"];
m_db = ["","فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]


day = input("hello\nwelcome to this program\npls enter your student id :\n");
day = int(day)%365;
print(day,"th day of year");
tool_m = 31;
mounth = "";
if day == 0 :
    print ("im so sorry but we have a problem :)\nso i changed your day to 29 esfand");
    day = 365;

for i in range(1,13):
    if i>6 : tool_m = 30;
    if day <= tool_m :
        mounth = i;
        break;
    day-=tool_m;

print(day,"th of ", mounth,"th mounth of the year")
mounth = m_db[mounth]
s= "http://fa.wikipedia.org/wiki/"+n_db[day]+"_"+str(mounth);
inp = input("do you want to know more about that day ? \n y or n? ")
if (inp[0]=='y' or inp[0]=='Y'): webbrowser.open(s)

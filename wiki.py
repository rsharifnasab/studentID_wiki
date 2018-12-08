import subprocess
import webbrowser
def copy2clip(txt):
    cmd = 'echo '+txt.strip()+'|clip'
    try:
        return subprocess.check_call(cmd,shell=True)
    except:
        pass

day = input("helo\nwelcome to this program\npls enter your studetn id :\n");
day = int(day)%365;
print(day,"th day of year");
n_db = ["۰","۱","۲","۳","۴","۵","۶","۷","۸","۹","۱۰","۱۱","۱۲","۱۳","۱۴","۱۵","۱۶","۱۷","۱۸","۱۹","۲۰","۲۱","۲۲","۲۳","۲۴","۲۵","۲۶","۲۷","۲۸","۲۹","۳۰","۳۱"];
m_db = ["","فروردین","اردیبهشت","خرداد","تیر","مرداد","شهریور","مهر","آبان","آذر","دی","بهمن","اسفند"]
tool_m = 31;
mounth = "";
if day == 0 :
    print ("im so sorry but we have a problem :)\nso i changed your day to 29 esfand");
    day = 365;
    #exit()
for i in range(1,13):
    if i>6 : tool_m = 30;
#    if i==12 : tool_m = 29;
    if day <= tool_m :
        mounth = i;
        break;
    day-=tool_m;

print(day,"th of ", mounth,"th mounth of the year")
mounth = m_db[mounth]
#https://fa.wikipedia.org/wiki/%DB%B3_%D8%B4%D9%87%D8%B1%DB%8C%D9%88%D8%B1
s= "http://fa.wikipedia.org/wiki/"+n_db[day]+"_"+str(mounth);
#copy2clip(s)
inp = input("do you want to know more about that day ? \n y or n? ")
if (inp[0]=='y' or inp[0]=='Y'): webbrowser.open(s)

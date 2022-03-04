class Time:
    def __init__(the_object, h, m, s):
        the_object.hour = h 
        the_object.minute = m 
        the_object.second = s 

    def __repr__(the_object):
        return f"{the_object.hour}:{the_object.minute}:{the_object.second}"

    @classmethod
    def add_time(cls, time1, time2):
        sec = time1.second + time2.second
        carry = 0
        if(sec > 60):
            carry = sec // 60
            sec = sec % 60
        min = time1.minute + time2.minute + carry
        carry = 0
        if(min > 60):
            carry = min // 60
            min = min % 60
        hr = time1.hour + time2.hour + carry
        if(hr > 24):
            hr = hr % 24
        time3 = Time(hr, min, sec)
        print(time3)

t1 = Time(12,45,50)
t2 = Time(10,35,45)
Time.add_time(t1,t2)
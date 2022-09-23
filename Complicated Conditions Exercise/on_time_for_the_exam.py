hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

time_exam_minutes = hour_exam * 60 + minute_exam
time_arrive_minutes = hour_arrive * 60 + minute_arrive
diff = abs(time_exam_minutes - time_arrive_minutes)

if time_exam_minutes < time_arrive_minutes:
    print("Late")
    if diff < 60:
        print(f"{diff} minutes after the start")
    else:
        hours_diff = diff // 60
        minutes_diff = diff % 60
        if minutes_diff < 10:
            print(f"{hours_diff}:0{minutes_diff} hours after the start")
        else:
            print(f"{hours_diff}:{minutes_diff} hours after the start")
elif time_exam_minutes == time_arrive_minutes or diff <= 30:
    if time_exam_minutes == time_arrive_minutes:
        print("On Time")
    else:
        print("On Time")
        print(f"{diff} minutes before the start")
elif time_exam_minutes > time_arrive_minutes:
    print("Early")
    if diff < 60:
        print(f"{diff} minutes before the start")
    else:
        hours_diff = diff // 60
        minutes_diff = diff % 60
        if minutes_diff < 10:
            print(f"{hours_diff}:0{minutes_diff} hours before the start")
        else:
            print(f"{hours_diff}:{minutes_diff} hours before the start")



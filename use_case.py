from send_email import send_email

#do some time intensive work
i = 1
for _ in range(100000):
    i += i

#send yourself an email when this work is finished
send_email('your_email@mail.com', 'Work finished', 'Check it out!')


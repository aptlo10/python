class Qustoin:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "what is the capital of egypt?\n(a) cairo\n(b)alexandra \n(c)giza \n\n",
    "What is result of 5*5?\n(a) 30\n(b)25 \n(c)30 \n\n",
    " how is best player?\n(a) tika\n(b)salah\n(c)misse \n\n"
]

qus = [
    Qustoin(question_prompts[0], "a"),
    Qustoin(question_prompts[1], "b"),
    Qustoin(question_prompts[2], "c"),
]


def run_test(qustoins):
    score = 0
    for qustoins in qus:
        answer = raw_input(qustoins.prompt)
        if answer == qustoins.answer:
            score += 1
    print " your score is " + str(score) + "/" + str(len(qus))
    if score >= 2:
        begin = raw_input("your score is " + str(score) + " " + "and good" + " " + "would you try again \n")
        if begin == "yes":
            run_test(qus)
        elif begin in "no":
            print "good bay"
    if score <= 1:
        begin = raw_input("your score is " + str(score) + " " + "and bad" + " " + "would you try again \n")
        if begin == "yes":
            run_test(qus)
        else:
            print "good bay"


def lenier_regresion():
    x = raw_input("input_x:")
    xx = x.split()
    xxx = map(int, xx)
    list_x = [i ** 2 for i in xxx]
    sum_xxx = sum(xxx)
    sum_listt_x = sum(list_x)
    y = raw_input("input_y:")
    yy = y.split()
    yyy = map(int, yy)
    list_y = [i ** 2 for i in yyy]
    sum_yy = sum(yyy)
    sum_listt_y = sum(list_y)
    x_m_y = [xxx * yyy for xxx, yyy in zip(xxx, yyy)]
    sum_xy = sum(x_m_y)
    a_hat = ((sum_xxx * sum_yy) - (len(list_x) * sum_xy)) / float((sum_xxx ** 2) - (len(list_x) * sum_listt_x))
    b_hat = ((sum_xxx * sum_xy) - (sum_yy * sum_listt_x)) / float((sum_xxx ** 2) - (len(list_x) * sum_listt_x))
    std_x = ((sum_listt_x - (1.0 / len(list_x) * (sum_xxx ** 2))) / (len(list_x) - 1)) ** 0.5
    std_y = ((sum_listt_y - (1.0 / len(list_x) * (sum_xxx ** 2))) / (len(list_x) - 1)) ** 0.5
    r_sequare = (std_x / std_y) * a_hat

    print"input y to pridect"
    k = raw_input()
    y = a_hat * float(k) + b_hat
    print "y prediction is =", y
    if r_sequare >= 0.8:
        print"strong r square =", r_sequare
    else:
        print"weak rsquare", r_sequare
    while True:
        begin = raw_input("would you want to try again \n")
        if begin in "yes":
            lenier_regresion()
            break
        elif begin in "len":
            lenier_regresion()
            break
        elif begin in "no":
            print "good bay"
            break
        else:
            print 'Invalid input.'


while True:
    begin = raw_input(
        "would you begin quize\n type quize to begin quiz \n type len to begin lenier_regresion program \n type no to close \n")
    if begin in "quize":
        run_test(qus)
        break
    elif begin in "len":
        lenier_regresion()
        break
    elif begin in "no":
        print "good bay"
        break
    else:
        print 'Invalid input.'








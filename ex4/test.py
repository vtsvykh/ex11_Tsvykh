import schedule


def read_subject(filename):
    with open(filename, 'r', encoding='utf_8') as file:
        lines = file.read().splitlines()

        subjects = []
        for line in lines:

            info = [elem.lstrip() for elem in line.split(',')]
            info = info[1:]
            for pair in info:
                pair = pair.split('_')
            subject = schedule.Subject(pair[0], pair[1], pair[2], pair[3])
            subjects.append(subject)

        return subjects


def print_schedule(group):
    for day in group.schedule:
        print(f'{day}:\n')
        for course in group.schedule[day]:
            course = course.split('_')
            course[1] = schedule.Subject(course[0], course[1], course[2], course[3])
            print(course[1])
        print()


student_1 = schedule.Student('Цвых Виктория', 222218, 22704_2)
group_1 = schedule.Group(2022, 'Бакалавриат', 'Экономический факультет',
                         'Бизнес-информатика', 22704_2, 25)
group_1.set_schedule('22704_2.txt')
print(80 * '-')
course = group_1.get_course()
print(f'Для студента {student_1.name}, обучаещегося на {course} курсе,\n'
      f'Факультет: {group_1.faculty},\n'
      f'Направление: {group_1.direction},\n'
      f'Действует расписание:\n')
print_schedule(group_1)

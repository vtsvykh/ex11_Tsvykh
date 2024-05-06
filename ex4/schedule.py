from datetime import datetime


class Student:
    """
    Class of student.

    Args:
        name (str): name of students
        id (int): credit book number
        group(int): group number

    """

    def __init__(self, name, id, group):
        """

        :param name (str): name of students
        :param id (int): credit book number
        :param group (int): group number
        """
        self.name = name
        self.id = id
        self.group = group

    def __str__(self):
        return f'Студент {self.name} с номером зачетной книжки {self.id} в группе {self.group}'

    def __repr__(self):
        return self.__str__()


class Group:
    """
    Class of group.

    Args:
        year_adm (int): year of enrolment
        lvl_edct (str): level of education
        faculty (str): faculty
        direction (str): direction
        num_group (int): group number
        num_ppl(int): number of people
        schedule (dict): dictionary of schedule
    """

    def __init__(self, year_adm, lvl_edct, faculty, direction, num_group, num_ppl):
        """
        The function initialises an instance of the molecule class.
        :param year_adm (int): year of enrolment
        :param lvl_edct (str): level of education
        :param faculty (str): faculty
        :param direction (str): direction
        :param num_group (int): group number
        :param num_ppl(int): number of people
        """
        self.year_adm = int(year_adm)
        self.lvl_edct = lvl_edct
        self.faculty = faculty
        self.direction = direction
        self.num_group = num_group
        self.num_ppl = int(num_ppl)
        self.schedule = {}

    def get_course(self):
        """
        Function for get course of group.
        :return: number of course
        """
        current_year = datetime.now().year
        if current_year - self.year_adm != 0:
            return current_year - self.year_adm
        return 1

    def set_schedule(self, filename):
        """
        Function set schedule.

        :param filename(txt): file with schedule
        """
        with open(filename, 'r', encoding='utf_8') as file:
            lines = file.read().splitlines()

            for line in lines:
                line = [elem.lstrip() for elem in line.split(',')]
                if line[0] == 'Понедельник':
                    self.schedule['Понедельник'] = line[1:]
                elif line[0] == 'Вторник':
                    self.schedule['Вторник'] = line[1:]
                elif line[0] == 'Среда':
                    self.schedule['Среда'] = line[1:]
                elif line[0] == 'Четверг':
                    self.schedule['Четверг'] = line[1:]
                elif line[0] == 'Пятница':
                    self.schedule['Пятница'] = line[1:]
                elif line[0] == 'Суббота':
                    self.schedule['Суббота'] = line[1:]

    def __str__(self):
        return f'{self.schedule}'

    def __repr__(self):
        return self.__str__()


class Subject:
    """
    Class of subject.

    Args:
        time (str): time of subject
        name (str): name of subject
        lecturer (str): name of lecturer
        auditories (int): number of auditorie
    """

    def __init__(self, time, name, lecturer, auditories):
        """
        The function initialises an instance of the molecule class.
        :param time (str): time of subject
        :param name (str): name of subject
        :param lecturer (str): name of lecturer
        :param auditories (int): number of auditorie
        """
        self.name = name
        self.lecturer = lecturer
        self.auditories = auditories
        self.time = time

    def __str__(self):
        return f'{self.time} {self.name} {self.lecturer} {self.auditories}'

    def __repr__(self):
        return self.__str__()

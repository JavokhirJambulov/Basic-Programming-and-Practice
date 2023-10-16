import os
import pickle

gradelist = []


def load_grades():
    loaded_grades = []
    if os.path.exists('grades.pickle'):
        with open(' grade.pickle', 'rb') as f:
            loaded_grades = pickle.load(f)

    else:
        grades = open('grades.txt', 'x')
        loaded_grades = grades.read()
        grades.close()
    return loaded_grades


def save_grades(saving_grades):
    with open('grades.pickle', 'wb') as f:
    pickle.dump(my_file, f)


def calculate_avg():


gradelist = load_grades()
save_grades(gradelist)
calculate_avg(gradelist)

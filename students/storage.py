from functools import lru_cache

students_list = []

@lru_cache()
def get_student_list():
    return students_list
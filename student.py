#!/usr/bin/python3
# -*- coding: utf-8 -*


class Student(object):
    def __init__(self, name, gender):
        self._name = name
        self.gender = gender

    def getName(self):
        return self._name


student = Student('Tom', 'male')
print(student.getName())

"""
CP1404/CP5632 Practical
project management class
Estimate - 90 minutes
"""


class Project:

    def __init__(self, name="", start_date=0, priority=0, cost=0.0, completion=0.0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):

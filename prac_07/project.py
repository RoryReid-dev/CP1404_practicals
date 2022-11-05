"""
CP1404/CP5632 Practical
project management class
Estimate - 90 minutes
"""


class Project:
    """Class to represent project"""

    def __init__(self, name="", start_date="", priority=0, cost=0.0, completion=0.0):
        """Initialise project class"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        """string method for project class"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, " \
               f"completion : {self.completion}%"

    def __repr__(self):
        """repr method for project class"""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost}, " \
               f"completion : {self.completion}%"
from flask import jsonify
meetups = []
questions  = []

class meetup:

    def __init__(self, title, venue, start_time, end_time):
        self.id = len(meetups)+1
        self.title = title
        self.venue = venue
        self.start_time = start_time
        self.end_time = end_time

    def store_meetup(self):
        meetups.append(self)

    def all_meetups():
        return [jsoner(meetup) for meetup in meetups]

    def get_one(m_id)   :
        return [meetup.jsoner(meetup)] for meetup in meetups if meetup.id == m_id]

    def jsoner(meetup):
        return jsonify(self.id = len(meetups)+1
        self.title = title
        self.venue = venue
        self.start_time = start_time
        self.end_time = end_time)

class question:
    def __init__(self, author, title, body, votes):
        self.id = len(questions) + 1
        self.author = author
        self.title = title
        self.body = body
        self.votes = votes
    
    def store_questions:
        question.append(self)

    def all-questions():
        rerturn [jsoner(question) for question in quetions]

    def jsoner(question):
        return jsonify(
        def __init__(self, author, title, body, votes):
        self.id = len(questions) + 1
        self.author = author
        self.title = title
        self.body = body
        self.votes = votes           
        )



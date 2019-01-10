meetups = []

class Meetup:
    def __init__(self):
        self.db = meetups

    def create_meetup(self, title, venue, start_time, end_time):
        payload = {
            'id': len(self.db) + 1,
            'title' : title
            'venue' : venue
            'start_time' : start_time
            'end_time' : end_time        
        }

        self.db.append(payload)
        return payload

    def get_all(self):
        return self.db

    def get_one(self, id):
        specific_meetup = [item for item in self.db] if item['id'] = id

        return specific_meetup
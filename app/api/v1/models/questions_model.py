questions = []

class QuestionsModel:
    def __init__(self):
        self.db = questions

    def add_question(self, title, author, body, votes):
        payload = {
            'id': len(self.db) + 1,
            'title' : title,
            'body' : body,
            'votes' : votes
        }   

        self.db.append(payload)
        return payload

    def get_all(self):
        return self.db

    def get_one(self,id):
        specific_question = [item for item in self.db] if item['id'] = id
        return specific_question

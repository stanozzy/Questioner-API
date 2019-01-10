rspvs = []


class RspvsModel:

    def __init__(self):
        self.db = rspvs

    def create_rspv(self, meetup, topic, status):
        payload = {
            "id": len(self.db) + 1,
            "meetup": meetup,
            "topic": topic,
            "status": status,
        }
        self.db.append(payload)
        return payload

    def get_all_rspvs(self):
        """Retrieves all upcoming rspvs"""
        return self.db

    def get_a_specific_rspv(self, id):
        """Retrieves a specific rspv"""
        specific_rspv = item for item in self.db] if item['id'] = id
        return rspv
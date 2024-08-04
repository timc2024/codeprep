from pymongo import MongoClient
from bson import ObjectId
from config import MONGODB_URI

class Database:
    def __init__(self):
        self.client = MongoClient(MONGODB_URI)
        self.db = self.client['prompt']
        self.prompts_collection = self.db['prompt']

    def get_all_prompts(self):
        return list(self.prompts_collection.find())

    def get_prompt(self, prompt_id):
        return self.prompts_collection.find_one({'_id': ObjectId(prompt_id)})

    def add_prompt(self, tag, content):
        return self.prompts_collection.insert_one({
            'tag': tag,
            'content': content
        }).inserted_id

    def update_prompt(self, prompt_id, tag, content):
        self.prompts_collection.update_one(
            {'_id': ObjectId(prompt_id)},
            {'$set': {'tag': tag, 'content': content}}
        )

    def delete_prompt(self, prompt_id):
        self.prompts_collection.delete_one({'_id': ObjectId(prompt_id)})

db = Database()
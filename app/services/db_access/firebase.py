import secrets as sc
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from app.services.db_access import DbAccess


class FireBaseDbAccess(DbAccess):

    @staticmethod
    def get_database():
        firestore_key = os.environ.get('FIRESTORE_KEY')
        if firestore_key:
            cred = credentials.Certificate(os.environ.get('FIRESTORE_KEY'))
            firebase_admin.initialize_app(cred)

        else:
            cred = credentials.ApplicationDefault()
            projectId = os.environ.get('GOOGLE_CLOUD_PROJECT')
            firebase_admin.initialize_app(cred, {'projectId': projectId})

        database = firestore.client()
        return database

    
    def save_new_url(self, complete_url):

        database = FireBaseDbAccess.get_db()

        short_test = sc.token_urlsafe(5)[:5]        
        is_new = not self.check_short_url(short_test)        
        while not is_new:
            short_test = sc.token_urlsafe(5)[:5]
            is_new = not self.check_short_url(short_test)
        
        url_ref = database.collection('short_urls')
        url_ref.set({
            'short_url': short_test,
            'complete_url': complete_url
        })

        return short_test

    
    def check_short_url(self, short_url):
        database = FireBaseDbAccess.get_db()
        urls_ref = database.collection('short_urls').where('short_url', '==', short_url).stream()
        if len(urls_ref) > 0:
            to_dict = urls_ref[0].to_dict()
            return to_dict['complete_url']


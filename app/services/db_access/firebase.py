import secrets as sc
import os, traceback
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from app.services.db_access import DbAccess
import app.helpers as helpers


class FireBaseDbAccess(DbAccess):

    def __init__(self):

        firestore_key = os.environ.get('FIRESTORE_KEY')
        if firestore_key:
            cred = credentials.Certificate(os.environ.get('FIRESTORE_KEY'))
            fb_app = firebase_admin.initialize_app(cred)

        else:
            cred = credentials.ApplicationDefault()
            projectId = os.environ.get('GOOGLE_CLOUD_PROJECT')
            fb_app = firebase_admin.initialize_app(cred, {'projectId': projectId})

        database = firestore.client()
        self.db = database
        self.fb_app = fb_app

    
    def save_new_url(self, complete_url):        

        short_test = helpers.create_short_url()        
        is_new = not self.check_short_url(short_test)        
        while not is_new:
            short_test = helpers.create_short_url()            
            is_new = not self.check_short_url(short_test)
        
        url_ref = self.db.collection('short_urls').document()
        url_ref.set({
            'short_url': short_test,
            'complete_url': complete_url,
            'created_at': firestore.SERVER_TIMESTAMP
        })

        return short_test

    
    def check_short_url(self, short_url):
        
        urls_ref = self.db.collection('short_urls').where('short_url', '==', short_url).stream()
        first = next(urls_ref, None)
        if first:
            to_dict = first.to_dict()
            return to_dict['complete_url']
        



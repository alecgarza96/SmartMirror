from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


class GoogleCalendar():

    def __init__(self):
        self.creds = None
        self.events = None
        self.SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

    def _getCreds(self):
        if os.path.exists('token.json'):
            self.creds = Credentials.from_authorized_user_file('token.json', self.SCOPES)

    def _userlogin(self):
        if not self.creds or not self.creds.valid:
            if self._checkCredentialsExpired():
                self._refreshCredentials()
            else:
                self._loginPrompt()
            self._saveCredentials()
    
    def _checkCredentialsExpired(self):
        #review docs
        return self.creds and self.creds.expired and self.creds.refresh_token

    def _refreshCredentials(self):
        #review docs
        self.creds.refresh(Request())

    def _loginPrompt(self):
        flow = InstalledAppFlow.from_client_secrets_file(
            'credentials.json', self.SCOPES)
        self.creds = flow.run_local_server(port=0)

    def _saveCredentials(self):
        with open('token.json','w') as token:
            token.write(self.creds.to_json())

    def _makeRequest(self):
        service = build('calendar', 'v3', credentials=self.creds)

        #call the calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' #'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        self.events = events_result.get('items',[])

    def _catchHttpError(self, error):
        print('An error ocurred: %s' % error)
        self.events=[]

    def getEvents(self):
        try:
            self._makeRequest()
            """
            # Prints the start and name of the next 10 events
            for event in self.events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                print(start, event['summary'])
            """
        except HttpError as error:
            self._catchHttpError(error)

        return self.events


from google_auth_oauthlib import flow
import io
import os
import oauth2client
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types
# import logging
import google.cloud.storage as gcs
# import webapp2
# from google.cloud import appengine
# from google.cloud import app_identity

buckname = 'ace6280'


def get(self, buckname):
    bucket_name = os.environ.get(buckname,
                                 app_identity.get_default_gcs_bucket_name())

    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Demo GCS Application running from Version: '
                        + os.environ['CURRENT_VERSION_ID'] + '\n')
    self.response.write('Using bucket name: ' + bucket_name + '\n\n')


def read_file(self, filename):
    self.response.write('Reading the full file contents:\n')
    gcs_file = gcs.open(filename)
    contents = gcs_file.read()
    gcs_file.close()
    var1 = self.response.write(contents)
    return var1


# Trying to get end-user permissions using Google SDK
# TODO: Uncomment the line below to set the `launch_browser` variable.
launch_browser = True

# The `launch_browser` boolean variable indicates if a local server is used
# as the callback URL in the auth flow. A value of `True` is recommended,
# but a local server does not work if accessing the application remotely,
# such as over SSH or from a remote Jupyter notebook.

filename = 'client_secrets.json'

appflow = flow.InstalledAppFlow.from_client_secrets_file(filename, scopes = 'https://speech.googleapis.com/v1/speech:recognize')
if launch_browser:
    appflow.run_local_server()
else:
    appflow.run_console()

credentials = appflow.credentials
# Instantiates a client
client = speech.SpeechClient()

# __file__ = 'gs://audheart/heartbeat-01a.mp3'
# __file__ = '/home/mehta_himanshi/My-Project-81898/heartbeat-01a.mp3'
# __file__ = 'heartbeat-01a.mp3'

# The name of the audio file to transcribe
# file_name = os.path.join(os.path.dirname(
#    '/home/mehta_himanshi/'),'My-Project-81898/', __file__)

file_name = '/home/mehta_himanshi/My-Project-81898/heartbeat-01a.mp3'
# Loads the audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,  # LINEAR16 change to MP3: throws error
    sample_rate_hertz=16000,
    language_code='en-US')

# Detects speech in the audio file
response = client.recognize(config, audio)

for result in response.results:
    print('Transcript: {}'.format(result.alternatives[0].transcript))

import sys
import os
import requests
import json

errors = __import__('errors', globals(), locals(), [], sys._addon_import_level_base)
version = __import__('version', globals(), locals(), [], sys._addon_import_level_base)
constants = __import__('constants', globals(), locals(), [], sys._addon_import_level_base)
logging_utils = __import__('logging_utils', globals(), locals(), [], sys._addon_import_level_base)
logger = logging_utils.get_child_logger(__name__)

if hasattr(sys, '_sentry_crash_reporting'):
    import sentry_sdk

class CloudLanguageTools():
    def __init__(self):
        self.base_url = os.environ.get('ANKI_LANGUAGE_TOOLS_BASE_URL', 'https://cloudlanguagetools-api.vocab.ai')
        self.use_vocabai_api = os.environ.get('ANKI_LANGUAGE_TOOLS_VOCABAI_API', 'false').lower() == 'true'

    def configure(self, api_key):
        self.api_key = api_key

    def get_request_headers(self):
        if self.use_vocabai_api:
            return {
                'Authorization': f'Api-Key {self.api_key}',
                'User-Agent': f'anki-hyper-tts/{version.ANKI_HYPER_TTS_VERSION}'}
        else:
            return {
                'api_key': self.api_key, 
                'client': 'hypertts', 
                'client_version': version.ANKI_HYPER_TTS_VERSION,
                'User-Agent': f'anki-hyper-tts/{version.ANKI_HYPER_TTS_VERSION}'}

    def get_tts_audio(self, source_text, voice, options, audio_request_context):
        if hasattr(sys, '_sentry_crash_reporting'):
            sentry_sdk.set_user({"id": f'api_key:{self.api_key}'})
            sentry_sdk.set_context("user", {
                "api_key": self.api_key,
            })

        # query cloud language tools API
        if self.use_vocabai_api:
            url_path = '/audio'
        else:
            url_path = '/audio_v2'
        full_url = self.base_url + url_path
        data = {
            'text': source_text,
            'service': voice.service.name,
            'request_mode': audio_request_context.get_request_mode().name,
            'language_code': voice.language.lang.name,
            'voice_key': voice.voice_key,
            'options': options
        }
        logger.info(f'request url: {full_url}, data: {data}')
        response = requests.post(full_url, json=data, headers=self.get_request_headers(),
            timeout=constants.RequestTimeout)

        if response.status_code == 200:
            return response.content
        elif response.status_code == 404:
            raise errors.AudioNotFoundError(source_text, voice)
        else:
            error_message = f"Status code: {response.status_code} ({response.content})"
            raise errors.RequestError(source_text, voice, error_message)    

    def account_info(self, api_key):
        response = requests.get(self.base_url + '/account', headers={'api_key': api_key})
        data = json.loads(response.content)
        return data

    def request_trial_key(self, email):
        logger.info(f'requesting trial key for email {email}')
        response = requests.post(self.base_url + '/request_trial_key', json={'email': email})
        data = json.loads(response.content)
        logger.info(f'retrieved {data}')
        return data        
def transcribe_gcs(gcs_uri, timeout=1000):
    """Asynchronously transcribes the audio file specified by the gcs_uri."""
    import io
    import os
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    import google.cloud.storage as gcs
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u'Transcript: {}'.format(result.alternatives[0].transcript))
        print('Confidence: {}'.format(result.alternatives[0].confidence))

# InvalidArgument: 400 sample_rate_hertz (16000) in RecognitionConfig must either be unspecified or match the value in the FLAC header (8000).
# https://www.zamzar.com/uploadComplete.php?convertFile=mp3&to=flac&session=58ac9390e7bdcb6720e297b91c1bb6d&email=false&tcs=Z86
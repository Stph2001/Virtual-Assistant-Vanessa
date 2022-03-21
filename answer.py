def Change_Language(r, audio):
    record = r.recognize_google(audio,language="es-PE")
    record = record.lower()
    return record

def Answer(r, source, type=1, seconds = 2):
    print('Listening...')
    if type == 1:
        audio = r.listen(source)
    else:
        audio = r.record(source, duration=seconds)
    try:
        record = Change_Language(r, audio)
        print(record)
        return r,  source, record
    except Exception:
        return r, source, ' '


import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    text_in = req.params.get('text')
    if not text_in:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            text_in = req_body.get('text')

    if text_in:
        return func.HttpResponse(f"Words frequency: {freq_words(text_in)}")
    else:
        return func.HttpResponse(
             "This Serverless function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )


def freq_words(text):
    text = str(text).lower()
    word_list = text.split(' ')
    out = {}
    for word in word_list:
        if word not in out:
            out[word] = 1
        else:
            tmp = int(out[word])
            out[word] = tmp + 1
    return out
import json
import os

from flask import Flask, jsonify, request
from gensim.summarization import summarize
import git

from .final import get_answer, construct_graph
from .extraction import parse_docs
from .utils import get_abs_path

app = Flask(__name__)


@app.route('/update')
def update_docs():
    if 'coala' in os.listdir(get_abs_path('')):
        git.Repo(get_abs_path('coala')).remote('origin').update()
    else:
        git.Repo.clone_from('https://github.com/coala/coala.git',
                            get_abs_path('coala'))


update_docs()

DATA = parse_docs()
GRAPH = construct_graph(DATA)


@app.route('/answer')
def serve_answer():
    global GRAPH
    return jsonify(list(get_answer(request.args.get('question'), GRAPH)))


@app.route('/summarize')
def serve_summary():
    try:
        summary = summarize(request.args.get('text'))
    except ValueError:
        summary = request.args.get('text')
    return jsonify({'res': summarize(request.args.get('text'))})

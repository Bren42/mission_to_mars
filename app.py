#import dependencies
from flask import Flask, render_template,redirect, url_for
from flask_pymongo import PyMongo
from bs4 import BeautifulSoup as bs
import scraping



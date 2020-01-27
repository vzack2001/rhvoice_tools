#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import subprocess
import configparser
from os.path import exists as path_exists
from os.path import expanduser
from rhvoice_preprocessing import text_prepare


def rhvoice_say(args):
    if len(args) > 1:
        """
        Чтение текста RHVocie с предварительнгой обработкой текста.
        """
        txt = text_prepare(args[1])        # предварительная подготовка текста

        # открываем файл конфигурации
        file_name = expanduser("~") + '/.rhvoice_say.conf'
        config = configparser.ConfigParser()
        if not path_exists(file_name):
            # если файл отсутствует, создаем новый со стандартными настройками
            config['Settings'] = {'use_speech_dispatcher': 'False',
                                  'voice': 'Aleksandr+Alan'}
            with open(file_name, 'w') as configfile:
                config.write(configfile)
        config.read(file_name)
        settings = config['Settings']
        use_SD = settings.getboolean('use_speech_dispatcher')
        voice = settings.get('voice')

        if use_SD:
            # -e, --pipe-mode (Pipe from stdin to stdout plus Speech Dispatcher)
            # -w, --wait (Wait till the message is spoken or discarded)
            # -y, --synthesis-voice (Set the synthesis voice)
            p = subprocess.Popen(['spd-say', "-e", "-w", "-y" + voice],
                                 stdin=subprocess.PIPE)
        else:
            # -p <spec>, --profile <spec> (voice profile)
            p = subprocess.Popen(['RHVoice-test', "-p " + voice],
                                 stdin=subprocess.PIPE)
        p.communicate(txt.encode('utf-8'))
    else:
        print('Нет текста для чтения...')

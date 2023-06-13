#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import secrets

__author__ = 'Jonatan Morales'
__version__ = '1.0.0a'

# Logging
logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# "apuesta" y "reintegro"
apuesta = []
reintegro = 0

while len(apuesta) < 6:
    number = secrets.randbelow(50)
    if number !=0 and number not in apuesta:
        apuesta.append(number)

while reintegro == 0:
    number = secrets.randbelow(10)
    if number != 0:
        reintegro = number

log.info("Apuesta = %s" % apuesta)
log.info("Reintegro = %s" % reintegro)

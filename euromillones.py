#! /usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Jonatan Morales'
__version__ = '1.0.0'

import logging
import secrets

# Logging
logging.basicConfig(format='%(message)s')
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

# "apuesta" y "estrellas" lists
apuesta = []
estrellas = []

while len(apuesta) < 5:
    number = secrets.randbelow(50)
    if number !=0 and number not in apuesta:
        apuesta.append(number)

while len(estrellas) < 2:
    number = secrets.randbelow(12)
    if number != 0 and number not in estrellas:
        estrellas.append(number)

log.info("Apuesta = %s" % apuesta)
log.info("Estrellas = %s" % estrellas)

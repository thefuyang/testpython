#!/usr/bin/env python
# coding=utf-8
import os
L = ['Hello', 'World', 18, 'Apple', None]
A = [s for s in L if isinstance(s, str)]
print A
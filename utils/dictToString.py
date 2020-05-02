#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictToString():

    def dictToStr(self, data):
        lista = []
        for k, v in data.items():
            lista.append(": ".join([k, v]))
            content = ' - '.join(map(str, lista))
        return content

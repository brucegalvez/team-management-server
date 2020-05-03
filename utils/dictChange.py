#!/usr/bin/env python
# -*- coding: utf-8 -*-


class DictChange():

    def dictToStr(self, data):
        content = ' - '.join(map(str, self.dictToList(data)))
        return content

    def dictToList(self, data):
        lista = []
        for k, v in data.items():
            lista.append(": ". join([k, v]))
        return lista

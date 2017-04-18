# -*- coding: utf-8 -*-
__author__ = 'Vit'

import email
import quopri

if __name__ == "__main__":
    fle = 'files/Message14924067930000000028.eml'
    with open(fle) as f:
        msg=email.message_from_file(f)
        walk=msg.walk()
        part1=walk.__next__().as_string()
        print(part1)
        part=walk.__next__().as_string()
        # print(part)

        # print(quopri.decodestring(part).decode())

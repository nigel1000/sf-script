#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/17

import xml.sax
from learn.library.parse_xml_sax import MovieHandler

xml_str = '''
<collection shelf="New Arrivals">
<movie title="Enemy Behind">
   <type>War, Thriller</type>
   <format>DVD</format>
   <year>2003</year>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Talk about a US-Japan war</description>
</movie>
<movie title="Transformers">
   <type>Anime, Science Fiction</type>
   <format>DVD</format>
   <year>1989</year>
   <rating>R</rating>
   <stars>8</stars>
   <description>A schientific fiction</description>
</movie>
   <movie title="Trigun">
   <type>Anime, Action</type>
   <format>DVD</format>
   <episodes>4</episodes>
   <rating>PG</rating>
   <stars>10</stars>
   <description>Vash the Stampede!</description>
</movie>
<movie title="Ishtar">
   <type>Comedy</type>
   <format>VHS</format>
   <rating>PG</rating>
   <stars>2</stars>
   <description>Viewable boredom</description>
</movie>
</collection>
'''

# # 创建一个 XMLReader
# parser = xml.sax.make_parser()
# # 关闭命名空间
# parser.setFeature(xml.sax.handler.feature_namespaces, 0)
# # 重写 ContextHandler
# Handler = MovieHandler()
# parser.setContentHandler(Handler)
# parser.parse(file_path)

if __name__ == '__main__':
    xml.sax.parseString(xml_str, MovieHandler())

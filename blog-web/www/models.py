#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 2018/6/30


from www.orm import Model, StringField, BooleanField, FloatField, TextField
import time
import uuid
import asyncio
import www.orm as orm


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    email = StringField(ddl='varchar(50)')
    passwd = StringField(ddl='varchar(50)')
    admin = BooleanField()
    name = StringField(ddl='varchar(50)')
    image = StringField(ddl='varchar(500)')
    created_at = FloatField(default=time.time)


class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)


class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)


if __name__ == '__main__':
    async def test():
        await orm.create_pool(loop, user='root', password='#/d5)anzaVlN', db='blog')
        u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
        await u.save()


    async def show():
        users = await User.findAll()
        print(users)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())
    loop.run_until_complete(show())
    # loop.close()

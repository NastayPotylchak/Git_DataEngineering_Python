from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Table

Base = declarative_base()


class IdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class NameMixin:
    name = Column(String, nullable=False)


class UrlMixin:
    url = Column(String, nullable=False, unique=True)


tag_post = Table('Tag_Post',
                 Base.metadata,
                 Column('post_id', Integer, ForeignKey('Post.id')),
                 Column('tag_id', Integer, ForeignKey('Tag.id'))
                 )


class Post(Base, IdMixin, UrlMixin):
    __tablename__ = 'Post'
    title = Column(String, nullable=False)
    author_id = Column(Integer, ForeignKey('Author.id'))
    author = relationship('Author')
    tags = relationship('Tag', secondary=tag_post)


class Author(Base, IdMixin, NameMixin, UrlMixin):
    __tablename__ = 'Author'
    posts = relationship(Post)


class Tag(Base, IdMixin, NameMixin, UrlMixin):
    __tablename__ = 'Tag'
    posts = relationship('Post', secondary=tag_post)

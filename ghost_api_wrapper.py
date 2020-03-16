import json
import requests

GHOST_CONTENT_API_KEY = ''
BLOG_DOMAIN = ''
VERSION = ''
RESOURCE_URL = lambda target: 'https://{0}/ghost/api/{1}/content/{2}/?key={3}'.format(BLOG_DOMAIN, VERSION, target,
                                                                                      GHOST_CONTENT_API_KEY)

class GHOST_ENDPOINTS:
    ALL_POSTS = RESOURCE_URL('posts')
    POST_BY_ID = RESOURCE_URL('posts/{}')
    POST_BY_SLUG = RESOURCE_URL('posts/slug/{}')
    POST_BY_AUTHOR = RESOURCE_URL('authors')
    POST_BY_AUTHOR_ID = RESOURCE_URL('authors/{}')
    POST_BY_AUTHOR_SLUG = RESOURCE_URL('authors/slug/{}')
    POST_BY_TAGS = RESOURCE_URL('tags')
    POST_BY_TAG_ID = RESOURCE_URL('tags/{}')
    POST_BY_TAG_SLUG = RESOURCE_URL('tags/slug/{}')
    POST_BY_PAGES = RESOURCE_URL('pages')
    POST_BY_PAGE_ID = RESOURCE_URL('pages/{}')
    POST_BY_PAGE_SLUG = RESOURCE_URL('pages/slug/{}')
    SETTINGS = RESOURCE_URL('settings')


class GhostAPIWrapper(object):

    @classmethod
    def getAllPosts(cls):
        res = requests.get(GHOST_ENDPOINTS.ALL_POSTS)
        return json.loads(res.content)

    @classmethod
    def getPostById(cls, postId):
        res = requests.get(GHOST_ENDPOINTS.POST_BY_ID.format(postId))
        return json.loads(res.content)

    @classmethod
    def getPostBySlug(cls, slug):
        res = requests.get(GHOST_ENDPOINTS.POST_BY_SLUG.format(slug))
        return json.loads(res.content)

    @classmethod
    def getSettings(cls):
        res = requests.get(GHOST_ENDPOINTS.SETTINGS)
        return json.loads(res.content)

    @classmethod
    def getPostByAuthor(cls, author):
        res = requests.get(GHOST_ENDPOINTS.POST_BY_AUTHOR.format(author))
        return json.loads(res.content)

    @classmethod
    def getPostByAuthorId(cls, authorId):
        res = requests.get(GHOST_ENDPOINTS.POST_BY_AUTHOR_ID.format(authorId))
        return json.loads(res.content)

    @classmethod
    def getPostByAuthorSlug(cls, authorName):
        res = requests.get(GHOST_ENDPOINTS.POST_BY_AUTHOR_SLUG.format(authorName))
        return json.loads(res.content)


ghostContentApi = GhostAPIWrapper()

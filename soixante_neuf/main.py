import aiohttp 
from datetime import datetime 
from exceptions import SubredditPrivated, SubredditNotFound, RedditError


class Post:

    def __init__(self, data):
        self.subreddit = data['subreddit']
        self.upvotes = data['ups']
        self.url = 'https://reddit.com' + data['permalink']
        self.created_at = datetime.fromtimestamp(data['created_utc'])
        self.media_url = data.get('url_overridden_by_dest')
        self.title = data['title']
        self.nsfw = data['over_18']
        self.pinned = data['pinned']
        
        if self.media_url:
            if any(self.media_url.endswith(s) for s in ['.png', '.gif', '.jpg', '.jpeg']):
                self.is_image = True 
            else:
                self.is_image = False
        else:
            self.is_image = False


async def get_posts(sub, limit: int = 0):
    url = f'https://reddit.com/r/{sub}.json?limit={limit}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 404:
                raise SubredditNotFound(f'The subreddit r/{sub} was not found.', resp.status)
            elif resp.status == 403:
                raise SubredditPrivated(f'The subreddit r/{sub} was privated.', resp.status)
            elif resp.status != 200:
                raise RedditError(f'Something went wrong (status code {resp.status})', resp.status)
            data = await resp.json()
            data = data['data']['children']
            return [Post(data['data']) for data in data]

        
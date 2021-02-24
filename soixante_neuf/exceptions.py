class RedditError(Exception):
    def __init__(self, message, status_code):
        super(RedditError, self).__init__(message)
        self.status_code = status_code 

class SubredditNotFound(RedditError):
    pass 

class SubredditPrivated(RedditError):
    pass 
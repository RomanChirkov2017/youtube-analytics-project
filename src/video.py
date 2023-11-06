from src.apimix import ApiMixin


class Video(ApiMixin):

    def __init__(self, video_id):
        self.__video_id = video_id
        try:
            self.video = self.get_service().videos().list(
            id=video_id, part='snippet,statistics'
            ).execute()
            self.id = self.video['items'][0]['id']
            self.title = self.video['items'][0]['snippet']['title']
            self.url = f'https://youtu.be/{self.__video_id}'
            self.view_count = int(self.video['items'][0]['statistics']['viewCount'])
            self.like_count = int(self.video['items'][0]['statistics']['likeCount'])

        except(IndexError, TypeError):
            self.title = self.url = self.view_count = self.like_count = None

    def __str__(self):
        return f'{self.title}'

    @property
    def video_id(self) -> str:
        return self.__video_id


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

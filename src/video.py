from src.apimix import ApiMixin


class Video(ApiMixin):

    def __init__(self, video_id):
        self.__video_id = video_id
        self.video = self.get_service().videos().list(
            id=video_id, part='snippet,statistics'
        ).execute()
        self.id = self.video['items'][0]['id']
        self.title_video = self.video['items'][0]['snippet']['title']
        self.url = f'https://youtu.be/{self.__video_id}'
        self.video_count = int(self.video['items'][0]['statistics']['viewCount'])
        self.video_likes = int(self.video['items'][0]['statistics']['likeCount'])

    def __str__(self):
        return f'{self.title_video}'


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

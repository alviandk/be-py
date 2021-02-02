from django.conf import settings

from django_oss_storage.backends import (
    OssMediaStorage,
    OssStaticStorage,
    OssStorage
)


class BepyOssStaticStorage(OssStorage):

    def __init__(self, bucket_name=None):
        self.location = settings.STATIC_URL
        bucket_static = settings.BEPY_STATIC_BUCKET_NAME
        super(BepyOssStaticStorage, self).__init__(bucket_name=bucket_static)
        
class BepyOssMediaStorage(OssStorage):
    def __init__(self, bucket_name=None):
        self.location = settings.MEDIA_URL
        bucket_media = settings.BEPY_MEDIA_BUCKET_NAME
        super(BepyOssMediaStorage, self).__init__(bucket_name=bucket_media)
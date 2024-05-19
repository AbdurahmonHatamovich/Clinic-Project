import uuid

class SaveMediaFiles(object):

    def doctor_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/doctors/{uuid.uuid4()}.{image_extension}'


    def comments_image_path(instance, filename):
        image_extension = filename.split('.')[-1]
        return f'media/comments/{uuid.uuid4()}.{image_extension}'

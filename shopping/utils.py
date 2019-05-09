from uuid import uuid4
import os

def uuid_upload_to(instance , filename):
    ext = os.path.splitext(filename)[-1].lower() #2개의 값인데 마지막값을 가져온다
    uuid_name= uuid4().hex
    return '/'.join([
        uuid_name[:2], # 처음 두글자 256가지 조합
        uuid_name[2:4], # 그다음 두글자 
        uuid_name[4:] +ext #경로+확장자
    ])
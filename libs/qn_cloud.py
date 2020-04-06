from qiniu import Auth,put_file
from xiaoban import cfg
def upto_qn(filename,filepath):
    access_key = cfg.QN_ACCESS_KEY
    secret_key = cfg.QN_SECRET_KEY

    q = Auth(access_key,secret_key)
    bucket_name = cfg.QN_BUCKET
    token = q.upload_token(bucket_name,filename,3600)
    put_file(token,filename,filepath)
    return f'{cfg.QN_LOADURL}{filename}'

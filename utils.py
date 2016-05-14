ALLOWED_EXTENSIONS = ["pdf", "docx", "doc"]


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS
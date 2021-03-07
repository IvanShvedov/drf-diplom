
def update_worker(model, **kwargs):
    model.name = kwargs.get('name')
    model.mailing = kwargs.get('mailing')
    model.gender = kwargs.get('gender')
    model.language = clear_str(kwargs.get('language'))
    model.birthday = kwargs.get('birthday')
    model.city = kwargs.get('city')
    model.phone = clear_str(kwargs.get('phone'))
    model.about = kwargs.get('about')
    model.social_links = clear_str(kwargs.get('social_links'))
    model.citizenship = kwargs.get('citizenship')
    model.profile_link = kwargs.get('profile_link')
    model.photo_url = kwargs.get('photo_url')
    model.profile_background = kwargs.get('profile_background')
    return model


def clear_str(string):
    if string is not None:
        return str(string).replace('[', '').replace(']', '').replace("'", "")
    return None
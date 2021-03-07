
def update_worker(model, **kwargs):
    model.name = kwargs.get('name')
    model.mailing = kwargs.get('mailing')
    model.gender = kwargs.get('gender')
    model.language = kwargs.get('language')
    model.birthday = kwargs.get('birthday')
    model.city = kwargs.get('city')
    model.phone = kwargs.get('phone')
    model.about = kwargs.get('about')
    model.social_links = kwargs.get('social_links')
    model.citizenship = kwargs.get('citizenship')
    model.profile_link = kwargs.get('profile_link')
    model.photo_url = kwargs.get('photo_url')
    model.profile_background = kwargs.get('profile_background')

    model.experience = kwargs.get('experience')
    model.education = kwargs.get('education')
    return model


def update_employer(model, **kwargs):
    model.name = kwargs.get('name')
    model.name = kwargs.get('mailing')
    model.name = kwargs.get('address')
    model.name = kwargs.get('profile_background')
    model.name = kwargs.get('photo_url')
    model.name = kwargs.get('links')
    model.name = kwargs.get('phone')
    model.name = kwargs.get('profile_link')
    model.name = kwargs.get('about')
    return model

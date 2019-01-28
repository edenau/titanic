from pre_processing import pre_processing

def fit_model(sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked, model, scaler):

    processed_x = pre_processing(sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked, scaler)
    #pred_class = model.predict(processed_x)
    prob = model.predict_proba(processed_x)[0,1]

    # HTML formatting
    html = ''
    # Hard binary classifier
    '''
    html = addContent(html, header('Oh...', color='darkblue'))
    if pred == 1:
        html = addContent(html, box('You would have survived!'))
    else:
        html = addContent(html, box('You would have died.'))
    '''

    # Soft binary classifier
    html = addContent(html, box('Your survival probability would be...'))

    if prob < 0.17:
        color = '#6D2028'
    elif prob < 0.34:
        color = '#FF4C49'
    elif prob < 0.51:
        color = '#FF8C42'
    elif prob < 0.68:
        color = '#FF9F63'
    else:
        color = '#6EA1D1'

    html = addContent(html, header('{:.2%}'.format(prob), color=color))

    return f'<div>{html}</div>' #<div>{gen_html}</div><div>{a_html}</div>'


# Create an HTML header
def header(text, color='black', gen_text=None):

    if gen_text:
        raw_html = f'<h1 style="margin-top:16px;color: {color};font-size:54px"><center>' + str(
            text) + '<span style="color: red">' + str(gen_text) + '</center></h1>'
    else:
        raw_html = f'<h1 style="margin-top:12px;color: {color};font-size:54px"><center>' + str(
            text) + '</center></h1>'
    return raw_html

# Create an HTML box of text
def box(text, gen_text=None):

    if gen_text:
        raw_html = '<div style="padding:8px;font-size:28px;margin-top:28px;margin-bottom:14px;">' + str(
            text) + '<span style="color: red">' + str(gen_text) + '</div>'

    else:
        raw_html = '<div style="border-bottom:1px inset black;border-top:1px inset black;padding:8px;font-size: 28px;">' + str(
            text) + '</div>'
    return raw_html

# Concatenate html content together
def addContent(old_html, raw_html):

    old_html += raw_html
    return old_html

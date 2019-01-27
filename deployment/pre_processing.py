def pre_processing(sex, title, age, Pclass, cabin, SibSp, ParCh, fare, embarked, scaler):

    x = [sex, age, SibSp, ParCh, fare, cabin]

    # One-hot encode, delete first column
    if Pclass == 2:
        x.extend([1])
    else:
        x.extend([0])
    if Pclass == 3:
        x.extend([1])
    else:
        x.extend([0])
    #####
    if embarked == 'Q':
        x.extend([1])
    else:
        x.extend([0])
    if embarked == 'S':
        x.extend([1])
    else:
        x.extend([0])
    #####
    if title == 'Miss':
        x.extend([1])
    else:
        x.extend([0])
    if title == 'Mr':
        x.extend([1])
    else:
        x.extend([0])
    if title == 'Mrs':
        x.extend([1])
    else:
        x.extend([0])
    if title == 'Rare':
        x.extend([1])
    else:
        x.extend([0])

    # Family size
    x.extend([SibSp+ParCh+1])

    # Is alone
    if (SibSp == 0) & (ParCh == 0):
        x.extend([1])
    else:
        x.extend([0])

    x = scaler.transform([x])
    return x

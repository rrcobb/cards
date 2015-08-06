# Write your function here!
def everyone_sign(names):
    result = {}

    for name in names:
        message = "I'll miss you! Thanks for the memories! Yours"
        for friend in names:
            # Don't sign your own name!
            if friend == name:
                # do nothing
                pass
            else:
                message += ", " + friend
        # add signature to a dictionary
        result[name] = message

    return result

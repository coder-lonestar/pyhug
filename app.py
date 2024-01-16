import hug


@hug.get(examples="name=Prashanth&age=31")
@hug.local()
def greet(name: hug.types.text, age: hug.types.number, hug_timer=3):
    """Greets user"""
    return {
        "message": "Hello {0}. Have a nice day!".format(name),
        "took": float(hug_timer),
    }

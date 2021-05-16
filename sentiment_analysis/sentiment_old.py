import text2emotion as te

# text = """I was asked to sign a third party contract a week out from stay. If it wasn't an 8 person group that took a lot of wrangling I would have cancelled the booking straight away. Bathrooms - there are no stand alone bathrooms. Please consider this - you have to clear out the main bedroom to use that bathroom. Other option is you walk through a different bedroom to get to its en-suite. Signs all over the apartment - there are signs everywhere - some helpful - some telling you rules. Perhaps some people like this but It negatively affected our enjoyment of the accommodation. Stairs - lots of them - some had slightly bending wood which caused a minor injury."""

text = """
The silicon chip inside her head
Gets switched to overload.
And nobody's gonna go to school today,
She's going to make them stay at home.
And daddy doesn't understand it,
He always said she was as good as gold.
And he can see no reasons
'Cause there are no reasons
What reason do you need to be shown?

Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I want to shoot
The whole day down.


The telex machine is kept so clean
As it types to a waiting world.
And mother feels so shocked,
Father's world is rocked,
And their thoughts turn to
Their own little girl.
Sweet 16 ain't so peachy keen,
No, it ain't so neat to admit defeat.
They can see no reasons
'Cause there are no reasons

What reason do you need?
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I want to shoot
The whole day down, down, down.

Shoot it all down


All the playing's stopped in the playground now
She wants to play with her toys a while.
And school's out early and soon we'll be learning
And the lesson today is how to die.
And then the bullhorn crackles,
And the captain tackles,
With the problems and the how's and why's.
And he can see no reasons
'Cause there are no reasons
What reason do you need to die?

The silicon chip inside her head
Gets switched to overload.
And nobody's gonna go to school today,
She's going to make them stay at home.
And daddy doesn't understand it,
He always said she was as good as gold.
And he can see no reasons
'Cause there are no reasons
What reason do you need to be shown?

Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
Tell me why?
I don't like, I don't like
Tell me why?
I don't like Mondays.
Tell me why?
I don't like, I don't like
Tell me why?
I don't like Mondays.
Tell me why?
I don't like Mondays.
I wanna shoot,
The whole day down.
"""

print(te.get_emotion(text))
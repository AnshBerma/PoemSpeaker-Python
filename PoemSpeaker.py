import pyttsx3
engine = pyttsx3.init()

engine.say("Twinkle, twinkle, little star, How I wonder what you are, Up above the world so high, Like a diamond in the sky, When the traveller in the dark, Thanks you for thy tiny spark, He could not see which way to go, If you did not twinkle so, When the blazing sun is gone, And he nothing shines upon, Then appears thy tiny spark, Twinkle, twinkle, in the dark")
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)
engine.runAndWait()
